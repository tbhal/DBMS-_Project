import sqlite3

class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS med(id INTEGER PRIMARY KEY,MedID INTEGER, MedName text, MedCost INTEGER, MedCompany text)")
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def insert(self, MedID, MedName, MedCost, MedCompany):
        self.cur.execute("INSERT INTO med VALUES (NULL, ?, ?, ?, ?)", (MedID, MedName, MedCost, MedCompany))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM med")
        rows = self.cur.fetchall()
        return rows

    def search(self, MedID = "", MedName = "", MedCost = "", MedCompany = ""):
        self.cur.execute("SELECT * FROM med WHERE MedID = ? OR MedName = ? OR MedCost = ? OR MedCompany = ?", (MedID, MedName, MedCost, MedCompany))
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM med WHERE id = ?", (id,))
        self.conn.commit()

    def update(self, id, MedID, MedName, MedCost, MedCompany):
        self.cur.execute("UPDATE med set MedID = ?, MedName = ?, MedCost = ?, MedCompany = ? WHERE id = ?", (MedID, MedName, MedCost, MedCompany, id))
        self.conn.commit()

#connect()
#insert("The sea", "Jhon", 1918, 123456)
#delete(3)
#update(4, "The sea2", "ice", 1920, 23456)
#print(view())
#print(search(author = "ice"))
