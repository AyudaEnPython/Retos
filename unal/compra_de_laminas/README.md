# Enunciado Original

## Compra de laminas

Llego la fiebre futbolera nuevamente y ya estas muy cerca de completar el album
solo te faltan unas pocas laminas, en vez de seguir gastando en sobre, te
enteraste que en una chaza de la Universidad Nacional de Colombia se están
vendiendo las laminas a un cierto precio, tu decidiste ir allá e intentar
comprar las laminas que esta chaza vende.

Desarrolle un programa en python que dada el conjunto de laminas con sus precios
y el conjunto de laminas que te faltan separadas por espacios, imprima el precio
y el conjunto de laminas que pudiste encontrar en la chaza.

Se recibirán 2 entradas la primera sera un diccionario en formato JSON, la segunda
un conjunto de laminas separadas por espacio, deberás imprimir dos salidas, la
primera es el dinero que debes invertir para comprar las laminas y la segunda
linea debe tener las laminas que pudiste comprar separadas por espacio.

|Entrada                                                                                             |Salida        |
|----------------------------------------------------------------------------------------------------|--------------|
|{"d": 55, "o": 57, "p": 65, "t": 55, "s": 73, "f": 89, "e": 72, "k": 65, "y": 65}<br>g q h t w p y f|274<br>t p y f|

## Variante 1

Hugo, Pago y Luis están coleccionando las láminas Locombia Tierra Querida y
encontraron una tienda donde vende algunas láminas, cada lámina es vendida a
un cierto precio.
Como ellos tienen una lista con los códigos de las láminas que les hacen
falta, quieren saber los códigos de las láminas que pueden comprar y el precio
a pagar por dicha compra.

Realizar un programa que dado un diccionario (en formato JSON) que tiene las
parejas código: precio de todas las láminas que tiene la tienda, y que dada
la lista de códigos de láminas que les faltan a Hugo, Paco y Luis (separados por
espacios), imprima el precio de las láminas que pueden comprar y los códigos de
las láminas que pueden comprar:

|Entrada                                                                                             |Salida        |
|----------------------------------------------------------------------------------------------------|--------------|
|{"t": 66, "u": 72, "d": 90, "r": 84, "j": 36, "g": 50, "s": 94, "q": 62, "f": 35}<br>d p h u i e t q|290<br>d u t q|

## Variante 2

María está realizando mercado y necesita saber el valor total de su compra para saber
si le alcanza el dinero. Para ello ve en una pantalla los precios de los productos
vendidos por el supermercado. En la pantalla se ven las iniciales de los productos; es
decir que si María desea conocer el precio del café, la leche y los huevos; revisará
las iniciales: {"c": 50, "l": 20, "h": 40}

Ayuda a María a saber el total de su compra ingresando un diccionario (en formato JSON
que tiene las parejas inicial_del_producto: valor) correspondiente al listado de los
productos ofrecidos por el supermercado. Posteriormente ingresando los productos que
María desea llevar del supermercado.

El programa debe imprimir el valor total de la compra y en una línea nueva las iniciales
de los nombres de los productos llevados por María.

|Entrada                                                                                             |Salida        |
|----------------------------------------------------------------------------------------------------|--------------|
|{"t": 66, "u": 72, "d": 90, "r": 84, "j": 36, "g": 50, "s": 94, "q": 62, "f": 35}<br>d p h u i e t q|290<br>d u t q|

> __**NOTA**__: Los enunciados originales contienen errores.
