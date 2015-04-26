#transmute: antipsychotic tool

import sqlite3
import tkinter
from tkinter import ttk

class Database(object):
    def __init__(self, filename, table):
        self.connection = sqlite3.connect(filename)

        with self.connection:
            self.connection.row_factory = sqlite3.Row
            self.cursor = self.connection.cursor()
            self.cursor.execute("SELECT * FROM %s" % table)
            self.contents = self.cursor.fetchall()

            self.cursor.execute("SELECT Name FROM ANTIPSYCHOTICS")
            self.drugs = self.cursor.fetchall()

    def get_drug(self, query):
        for drug in self.contents:
            if query in drug:
                return drug

    def dump_drugs(self):
        drug_list = []
        for drug in self.drugs:
            drug_list.append(drug)
        return drug_list

class TransmuteAntipsychotics(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Transmute: Antipsychotics")
        self.style = ttk.Style()
        self.style.theme_use("default")

        from_box = tkinter.Listbox(self, height=23)
        to_box = tkinter.Listbox(self, height=23)

        self.antipsychotics = Database("drugs.sqlite", "ANTIPSYCHOTICS")
    
        dumped = self.antipsychotics.dump_drugs()

        drug_dictionary = {}
        for i, row in enumerate(dumped):    
            l = []
            for col in range(0, len(row)):
                l.append(row[col]) 
            drug_dictionary[i] = l

        for drug in sorted(drug_dictionary.values()):
            drug_string = str(drug)
            drug_string = drug_string.replace("'","").replace("[","").replace("]","")

            from_box.insert(tkinter.END, drug_string)
            to_box.insert(tkinter.END, drug_string)

        from_box.bind("<<ListboxSelect>>", self.clicked_from)
        from_box.pack(side=tkinter.LEFT, padx=5, pady=3)

        to_box.bind("<<ListboxSelect>>", self.clicked_to)
        to_box.pack(side=tkinter.LEFT)

        self.pack(fill=tkinter.BOTH, expand=1, side=tkinter.LEFT)

        self.dose_entry = ttk.Entry(self, width=35)
        self.dose_entry.pack(side=tkinter.TOP, anchor=tkinter.W, padx=5, pady=3)

        self.convert_from = tkinter.StringVar()
        self.convert_from.set("mg of one antipsychotic roughly equates to:")
        self.label_from = ttk.Label(self, anchor=tkinter.W, textvariable=self.convert_from, width=35)
        self.label_from.pack(side=tkinter.TOP, anchor=tkinter.W, padx=5, pady=3)

        self.result_given = tkinter.StringVar()
        self.result_given.set("?")
        self.result_label = ttk.Label(self, anchor=tkinter.W, textvariable=self.result_given, width=35, relief=tkinter.RAISED, background="white")
        self.result_label.pack(side=tkinter.TOP, anchor=tkinter.W, padx=5, pady=3)

        self.convert_to = tkinter.StringVar()
        self.convert_to.set("mg of another antipsychotic.")
        self.label_to = ttk.Label(self, anchor=tkinter.W, textvariable=self.convert_to)
        self.label_to.pack(side=tkinter.TOP, anchor=tkinter.W, padx=5, pady=3)

        frame = ttk.Frame(self, relief=tkinter.FLAT, borderwidth=1)
        frame.pack(fill=tkinter.BOTH, expand=1)

        convert_button = ttk.Button(self, text="Convert", command = self.convert)
        convert_button.pack(side=tkinter.LEFT, padx=5, pady=3)

        exit_button = ttk.Button(self, text="Exit", command = self.kill)
        exit_button.pack(side=tkinter.LEFT, padx=5, pady=3)

    def give_result(self, result):
        toplevel = Toplevel()
        frame = ttk.Frame(self, borderwidth=1)
        frame.pack()

        label1 = ttk.Label(toplevel, text=result)
        label1.pack()

    def convert(self):
        db_from = self.antipsychotics.get_drug(from_drug)
        db_to = self.antipsychotics.get_drug(to_drug)
        dose = self.dose_entry.get()

        try:
            multiplier = float(db_from["CF"])/float(db_to["CF"])
            result = float(dose) * multiplier
            self.result_given.set(result)
        except:
            self.result_given.set("Enter a numeric dose above.")

    def clicked_from(self, val):
        sender = val.widget
        idx = sender.curselection()
        global from_drug 
        from_drug = sender.get(idx)
        self.convert_from.set("mg of "+from_drug+" roughly equates to:")

    def clicked_to(self, val):
        sender = val.widget
        idx = sender.curselection()
        global to_drug
        to_drug = sender.get(idx)
        self.convert_to.set("mg of "+to_drug+".")

    def kill(self):
        self.quit()

def main():
    root = tkinter.Tk()
    app = TransmuteAntipsychotics(root)
    root.mainloop()

main()