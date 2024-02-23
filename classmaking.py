import sqlite3


class database():
    def __init__(self,db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS contact (id INTEGER PRIMARY KEY,neme text,lname text,addres text,phone text)""")
        self.con.commit()

    def insert(self,name,lname,addres,phone):
        self.cur.execute("""INSERT INTO contact VALUES(NULL,?,?,?,?)""" , (name,lname,addres,phone))
        self.con.commit()


    def delete(self):
        self.cur.execute("DELETE FROM contact WHERE id = ?", (id,))
        self.con.commit()


    def fetch(self):
        self.cur.execute('SELECT * FROM contact')
        rows = self.cur.fetchall()
        return rows
        

d1 = database('D:/python project/database/classmakingdata.db')

# for i in range(2):
#     name = input('n')
#     lname = input('l')
#     addres = input('a')
#     phone = input('p')
#     d1.insert(name,lname,addres,phone)

record =(d1.fetch())
for i in record:
    print(f'name={i[1]}\tlname={i[2]}\n\taddres={i[3]}\tphone={i[4]}')
    print('===================')