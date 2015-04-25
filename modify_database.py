import sqlite3
import sys

connection = sqlite3.connect("drugs.sqlite")

q = """
        INSERT INTO Benzodiazepines(Name, Trade, CF, PeakMin, PeakMax, HalfMin, HalfMax)
        VALUES(?, ?, ?, ?, ?, ?, ?)
        """
with connection:
    cursor = connection.cursor()
#already made
    cursor.execute("CREATE TABLE Benzodiazepines(Name TEXT, Trade TEXT, CF NUMERIC, PeakMin NUMERIC, PeakMax NUMERIC, HalfMin NUMERIC, HalfMax NUMERIC)")
    cursor.execute(q, ("alprazolam", "Xanax", 2, 1, 2, 9, 20))
    cursor.execute(q, ("bromazepam", "Lexotan", 0.167, 0.5, 8, 10, 20))
    cursor.execute(q, ("chlordiazepoxide", "Librium", .04, 1, 4, 24, 100))
    cursor.execute(q, ("clonazepam", "Klonopin", 4, 1, 4, 19, 60))
    cursor.execute(q, ("clorazepate", "Tranxene", .067, 0.5, 2, 36, 100))
    cursor.execute(q, ("diazepam", "Valium", .2, 1, 2, 30, 200))
    cursor.execute(q, ("estazolam", "ProSom", .5, 1, 6, 10, 24))
    cursor.execute(q, ("flurazepam", "Dalmane", .067, 0.5, 1, 40, 250))
    cursor.execute(q, ("lorazepam", "Ativan", 1, 2, 4, 8, 24))
    cursor.execute(q, ("midazolam", "Versed", .133, 0.5, 1, 3, 3))
    cursor.execute(q, ("oxazepam", "Serax", .067, 2, 3, 3, 25))
    cursor.execute(q, ("quazepam", "Doral", .05, 1.75, 1.75, 39, 120))
    cursor.execute(q, ("temazepam", "Restoril", 0.1, 2.5, 2.5, 3, 24))
    cursor.execute(q, ("triazolam", "Halcion", 4, 1, 2, 1.5, 5))