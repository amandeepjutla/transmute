#from __future__ import division
import sqlite3

# db structure:
# name, tradename, class, conversion-factor, typicaldose
# Name, Trade, Class, CF, Typical

class Database(object):
    def __init__(self, filename):
        self.connection = sqlite3.connect(filename)

        with self.connection:
            self.connection.row_factory = sqlite3.Row
            self.cursor = self.connection.cursor()
            self.cursor.execute("SELECT * FROM Drugs")
            self.contents = self.cursor.fetchall()

    def get_drug(self, query):
        for drug in self.contents:
            if query in drug:
                return drug

data = Database("drugs.sqlite")

convert_from = raw_input("Convert from: ")
dosage = raw_input("Dosage in mg: ")
convert_to = raw_input("Convert to: ")

db_from = data.get_drug(convert_from)
db_to = data.get_drug(convert_to)

multiplier = float(db_from["CF"])/float(db_to["CF"])

result = float(dosage) * multiplier

print "Equivalent dose: ~"+str(result)+"mg"