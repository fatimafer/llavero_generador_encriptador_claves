#Esto ya lo tenemos
#Importamos la librería
import sqlite3 as sl
#creamos nuestra base de datos para guardar contraseñas
con = sl.connect('llavero.db')
with con:
    con.execute("""
        CREATE TABLE user_pass (
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            aplicacion TEXT,
            contraseña TEXT
        );
    """)
print('se ha creado su llavero')
#Creamos las contraseñas
aplicaciones = ["Gmail", "Tinder", "Twitter", "Tiktok", "Instagram"]
contrasenas = ["20051206Correo!", "qwerasdf1234#", "Tw2022+LMP", "Tik2022*VTP",
"Ins2022!MFR"]
#Las guardamos todas en un array tipo [(app1,pass1),(app2,pass2),etc.]
listasql = []
for i in range(len(aplicaciones)):
  listasql.append((aplicaciones[i],contrasenas[i]))
#Pasamos las contraseñas a nuestra base de datos
sql = 'INSERT INTO user_pass (aplicacion, contraseña) values(?, ?)'
data = listasql
with con:
    con.executemany(sql, data)
#Mostramos las contraseñas guardadas
print('Las contraseñas introducidas son: ')
with con:
    data = con.execute("SELECT aplicacion, contraseña FROM user_pass")
    for row in data:
        print(row[0]," ",row[1])
