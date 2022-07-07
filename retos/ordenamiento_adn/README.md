# Enunciado Original

## Ordenamiento de ADN

Una medida del "desorden" de una secuencia se define como la cantidad de pares
de sus entradas que están fuera de un orden establecido con respecto a los otros.
Tomemos como ejemplo la secuencia de letras "DAABEC", en la cual la medida de
desorden respecto a un ordenamiento alfabético es 5 debido a que la letra "D" es
más grande que 4 de las letras que están a su derecha y la letra "E" es sólo mayor
que la letra "C". La medida de desorden también puede ser interpretada como el
número de inversiones necesarias para dejar en orden la secuencia y para ejemplificar
esta interpretación consideremos la secuencia "AACEDGG", la cual está casi ordenada
pues tiene sólo una inversión (las letras "E" y "D") mientras que la secuencia
"ZWQM" tiene 6 inversiones (está exactamente en el orden inverso).

En el laboratorio de Biotecnología de la Universidad de Concepción se requiere
catalogar secuencias de ADN (Ácido Desoxirríbonucleico), las cuales están formadas por
4 letras "A", "C", "G" y "T", listándolas desde la más ordenada a la más desordenada
usando la medida de desorden. Las cadenas tienen distintas longitudes y cuando entre
dos o más cadenas la medida de desorden sea la misma éstas se deben ordenar de la más
larga a la de menor longitud. Aunque la longitud de las cadenas es variable, habrá
un valor de longitud mínimo y un valor máximo. Finalmente, si persiste el empate
usando los dos criterios anteriores, se tendrá que usar el orden alfabético como
tercer y último criterio.

## Entradas

Las entradas a este programa vendrán en un archivo de texto llamado "ADN.dat" con la
siguiente estructura:

En la primera línea vendrá la cantidad de casos de prueba siendo este valor mayor
que cero y menor que 50.

En una segunda línea vienen dos números enteros (cuyos valores deben estar entre 5 y
50) que establecen la longitud mínima y la longitud máxima que puede tener una cadena.
El primer valor debe ser menor o a lo sumo igual a el segundo. Si los valores son
erróneos el programa debe indicarlo y terminar.

La tercera línea contiene la cantidad `q` de cadenas de ADN que se deben procesar, el
cual es un número entero mayor que cero y menor que 50. Si el valor está fuera de rango
el programa debe indicar el error y terminar.

Luego habrá líneas `q` líneas, cada una conteniendo una cadena de ADN. Si alguna de las
cadenas tiene una longitud fuera de rango o si en la secuencia hay una letra distinta
de "A", "C", "G" o "T", el programa debe indicar el error y terminar.

## Salidas

La salida del programa es la lista con los `n` casos de prueba mostrando en cada uno
las `q` cadenas de entrada respectivas pero ordenadas de acuerdo a los criterios
establecidos en el enunciado.

## Ejemplo de entrada:

    1
    8 10
    6
    AACATGAAGG
    TTTTGGCCAA
    TTTGGCCAAA
    GATCAGATTT
    CCCGGGGGGA
    ATCGATGCAT

## Ejemplo de salida

    CCCGGGGGGA
    AACATGAAGG
    GATCAGATTT
    ATCGATGCAT
    TTTTGGCCAA
    TTTGGCCAAA
