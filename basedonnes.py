import sqlite3

connection = sqlite3.connect('celibrite.db')

curseur = connection.cursor()
try:
    # curseur.execute(''' CREATE TABLE  IF NOT EXISTS Celibrites
    #                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
    #                     nom TEX,
    #                     prenom TEXT,
    #                     age INTEGER,
    #                     popularite REAL) ''')
    
    
                        
    # curseur.execute(''' INSERT INTO Celibrites(
    #         nom,prenom,age,popularite)
    #         VALUES("Rambo", "Rambo",50,8.7)
    #         ''')
    # curseur.execute(''' INSERT INTO Celibrites(
    #         nom,prenom,age,popularite)
    #         VALUES("JET ", "Lee",55,8.8)
    #         ''')
    # curseur.execute(''' INSERT INTO Celibrites(
    #         nom,prenom,age,popularite)
    #         VALUES("Jon", "Whoo",60,9.3)
    #         ''')
    
    # connection.commit()
    
    doonnes=curseur.execute(''' SELECT * FROM Celibrites ''')
    #print(doonnes.fetchone())
    print(doonnes.fetchall())
    
except Exception as e :
    print(e)
finally:
    connection.close()