import sqlite3

# db structure:
# name, tradename, class, conversion-factor, typicaldose
# Name, Trade, Class, CF, Typical

connection = sqlite3.connect("drugs.sqlite")

with connection:
    connection.row_factory = sqlite3.Row

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Drugs")

    drugs = cursor.fetchall()

    for drug in drugs:
        print drug["Name"]
        print drug["Trade"]
        print drug["Class"]
        print drug["CF"]
        print drug["Typical"]