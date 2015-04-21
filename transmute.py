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

    def send_contents(self):
        return self.contents

data = Database("drugs.sqlite")
drugs = data.send_contents()

for drug in drugs:
    print drug["Name"]
    print drug["Trade"]
    print drug["Class"]
    print drug["CF"]
    print drug["Typical"]