from textblob.classifiers import NaiveBayesClassifier
import json


fentrenamiento=open('datosentrenamientos.json', 'r')
cl = NaiveBayesClassifier(fentrenamiento,format="json")
fentrenamiento.close
cadena = input("Desea ingresar el  tweet para clasificar")
presicion=cl.accuracy(cadena)
print("Presision: "+str(presicion))
