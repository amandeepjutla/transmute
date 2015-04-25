from Tkinter import Tk, RIGHT, LEFT, TOP, BOTTOM, BOTH, RAISED, END, SW, W, Listbox, StringVar
from ttk import Frame, Button, Style, Label
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

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    def initUI(self):
        self.parent.title("Transmute")
        self.style = Style()
        self.style.theme_use("default")

        box1 = Listbox(self)
        box2 = Listbox(self)

        antipsychotics = Database("drugs.sqlite", "ANTIPSYCHOTICS")
        
        dumped = antipsychotics.dump_drugs()

        d = {}
        for i, row in enumerate(dumped):    
            l = []
            for col in range(0, len(row)):
                l.append(row[col]) 
            d[i] = l
        for drug in d.values():
            drug_string = str(drug)
            drug_string = drug_string.replace("'","").replace("[","").replace("]","")
            drug_string = drug_string[1:]
            box1.insert(END, drug_string)

            box2.insert(END, drug_string)

        box1.bind("<<ListboxSelect>>", self.onSelect1)
        box1.pack(side=LEFT, padx=5, pady=5)

        box2.bind("<<ListboxSelect>>", self.onSelect2)
        box2.pack(side=LEFT)

        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=1)
        self.pack(fill=BOTH, expand=1, side=LEFT)

        self.convert_from = StringVar()
        self.convert_from.set("From: ")
        self.label_from = Label(self, anchor=W, textvariable=self.convert_from)
        self.label_from.pack(side=TOP, anchor=W, padx=5)

        self.convert_to = StringVar()
        self.convert_to.set("To: ")
        self.label_to = Label(self, anchor=W, textvariable=self.convert_to)
        self.label_to.pack(side=TOP, anchor=W, padx=5, pady=5)

        okButton = Button(self, text="Exit")
        okButton.pack(side=BOTTOM, padx=5, pady=5)

        closeButton = Button(self, text="Convert")
        closeButton.pack(side=BOTTOM)

    def onSelect1(self, val):
        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)
        self.convert_from.set("From: "+value)

    def onSelect2(self, val):
        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)
        self.convert_to.set("To: "+value)

def main():
    root = Tk()
    app = Example(root)
    root.mainloop()

main()