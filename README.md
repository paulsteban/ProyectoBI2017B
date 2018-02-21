# ProyectoBI2017B
Machine learning (aprendizaje de maquina) es parte de la inteligencia artificial, para otorgarles la capacidad de aprender por sus propios medios, esto quiere decir que no necesitados estar programando consecutivamente.

El aprendizaje de maquina se toma como un gran aporte para el análisis estadístico por el uso de las computadoras, una de os mayores aplicativos es el realizar predicciones computacionales de datos previamente obtenidos de alguna fuente determinada. 

Se puede decir que el aprendizaje de maquina esta fuertemente relacionado también con la optimización matemática, esto se debe a que aporta con métodos, teoría y dominios de las aplicaciones para este campo.

El aprendizaje de maquina se combina con la extracción de datos, donde está más centrado en el análisis exploratorio de datos y se conoce como aprendizaje no supervisado.
Machine learning también se puede supervisar y utilizar para aprender y determinar perfiles de comportamiento básicos para diferentes entidades y luego encontrar anomalías importantes.

Análisis de sentimiento es el campo de estudio que analiza las opiniones, sentimientos, evaluaciones, actitudes de las personas, y emociones hacia entidades tales como productos, servicios, organizaciones, individuos, problemas, eventos, temas y sus atributos. 

El análisis de opinión y la minería de opinión se centra principalmente en las opiniones que expresan o implican sentimientos positivos o negativos. 

Se aplicara machine learning en la reacción de grandes masas en un sistema geográfico determinado mediante un análisis eficiente y eficaz que tome en cuenta los sentimientos para analizar los datos recogidos de la red social Twitter y obtener como resultado la inclinación política en general.


Método 

Adquisición de datos 

 

Los datos para analizar serán cosechados de Twitter que se publicaron en las ciudades más importantes del país. Para esto se ocupará CouchDb como gestor de base de datos que por medio de un script realizado en Python que almacena en tiempo real. 

 

Las coordenadas que usar son las siguientes: 

Quito: -78.332361, -0.371299, -78.546594, 0.020773 

Guayaquil:  -79.850098-2.282060, -80.078751, -2.026808 

Cuenca: -78.927926, -2.922271, -79.056500, -2.851636 

 

Los datos se obtuvieron desde 01/02/2018 hasta 05/02/218. 

  

Preprocesamiento 

Para filtrar los datos obtenidos de Quito, Guayaquil y Cuenca se lo pude realizar directamente en CouchDb. 

El código que se muestra a continuación fue usado para realizar vistas, las cuales permiten filtrar el texto, y obtener solo los que son en español. 

 

El código que se muestra a continuación fue usado para realizar vistas, las cuales permiten filtrar el texto, y obtener solo los que son en español. 

 

function (doc) { 

   if(doc.lang == "es"){ 

    emit(doc._id, {text: doc.text.replace(/[í]/gi, 'i').replace(/[^\w\s#.!]/gi, '')}); 

  } 

} 

 

Para filtrar los datos por ciudad, debido a que CouchDb no necesariamente recoge datos específicamente de las coordenadas indicadas, por lo tanto, usamos los siguientes códigos para cada ciudad. 

 

function (doc) { 

   if(doc.place.name == "Quito"){ 

    emit(doc._id, {text: doc.text.replace(/[í]/gi, 'i').replace(/[^\w\s#.!]/gi, '')}); 

  } 

} 

 

Para la vista de Guayaquil 

 

function (doc) { 

   if(doc.place.name == "Guayaquil"){ 

    emit(doc._id, {text: doc.text.replace(/[í]/gi, 'i').replace(/[^\w\s#.!]/gi, '')}); 

  } 

} 

 

Para la vista de Cuenca 

 

function (doc) { 

   if(doc.place.name == "Cuenca"){ 

    emit(doc._id, {text: doc.text.replace(/[í]/gi, 'i').replace(/[^\w\s#.!]/gi, '')}); 

  } 

} 

Procesamiento 

Aquí vamos a obtener los tweets que tengan como tema la consulta popular, esto realizar con el análisis de el texto que tiene cada tweet, para posteriormente ser clasificados como apoyo para el SI o el NO de dicha popular. 

Aprendizaje supervisado 

Para esto vamos a realizarlo con una técnica de aprendizaje supervisado, el código a usar fue realizado en Python. 

 

 

Expresiones regulares 

Como siguiente paso vamos a ocupar expresiones regulares para remover todos los caracteres especiales que tenemos en el texto de cada tweet. 

 

 

Clasificador 

Finalmente, se le otorgara todos estos datos al clasificador (TextBlob). 

 

Análisis 

TextBlob 

El principal clasificador que se uso es TextBlob que es una biblioteca para procesar texto de una base de datos, esta Api nos proporciona una característica para el análisis de sentimiento mediante el proceso del lenguaje natural. 

