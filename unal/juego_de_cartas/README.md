# Enunciado Original

# Juego de cartas

Los estudiantes de la Universidad de Colombia se cansaron del juego de
uno y decidieron inventarse un nuevo juego, este juego utiliza las 26
letras del abecedario sin incluir la ñ y se puede seleccionar mayúsculas
o minúsculas, la idea del juego es simple el usuario empieza sacar cartas
una por una hasta que encuentre una carta con una letra diferente a la
que había sacado previamente al llegar a ese escenario el usuario cuenta
cuantas veces se repitió dicho valor y así continua hasta que ya no pueda
sacar mas cartas.

Para hacer mas divertido el juego el usuario decidió tratar las mayúsculas
y minúsculas como iguales.

## Entrada

La entrada consta de una sucesión de caracteres separados por coma que
corresponden a las cartas sacadas por el jugador.

## Salida

La salida consta de dos líneas: la primera es la cartas que fue sacando en
cada turno hasta que encontró una diferente, el valor de la carta debe
escribirse en mayúscula y la segunda es la cantidad de repeticiones de esa
carta antes de que haya encontrado una diferente, cada una de los resultados
debe estar separado por espacio.

|Entrada                      |Salida                                  |
|-----------------------------|----------------------------------------|
|z,z,Z,Z,i,a,z,Z,A,A,z,a,z,A,A|Z I A Z A Z A Z A <br> 4 1 1 2 2 1 1 1 2|

> __**Nota**__: El enunciado original contiene errores ortográficos.

# Variante

Hugo, Paco y Luis siguen en el viaje por carretera con su tío Donaldo. Luis se
acaba de despertar y Hugo y Paco deciden empezar un nuevo juego para incluir a
Luis. Ahora van a contar el número de placas seguidas que tienen la primera letra
igual. Cada vez que pasan los vehículos anotan las placas y luego cuentan la
cantidad de cada una.

Realizar un programa que reciba una lista con las primers letras de las placas
vistas por Hugo (SEPARADAS POR UNA COMA CADA LETRA), Paco y Luis e imprima en una
fila las letras que fueron viendo, separadas por un espacio, y en otra fila las
veces seguidas que vieron dicha letra, separados por un espacio.

Ejemplo

|Entrada                        |Salida                                                |
|-------------------------------|------------------------------------------------------|
|A,A,a,c,g,c,B,A,F,f,b,f,E,b,f,b|A C G C B A F B F E B F B<br>3 1 1 1 1 1 2 1 1 1 1 1 1|

# Just Dance 2022

Just Dance es una franquicia de Ubisoft Forward para las personas que les gusta
bailar frente a una cámara y compartir con muchas personas por medio de stream,
convirtiéndose en tendencia a nivel mundial y pre cursos de plataformas como
tik tok. Por lo que deciden buscar ideas innovadoras para mantenerse en el mercado,
por lo que proceden a analizar danzas como zumba, reggae, etc.

La nueva propuesta consta de lo siguiente: En el juego se presentarán una serie de
pasos, uno a la vez, cada uno de los pasos estarán asociados a una letra distinta del
alfabeto; debido a que tendremos pasos de baile que serán muy similares, por lo que el
movimiento podrá ser representado por la letra del alfabeto en mayúsculas o minúsculas.
La idea es que la persona luego de ver la sucesión de pasos, determine cúales fueron
los pasos presentados y cuantas veces fueron realizados de manera consecutiva un mismo
paso.

Un ejemplo de una canción donde se presenta una secuencia de pasos,es la coreografía de
Axé de la canción Onda Onda, que inicia con la secuencia E,E,e,E,E,d,E,E,D,c,C. En este
caso, los pasos inferidos serán E (con cinco repeticiones), D (con una repetición),
E (con dos repeticiones), D (con una repetición), y C (con dos repeticiones).

Como usted trabaja para la compañia como desarrollador, decide construir un programa que
pueda ayudar al bot del juego a comparar los resultados que brinda el jugador, brindando
movimientos tanto en minúsculas como en mayúsculas, cada uno separado por comas. La
salida contendrá en la primera línea la secuencia de pasos, representados por mayúsculas.

La salida debe ser en primera instancia la sucesión de pasos, representadas en
mayúsculas, sin tener en cuenta los pasos repetidos, y debajo de cada letra, la
cantidad de veces que presento el paso de manera consecutiva.

## Entrada

La entrada consta de una sucesión de caracteres separados por coma que corresponden a
los pasos determinados por el jugador.

## Salida

La salida consta de dos líneas: la primera es la sucesión de pasos sin repeticiones,
en mayúsculas y separadas por espacio; la segunda es la cantidad de veces que se
repitió cada paso de manera consecutiva, separado también por espacio.

|Entrada                                            |Salida                                                                    |
|---------------------------------------------------|--------------------------------------------------------------------------|
|E,E,e,E,E,d,E,E,D,c,C,E,E,B,E,E,a,E,A,E,g,E,G,E,f,E|E D E D C E B E A E A E G E G E F E<br>5 1 2 1 2 2 1 2 1 1 1 1 1 1 1 1 1 1|