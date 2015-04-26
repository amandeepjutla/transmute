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

            self.cursor.execute("SELECT Name FROM %s" % table)
            self.drugs = self.cursor.fetchall()

    def get_drug(self, query):
        for drug in self.contents:
            if query in drug:
                return drug

    def drug_dictionary(self):
        dump = []
        dictionary = {}
        for drug in self.drugs:
            dump.append(drug)
        for i, row in enumerate(dump):
            n = []
            for col in range(0, len(row)):
                n.append(row[col])
            dictionary[i] = n
        return dictionary

class TransmuteAntipsychotics(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        self.parent = parent
        self.antipsychotics = Database("drugs.sqlite", "ANTIPSYCHOTICS")
        self.assemble_interface()

    def assemble_interface(self):
        self.parent.title("Transmute: Antipsychotics")
        self.style = ttk.Style()
        self.style.theme_use("default")
        self.draw_listboxes(23, self.antipsychotics.drug_dictionary().values())

        self.pack(fill=tkinter.BOTH, expand=1, side=tkinter.LEFT)
        self.draw_entry_box()
        self.draw_from_field("antipsychotic")
        self.draw_result_label()
        self.draw_to_field("antipsychotic")

        frame = ttk.Frame(self, relief=tkinter.FLAT, borderwidth=1)
        frame.pack(fill=tkinter.BOTH, expand=1)
        self.draw_buttons()

    def draw_listboxes(self, height, values):
        from_box = tkinter.Listbox(self, height=height)
        to_box = tkinter.Listbox(self, height=height)
  
        for drug in sorted(values):
            drug_string = str(drug)
            drug_string = drug_string.replace("'","").replace("[","").replace("]","")

            from_box.insert(tkinter.END, drug_string)
            to_box.insert(tkinter.END, drug_string)

        from_box.bind("<<ListboxSelect>>", self.clicked_from)
        from_box.pack(side=tkinter.LEFT, padx=5, pady=3)

        to_box.bind("<<ListboxSelect>>", self.clicked_to)
        to_box.pack(side=tkinter.LEFT)

    def draw_entry_box(self):
        self.dose_entry = ttk.Entry(self, width=35)
        self.dose_entry.pack(side=tkinter.TOP, anchor=tkinter.W, padx=5, pady=3)

    def draw_result_label(self):
        self.result_given = tkinter.StringVar()
        self.result_given.set("?")
        self.result_label = ttk.Label(self, anchor=tkinter.W, textvariable=self.result_given, width=35, relief=tkinter.RAISED, background="white")
        self.result_label.pack(side=tkinter.TOP, anchor=tkinter.W, padx=5, pady=3)

    def draw_from_field(self, drug_type):
        self.convert_from = tkinter.StringVar()
        self.convert_from.set("mg of one "+drug_type+" roughly equates to:")
        self.label_from = ttk.Label(self, anchor=tkinter.W, textvariable=self.convert_from, width=35)
        self.label_from.pack(side=tkinter.TOP, anchor=tkinter.W, padx=5, pady=3)

    def draw_to_field(self, drug_type):
        self.convert_to = tkinter.StringVar()
        self.convert_to.set("mg of another "+drug_type+".")
        self.label_to = ttk.Label(self, anchor=tkinter.W, textvariable=self.convert_to)
        self.label_to.pack(side=tkinter.TOP, anchor=tkinter.W, padx=5, pady=3)

    def draw_buttons(self):
        convert_button = ttk.Button(self, text="Convert", command = self.convert)
        convert_button.pack(side=tkinter.LEFT, padx=5, pady=3)

        exit_button = ttk.Button(self, text="Exit", command = self.kill)
        exit_button.pack(side=tkinter.LEFT, padx=5, pady=3)

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

root = tkinter.Tk()
transmute_antipsychotics = TransmuteAntipsychotics(root)
root.mainloop()