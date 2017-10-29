Descripción
===========

El siguiente programa lee una colección de documentos y genera un diccionario con 
cada palabra y la frecuencia de aparición de esa palabra. Luego, se crea otro 
diccionario de prefijos, el cual contiene el prefijo luego de realizar stemming y
las palabras que se asocian a ese prefijo. Por último, se genera un archivo de salida
para analizar los resultados de manera más simple.

### Dependencias

Se hace uso de Python 3.6 y la biblioteca [NTLK], que se puede adquirir con el 
siguiente comando desde la consola de comandos en modo administrador:

> pip install ntlk

### Ejecución

El programa se ejecuta con el archivo `main.py`. Para ello, se debe escribir el 
sigueinte comando:

> python main.py num_documentos nombre_resultados ruta_colección

Donde cada parámetro es:

* num_documentos: cantidad de documentos que se desea procesar de la colección.
* nombre_resultados: nombre con el que se va a guardar el archivo de resultados.
* ruta_colección: se refiere a la ruta sobre la que se va a realizar la ejecución.
Esta ruta debe tener subcarpetas y dentro de estas subcarpetas se encuentran los
archivos a leer.

### Resultados de casos de prueba

El rendimien
 

[NTLK]: http://www.nltk.org/