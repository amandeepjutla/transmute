import sqlite3
import sys

connection = sqlite3.connect("antipsychotics.sqlite")

q = """
        INSERT INTO Drugs(Name, Trade, Class, CF, Typical)
        VALUES(?, ?, ?, ?, ?)
        """
with connection:
    cursor = connection.cursor()
    cursor.execute(q, ("name", "trade", "class", 0, 0))