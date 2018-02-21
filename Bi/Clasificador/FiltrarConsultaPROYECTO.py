import couchdb
import sys
import urllib2
import json
import re

URL='localhost'
db_name = 'mini'

'''========couchdb'=========='''
server = couchdb.Server('http://' + URL + ':5984/')  # ('http://localhost:5984/') poner la url de su base de datos
try:
    print
    db_name
    db = server[db_name]
    print
    'success'

except:
    sys.stderr.write("Error: DB not found. Closing...\n")
    sys.exit()

url = 'http://localhost:5984/mini/_design/vista/_view/ciudades'
req = urllib2.Request(url)
f = urllib2.urlopen(req)
d = json.loads(f.read())
s ="s"
n ="n"
positivo ="s"
negativo ="n"
print("hola")
cont=0
   
for x in d['rows']:
   cont =cont +1
   a = x['value']['text']
   b = a.upper()
   aux=","

   print("Tweet numero  "+ repr(cont) + ":" + b)
   cadena = input("Desea ingresar el  tweet a la base de datos")
   if(s == cadena):
      clase = input("Dar Calificacion al tweet")
      if(clase == positivo):
        datos = {
           "text": b, "label": "si"
        }
      elif(clase == negativo):
        datos = {
              "text": b, "label": "no"
        }
      with open('datos.json', 'a') as file:
        json.dump(datos, file)
        file.write(',\n')


#cl = NaiveBayesClassifier(file, format="json")