#APLICACIONES Y CONTRASEÑAS GUARDADAS EN EL LLAVERO
#creamos las listas para guardar los usuarios y contraseñas en el llavero
aplicaciones = []
contrasenas = []
#Importamos los usuarios y contraseñas de nuestro llavero
#Importamos la librería
import sqlite3 as sl
#Nos conectamos a nuestro llavero
con = sl.connect('llavero.db')
with con:
    data = con.execute("SELECT aplicacion, contraseña FROM user_pass")
    for row in data:
        aplicaciones.append(row[0])
        contrasenas.append(row[1])
#lista con las app en mayusculas
app_mayuscula = []
for i in range(len(aplicaciones)):
  app_mayuscula.append((aplicaciones[i].upper()))
#FUNCIONES PARA LA APP
#Lista de elementos que pueden aparecer en las contraseñas
minusculas = 'abcdefghijklmnopqrstuvwxyz'
mayusculas = minusculas.upper()
numeros = '0123456789'
caracteres = '!."$%&/()=?¿*+-'
#funcion probar la seguirdad de las contraseñas
def prueba_pass(passwd_prueba):
  prueba_mayus = False
  prueba_numeros = False
  prueba_caracteres = False
  prueba_long = False
  prueba_enc = False
  if len(passwd_prueba) > 6:
    prueba_long = True
  if passwd_prueba[0] != '·': #Las contraseñas no empezarán por · ya que utilizamos este caracter para saber si está encriptada
    prueba_enc = True
  for i in range(len(passwd_prueba)):
    if passwd_prueba[i] in (list(mayusculas)):
      prueba_mayus = True
    elif passwd_prueba[i] in (list(numeros)):
      prueba_numeros = True
    elif passwd_prueba[i] in (list(caracteres)):
      prueba_caracteres = True
  prueba_contraseña = prueba_mayus and prueba_numeros and prueba_caracteres and prueba_long and prueba_enc
  if prueba_contraseña == False:
    if prueba_enc == False:
      print('La contraseña no debe comenzar por ·')
    if prueba_long == False:
      print('Necesita una contraseña de al menos 6 elementos')
    if prueba_mayus == False:
      print('Necesita introducir al menos una mayuscula')
    if prueba_numeros == False:
      print('Necesita introducir al menos un número')
    if prueba_caracteres == False:
      print('Necesita introducir al menos un caracter')
  else:
    print('Enhorabuna, la contraseña introducida es correcta')
  return prueba_contraseña
#funcion para generar contraseña
def contrasenia(longitud):
  if nueva.upper() == 'A':
    print('ha elegido introducir una nueva contraseña')
    passwd = input('Introduzca la nueva contraseña ')
    #Vamos a llamar a la función prueba_pass para que nos diga si la contraseña creada es correcta
    while prueba_pass(passwd) == False:
      print('Inténtelo de nuevo')
      passwd = input('Introduzca la nueva contraseña ')
  else:
    print('ha elegido generar contraseña')
  #Le preguntamos al usuario la longitud de su contraseña
    longitud = int(input('Introduzca la longitud de la contraseña '))
    while longitud < 6:
      print('Escriba una longitud de al menos 6 caracteres')
      longitud = int(input('Introduzca la longitud de la contraseña '))
    import random
    from random import SystemRandom
#La contraseña debe de tener como mínimo un caracter, un número, una mayuscula y una minúscula
#Le pedimos que nos genere un número aleatorio de minusculas entre 1 y la longitud de la contraseña
#A la longitud de la contraseña, restamos 1 porque tiene que reservar al menos un espacio para 1 numero
#Le restamos otro porque tiene que reservar al menos 1 espacio para la mayúscula
#Le restamos otro porque tiene que reservar un espacio para el caracter
    long_minusculas = random.randrange(1,(longitud+1-3))
#Le pedimos que nos genere un número aleatorio de caracteres entre 1 y la longitud de la contraseña
#A la longitud de la contraseña, restamos la longitud de las minusculas calculada
#Le restamos otro porque tiene que reservar al menos 1 espacio para el número
#Le restamos otro porque tiene que reservar un espacio para el caracter
    long_mayusculas = random.randrange(1,(longitud+1-long_minusculas-2))
#Le pedimos que nos genere un número aleatorio de caracteres entre 1 y la longitud de la contraseña
#A la longitud de la contraseña, restamos la longitud de los caracteres calculada
#Le restamos la longitud de las mayúsculas calcluladas
#Le restamos otro porque tiene que reservar un espacio para el caracter
    long_numeros = random.randrange(1,(longitud+1-long_minusculas-long_mayusculas-1))
#A la longitud de la contraseña, restamos la longitud de los caracteres calculada
#Le restamos la longitud de los números calculados
#Le restamos la longitud de las mayúsculas calculada
    long_caracteres = longitud - long_minusculas - long_numeros - long_mayusculas
#Creamos un string con mayusculas minúsculas y números
    string_prueba = ""
    for i in range(long_minusculas):
      string_prueba = string_prueba + random.choice(minusculas)
    for i in range(long_mayusculas):
      string_prueba = string_prueba + random.choice(mayusculas)
    for i in range(long_numeros):
      string_prueba = string_prueba + random.choice(numeros)
    for i in range(long_caracteres):
      string_prueba = string_prueba + random.choice(caracteres)
#Vamos a crear un string que nos genere posiciones aleatorias para mezclar los caracteres autogenerados
    posiciones = []
    posicion = 0
    while len(posiciones) < len(string_prueba):
      posicion = random.randrange(0,(len(string_prueba)))
      if posicion not in posiciones:
        posiciones.append(posicion)
#Nos va a posicionar los caracteres de la contraseña según lo indicado en el string anterior
    passwd = ""
    for i in range(len(posiciones)):
      passwd = passwd + string_prueba[posiciones[i]]
  return passwd
#PARA ENCRIPTAR
murcielago = ['M', 'U', 'R', 'C', 'I', 'E', 'L', 'A', 'G', 'O']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

#funcion encriptar
def encriptar(pass_nueva):
  pass_enc = "·"
  for i in range(len(pass_nueva)):
    if pass_nueva[i] in murcielago:
      for j in range(len(murcielago)):
        if pass_nueva[i] == murcielago[j]:
          pass_enc = pass_enc + numeros[j]
    elif pass_nueva[i] in numeros:
      for k in range(len(numeros)):
        if pass_nueva[i] == numeros[k]:
          pass_enc = pass_enc + murcielago[k]
    else:
      pass_enc = pass_enc + pass_nueva[i]
  return(pass_enc)

#funcion desencriptar
def desencriptar(password_enc):
  pass_desc = ""
  for i in range(1,len(password_enc)):
    if password_enc[i] in murcielago:
      for j in range(len(murcielago)):
        if password_enc[i] == murcielago[j]:
          pass_desc = pass_desc + numeros[j]
    elif password_enc[i] in numeros:
      for k in range(len(numeros)):
        if password_enc[i] == numeros[k]:
          pass_desc = pass_desc + murcielago[k]
    else:
      pass_desc = pass_desc + password_enc[i]
  return(pass_desc)

#PROGRAMA LLAVERO
pass_old = "" #Vamos a declarar una variable que nos va a guardad la contraseña antigua por si el usuario la cambia y después quiere recuperarla
pos_cont = 0 #Vamos a guardar la posición de la matriz donde estaba la contraseña antigua
accion_ant = 'Ninguna' #Vamos a guardar la accion anterior que realizó el usuario por si la quiere deshacer
seleccion = input('Bienvenido a su llavero de contraseñas, ¿Desea realizar alguna acción? S/N ')
while seleccion.upper() not in ['N','S']:
  seleccion = input('Elija una opcion correcta S/N ')
while seleccion.upper() != 'N':
  print('Elija una de las siguientes opciones')
  opcion = input('A Agregar nueva contraseña \n B Buscar una aplicacion \n C Deshacer última contraseña \n D modificar una contraseña \n E salir ')
  while opcion.upper() not in ['A','B','C','D','E']:
    print('Elija una opcion correcta')
    opcion = input('A Agregar nueva contraseña \n B Buscar una aplicacion \n C Deshacer última contraseña \n D modificar una contraseña \n E salir')
  if opcion.upper() == 'E':
    seleccion = 'N'
  else:
#AGREGAR NUEVAS CONTRASEÑAS
    if opcion.upper() == 'A':
      print('Su seleccion ha sido A \n sus aplicaciones guardadas son')
      for i in range(len(aplicaciones)):
        print(aplicaciones[i])
      aplicacion = input('¿Para qué aplicación desea agregar la nueva contraseña? \n escriba N si no desea añadir ninguna aplicación ')
      while (aplicacion.upper() in app_mayuscula):
        print('Esa aplicacion ya está en su llavero ')
        aplicacion = input('¿Para qué aplicación desea agregar la nueva contraseña? \n escriba N si no desea añadir ninguna aplicación ')
      if aplicacion.upper() == 'N':
        print('No se ha añadido ninguna aplicación')
      else:
        aplicaciones.append(aplicacion)
        app_mayuscula.append((aplicaciones[(len(aplicaciones))-1].upper()))
        nueva = input('Desea \n A -Introducir una nueva contraseña \n B -Que el sistema genere una nueva ')
        while nueva.upper() not in ['A','B']:
          print('Opción incorrecta')
          nueva = input('Desea \n A -Introducir una nueva contraseña \n B -Que el sistema genere una nueva ')
        pass_new = contrasenia(nueva)
        cripto = input('¿Desea encriptarla? S/N ')
        while cripto.upper() not in ['N','S']:
          cripto = input('Elija una opcion correcta S/N ')
        if cripto.upper() == 'S':
          contrasenas.append(encriptar(pass_new))
        else:
          contrasenas.append(pass_new)
        if cripto.upper() == 'S':
          print(f'La contraseña generada es {contrasenas[(len(contrasenas))-1]} \n y ha sido añadida a su llavero. \n Tenga en cuenta que se está mostrando encriptada')
        else:
          print(f'La contraseña generada es {contrasenas[(len(contrasenas))-1]} \n y ha sido añadida a su llavero')
#VER LA CONTRASEÑA
    elif opcion.upper() == 'B':
      print('Su seleccion ha sido B')
      print('Usted tiene guardadas contraseñas para las siguientes aplicaciones')
      for i in range(len(aplicaciones)):
        print(aplicaciones[i])
      app = input('seleccione una de ellas ')
      while app.upper() not in app_mayuscula:
        print('La aplicación seleccinada no se encuentra en el llavero')
        app = input('Indique la aplicación correcta ')
      for i in range(len(app_mayuscula)):
        if app_mayuscula[i] == app.upper():
          password1 = contrasenas[i]
      if password1[0] == "·":
        password1 = desencriptar(password1)
      print(f'la contraseña de {app} es {password1}')
#DESHACER LA ULTIMA ACCION
    elif opcion.upper() == 'C':
      print('Su seleccion ha sido C')
      if accion_ant == 'A':
        print('Su accion anterior fue añadir una apliación nueva')
        cambio = input('¿Desea continuar? S/N ')
        while cambio.upper() not in ['N','S']:
          cambio = input('Elija una opcion correcta S/N ')
        if cambio.upper() == 'S':
          print(f'se ha eliminado su aplicacion {aplicaciones[((len(aplicaciones))-1)]} y la contrasenia {contrasenas[((len(contrasenas))-1)]}')
          aplicaciones = aplicaciones[0:((len(aplicaciones))-2)]
          contrasenias = contrasenas[0:((len(contrasenas))-2)]
      if accion_ant == 'D':
        print('Su accion anterior fue cambiar la contraseña')
        cambio = input('¿Desea continuar? S/N ')
        while cambio.upper() not in ['N','S']:
          cambio = input('Elija una opcion correcta S/N ')
        if cambio.upper() == 'S':
          print(f'Se va a deshacer su contraseña guardada {contrasenas[pos_cont]} para la aplicacion {aplicaciones[pos_cont]}')
          contrasenas1 = contrasenas[0:(pos_cont)]
          contrasenas = contrasenas[(pos_cont+1):(len(contrasenas))]
          contrasenas1.append(pass_old)
          contrasenas1.extend(contrasenas)
          contrasenas = contrasenas1
          print('Se ha restaurado la contrasenia', contrasenas[pos_cont])
      elif accion_ant.upper() in ['B','C']:
        print('Su acción anterior fue ver la contraseña o deshacer una última acción. Esta opción no se puede deshacer')
#CAMBIAR CONTRASEÑA
    elif opcion.upper() == 'D':
      print('Su seleccion ha sido D')
      print('Usted tiene guardadas contraseñas para las siguientes aplicaciones')
      for i in range(len(aplicaciones)):
        print(aplicaciones[i])
      app = input('seleccione una de ellas ')
      while app.upper() not in app_mayuscula:
        print('La aplicación seleccinada no se encuentra en el llavero')
        app = input('Indique la aplicación correcta ')
      for i in range(len(app_mayuscula)):
        if app_mayuscula[i] == app.upper():
          pass_old = contrasenas[i] #Guardamos la contrasenia antigua por si el usuario decide deshacer cambios
          pos_cont = i #Guardamos la posicion en la matriz donde estaba la contrasenia antigua
          cambio = input(f'Desea cambiar la contraseña de {app} S/N ?')
      while cambio.upper() not in ['N','S']:
        cambio = input('Elija una opcion correcta S/N ')
      if cambio.upper() == 'S':
        nueva = input('Desea \n A -Introducir una nueva contraseña \n B -Que el sistema genere una nueva ')
        while nueva.upper() not in ['A','B']:
          print('Opción incorrecta')
          nueva = input('Desea \n A -Introducir una nueva contraseña \n B -Que el sistema genere una nueva ')
        pass_new = contrasenia(nueva)
        if pass_old[0] == "·":
          cripto = 'S'
          print('Como la contraseña anterior estaba encriptada, la nueva contraseña se encriptará')
        else:
          cripto = input('¿Desea encriptarla? S/N ')
          while cripto.upper() not in ['N','S']:
            cripto = input('Elija una opcion correcta S/N ')
        contrasenas1 = contrasenas[0:(pos_cont)] #Vamos a guardar la posiciones de las contraseñas anteriores a la modificada
        contrasenas = contrasenas[(pos_cont+1):(len(contrasenas))] #Vamos a guardar las posiciones de las contraseñas posteriores
        if cripto.upper() == 'S':
          contrasenas1.append(encriptar(pass_new)) #Añadimos la contraseña modificada encriptada
        else:
          contrasenas1.append(pass_new) #Añadimos la contraseña modificada sin encriptar
        contrasenas1.extend(contrasenas)
        contrasenas = contrasenas1
        if cripto.upper() == 'S':
          print(f'La contraseña generada es {contrasenas[pos_cont]} \n y ha sido añadida a su llavero. \n Tenga en cuenta que se está mostrando encriptada')
        else:
          print(f'La contraseña generada es {contrasenas[pos_cont]} \n y ha sido añadida a su llavero')
    accion_ant = opcion.upper()
    seleccion = input('¿Desea hacer algo más? S/N ')
  while seleccion.upper() not in ['N','S']:
    seleccion = input('Elija una opcion correcta S/N ')
#Eliminamos todas las contraseñas guardadas
with con:
  con.execute('DELETE FROM user_pass;')
#Guardamos apps y contraseñas en una lista tipo [(app1,pass1),(app2,pass2),etc.]
listasql = []
for i in range(len(aplicaciones)):
  listasql.append((aplicaciones[i],contrasenas[i]))
#Pasamos las contraseñas a nuestra base de datos
sql = 'INSERT INTO user_pass (aplicacion, contraseña) values(?, ?)'
data = listasql
with con:
    con.executemany(sql, data)
print('Hasta luego')
