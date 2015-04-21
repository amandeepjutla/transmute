import sqlite3
import sys

connection = sqlite3.connect("drugs.sqlite")

q = """
        INSERT INTO Drugs(Name, Trade, Class, CF, Typical)
        VALUES(?, ?, ?, ?, ?)
        """
with connection:
    cursor = connection.cursor()
    cursor.execute(q, ("aripiprazole", "Abilify", "other heterocyclic", 15, 20))
    cursor.execute(q, ("asenapine", "Saphris", "other heterocyclic", 20, 15))
    cursor.execute(q, ("iloperidone", "Fanapt", "other heterocyclic", 16.7, 18))
    cursor.execute(q, ("lurasidone", "Latuda", "other heterocyclic", 5, 60))
    cursor.execute(q, ("molindone", "Moban", "other heterocyclic", 10, 30))
    cursor.execute(q, ("paliperidone", "Invega", "other heterocyclic", 50, 6))
    cursor.execute(q, ("risperidone", "Risperdal", "other heterocyclic", 75, 4))
    cursor.execute(q, ("ziprasidone", "Geodon", "other heterocyclic", 2.5, 120))