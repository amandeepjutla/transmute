import sqlite3
import sys

connection = sqlite3.connect("drugs.db")

q = """
        INSERT INTO Drugs(Name, Trade, Class, CF, Typical)
        VALUES(?, ?, ?, ?, ?)
        """
with connection:
    cursor = connection.cursor()
#    cursor.execute(
 #       "CREATE TABLE Drugs(Name TEXT, Trade TEXT, Class TEXT, CF INT, Typical INT)")
    cursor.execute(q, ("fluphenazine", "Prolixin", "phenothiazine", 40, 7.5))
    cursor.execute(q, ("mesoridazine", "Serentil", "phenothiazine", 1.2, 250))
    cursor.execute(q, ("perphenazine", "Trilafon", "phenothiazine", 12.5, 24))
    cursor.execute(q, ("thioridazine", "Mellaril", "phenothiazine", 1, 300))
    cursor.execute(q, ("trifluoperazine", "Stelazine", "phenothiazine", 20, 15))
    cursor.execute(q, ("triflupromazine", "Vesprin", "phenothiazine", 3.8, 80))