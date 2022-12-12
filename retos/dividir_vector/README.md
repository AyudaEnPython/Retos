# Enunciado Original

## Descripción

Dado un vector $a$ el cual consta de $n$ elementos, se le dará un número $k$
($n$ será divisible por $k$).

Debes dividir el vector $a$ en $n/k$ segmentos y rotar una sola vez a la izquierda
los elementos del vector $a$ en cada segmento (cada segmento contendrá $k$ elementos)
como muestra el ejemplo:

Dada el vector $a$, con $k = 5$:
<table>
  <tr>
    <td> 5</td>
    <td>-8</td>
    <td> 9</td>
    <td>12</td>
    <td> 0</td>
    <td> 4</td>
    <td>-1</td>
    <td>25</td>
    <td>3</td>
    <td>10</td>
    <td> 6</td>
    <td> 2</td>
    <td>15</td>
    <td> 7</td>
    <td>11</td>
    <td> 5</td>
    <td>26</td>
    <td>31</td>
    <td> 0</td>
    <td> 4</td>
  </tr>
</table>

Despues de rotar a la izquierda cada segmento del vector:
<table>
  <tr>
    <td>-8</td>
    <td> 9</td>
    <td>12</td>
    <td> 0</td>
    <td> 5</td>
    <td>-1</td>
    <td>25</td>
    <td>3</td>
    <td>10</td>
    <td> 4</td>
    <td> 2</td>
    <td>15</td>
    <td> 7</td>
    <td>11</td>
    <td> 6</td>
    <td>26</td>
    <td>31</td>
    <td> 0</td>
    <td> 4</td>
    <td> 5</td>
  </tr>
</table>

## Entrada

La primera línea de entrada consta de dos números enteros $n$
($1 \le n \le 1000$) y $k$ ($1 \le k \le n$), se garantiza que
$n$ siempre será divisible por $k$, es decir: $n \% k = 0$.

La segunda línea consta de $n$ enteros $a_0 \ a_1 \ a_2 \ ... a_{n-1}$
$(1 \le a_i \le 100000)$ los cuales son los elementos del vector,
en la entrada de datos cada par de elementos adyacentes estarán
separados por un espacio.

## Salida

Imprima el vector despues de rotar a la izquierda cada segmento del
vector, cada par de elementos debe estar separados por un espacio.

## Ejemplo de entrada y salida

| Entrada                                                |
|--------------------------------------------------------|
|20 5<br>5 -8 9 12 0 4 -1 25 3 10 6 2 15 7 11 5 26 31 0 4|

| Salida                                         |
|------------------------------------------------|
|-8 9 12 0 5 -1 25 3 10 4 2 15 7 11 6 26 31 0 4 5|