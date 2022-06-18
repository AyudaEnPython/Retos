# Enunciado Original

## Descripción

Valeria tiene mucha hambre. Coge una cena que compro del supermercado, la mete
en el microondas y registra en el microoondas 02 : 15 para cocinarla en 2 minutos
y 15 segundos. Valeria desconoce que el microondas toma estos valores como horas
y minutos, es decir, el microondas toma 02 : 15 como 2 horas y 15 minutos (no 2
minutos y 15 segundos).
Necesitamos indicarle a Valeria cuánto tiempo extra (es decir, tiempo adicional)
tendrá que esperar hasta que se termine de cocinar su cena. Es decir, debemos
decirle a Valeria que su comida estará lista en 2 horas, 12 minutos y 45 segundos
más de lo que ella esperaba.

### El problema:
Dado el tiempo inicial en la forma de _MM : SS_, donde la entrada se toma realmente
como _HH : MM_, determine cuánto tiempo más estará su comida en el microondas.
Proporcione esta información en forma de _HH : MM : SS_.

## Entrada

La primera línea de la entrada contiene un número entero _t_ (1 <= _t_ <= 100): el
número de casos de prueba.

Cada caso de prueba constará de una sola línea en forma de _MM : SS_, que
representa los valores que ingreso Valeria. _MM_ y _SS_ estarán en el rango de
00 y 59 (inclusive), pero ambos no serán 00 al mismo tiempo, es decir, el tiempo
total será positivo, es decir, que la entrada no será 00 : 00.

## Salida

Por cada caso de prueba: La salida debe contener una sola línea de _HH : MM : SS_,
que indica el tiempo adicional de cocimiento de los alimentos en el microondas.
Tenga en cuenta que debe imprimir dos dígitos para cada parte.
También tenga en cuenta que _MM_ y _SS_ deben estar en el rango de 00 a 59.

### Ejemplo

| Entrada                    | Salida                         |
|----------------------------|--------------------------------|
|3<br>05:00<br>13:37<br>00:10|04:55:00<br>13:23:23<br>00:09:50|
