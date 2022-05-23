# Simulador de futbol

De un listado de trece ( 13 ) jugadores sacados del equipo ideal y representados
por los caracteres separados por coma ( . , + , T , | , X , - , * , Y , W , ! , @ , # , $)
se debe realizar un campeonato en el cual cada jugador debe seleccionar mínimo un (1) y
máximo seis (6) cobradores de tiro penal y a su vez elegir el mismo rango de jugadores
que serán porteros. La lista de jugadores seleccionados como cobradores no debe tener
jugadores repetidos como tampoco la de porteros, sin embargo se puede seleccionar un
jugador como cobrador y como portero sin ningún problema. Adicional se va a solicitar
el nombre del equipo que el usuario le quiera asignar al team.

Una vez Obtenida la lista seleccionada por parte de los usuarios, cada cobrador debe
empezar la tanda de penales cobrando a cada uno de los porteros seleccionados y para
determinar quien anoto un tanto en cada ejecución, se obtendrá el valor Unicode de
cada jugador y el que tenga mayor valor será el triunfador. Por tanto, si el código
Unicode del cobrador es mayor que el del portero se le asignara un gol  \u00D8  en
caso de que tengan igual valor se toma como empate (\u265E) y en caso de que su valor
sea menor se toma como atajada(\u00A5).
Finalmente, la consola deberá mostrar, primero el resultado final de cada disparo
representado por su respectivo carácter Unicode, en la segunda línea determinar si
el nombre del equipo es palíndromo o no mediante un mensaje que diga “ES PALINDROMO”
o “NO ES PALINDROMO” y en la última línea debe imprimirse un entero con la mayor
cantidad de goles anotados por un o unos jugadores en su respectiva tanda de anotación.

| Entradas                               | Salidas                                        |
|----------------------------------------|------------------------------------------------|
|*WXT+<br>-*Y.$<br>Ají traga la lagartija|¥♞¥¥ØØØ¥ØØØØ¥ØØØØ¥ØØ¥Ø¥¥Ø<br>ES PALINDROMO<br>4|

> __**NOTA**__: El enunciado esta mal redactado.
