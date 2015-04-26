from tkinter import Tk, RIGHT, LEFT, TOP, BOTTOM, BOTH, FLAT, RAISED, SUNKEN, RIDGE, END, SW, W, Listbox, StringVar, Toplevel
from tkinter import ttk

#ttk import Frame, Button, Style, Label
import sqlite3

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

    def dict_gen(list):
        d = {}
        for i, row in enumerate(list):
            l = []
            for col in range(0, len(row)):
                l.append(row[col]) 
            d[i] = l
        return d

    def dump_drugs(self):
        drug_list = []
        for drug in self.drugs:
            drug_list.append(drug)
        return drug_list

class Example(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    def initUI(self):
        self.parent.title("Transmute")
        self.style = ttk.Style()
        self.style.theme_use("default")

        box1 = Listbox(self, height=23)
        box2 = Listbox(self, height=23)

        self.antipsychotics = Database("drugs.sqlite", "ANTIPSYCHOTICS")
    
        dumped = self.antipsychotics.dump_drugs()

        d = {}
        for i, row in enumerate(dumped):    
            l = []
            for col in range(0, len(row)):
                l.append(row[col]) 
            d[i] = l

        for drug in d.values():
            drug_string = str(drug)
            drug_string = drug_string.replace("'","").replace("[","").replace("]","")

            box1.insert(END, drug_string)
            box2.insert(END, drug_string)

        box1.bind("<<ListboxSelect>>", self.onSelect1)
        box1.pack(side=LEFT, padx=5, pady=3)

        box2.bind("<<ListboxSelect>>", self.onSelect2)
        box2.pack(side=LEFT)

        self.pack(fill=BOTH, expand=1, side=LEFT)

        self.dose_entry = ttk.Entry(self, width=35)
        self.dose_entry.pack(side=TOP, anchor=W, padx=5, pady=3)

        self.convert_from = StringVar()
        self.convert_from.set("mg of one antipsychotic roughly equates to:")
        self.label_from = ttk.Label(self, anchor=W, textvariable=self.convert_from, width=35)
        self.label_from.pack(side=TOP, anchor=W, padx=5, pady=3)

        self.result_given = StringVar()
        self.result_given.set("?")
        self.result_label = ttk.Label(self, anchor=W, textvariable=self.result_given, width=35, relief=RAISED, background="white")
        self.result_label.pack(side=TOP, anchor=W, padx=5, pady=3)

        self.convert_to = StringVar()
        self.convert_to.set("mg of another antipsychotic.")
        self.label_to = ttk.Label(self, anchor=W, textvariable=self.convert_to)
        self.label_to.pack(side=TOP, anchor=W, padx=5, pady=3)

        frame = ttk.Frame(self, relief=FLAT, borderwidth=1)
        frame.pack(fill=BOTH, expand=1)

        convert_button = ttk.Button(self, text="Convert", command = self.convert)
        convert_button.pack(side=LEFT, padx=5, pady=3)

        exit_button = ttk.Button(self, text="Exit", command = self.kill)
        exit_button.pack(side=LEFT, padx=5, pady=3)

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

        multiplier = float(db_from["CF"])/float(db_to["CF"])
        result = float(dose) * multiplier
        self.result_given.set(result)

#        self.give_result(result)

    def onSelect1(self, val):
        sender = val.widget
        idx = sender.curselection()
        global from_drug 
        from_drug = sender.get(idx)
        self.convert_from.set("mg of "+from_drug+" roughly equates to:")

    def onSelect2(self, val):
        sender = val.widget
        idx = sender.curselection()
        global to_drug
        to_drug = sender.get(idx)
        self.convert_to.set("mg of "+to_drug+".")

    def kill(self):
        self.quit()

def main():
    root = Tk()
    app = Example(root)
    root.mainloop()

main()