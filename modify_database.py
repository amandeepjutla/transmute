import sqlite3
import sys

connection = sqlite3.connect("drugs.sqlite")

q = """
        INSERT INTO Drugs(Name, Trade, Class, CF, Typical)
        VALUES(?, ?, ?, ?, ?)
        """
with connection:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE Benzodiazepines(Name TEXT, Trade TEXT, CF NUMERIC, PeakMin NUMERIC, PeakMax NUMERIC, HalfMin NUMERIC, HalfMax NUMERIC)")
#    cursor.execute(q, ("name", "trade", "class", 0, 0))