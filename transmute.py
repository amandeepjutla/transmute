#Transmute

import sqlite3

# db structure:
# name, tradename, class, conversion-factor, typicaldose
# Name, Trade, Class, CF, Typical

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

antipsychotics = Database("drugs.sqlite", "ANTIPSYCHOTICS")
benzodiazepines = Database("drugs.sqlite", "BENZODIAZEPINES")

mode = raw_input("Mode? 1 - Antipsychotics, 2 - Benzodiazepines: ")
convert_from = raw_input("Convert from: ")
dosage = raw_input("Dosage in mg: ")
convert_to = raw_input("Convert to: ")

if mode =="1":
    db_from = antipsychotics.get_drug(convert_from)
    db_to = antipsychotics.get_drug(convert_to)
    
else:
    db_from = benzodiazepines.get_drug(convert_from)
    db_to = benzodiazepines.get_drug(convert_to)

multiplier = float(db_from["CF"])/float(db_to["CF"])
result = float(dosage) * multiplier

print "Equivalent dose: ~"+str(result)+"mg"