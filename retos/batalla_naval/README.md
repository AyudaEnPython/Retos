# Enunciado Original

Tienes que inicializar una matriz de 9x9 con todos los caracteres con
la letra `A` que simulan el Agua del juego Batalla Naval.

A continuación el usuario va a ingresar dos veces los siguientes datos:

- Posición fila inicio.
- Posición columna inicio.
- Tamaño de la ficha.
- Orientación de la ficha (0: vertical, 1: horizontal).

Con los datos debe colocar las fichas en el tablero reemplazando la letra
`A` por la letra `B` que simula un Barco en el juego.

Luego de esto tu programa debe imprimir el tablero de juego.

Finalmente, el usuario va a ingresar 2 valores más:

- Posición tiro en fila.
- Posición tiro en columna.

Con los datos debe indicar si el tiro al Agua, reemplazando la letra `A` por
`O`, o si dio en el Barco, reemplazando la letra `B` por `X`.

Luego de esto tu programa debe imprimir el tablero de juego.

**Importante**: Para imprimir la matriz tiene que usar el siguiente formato
en cada celda: "" + letra + "". Por ejemplo "A" o "B".

## Entrada de muestra 0

```
2
3
5
0

8
2
3
1

7
3
```

## Salida de muestra 0

```
AAAAAAAAA
AAAAAAAAA
AAABAAAAA
AAABAAAAA
AAABAAAAA
AAABAAAAA
AAABAAAAA
AAAAAAAAA
AABBBAAAA
```

## Entrada de muestra 1

```
2
3
5
0

8
2
3
1

8
4
```

## Salida de muestra 1

```
AAAAAAAAA
AAAAAAAAA
AAABAAAAA
AAABAAAAA
AAABAAAAA
AAABAAAAA
AAABAAAAA
AAAAAAAAA
AABBXAAAA
```

> __**NOTA**__: Se opta por cambiar el caracter para representar
> el mar (`A` -> `~`)