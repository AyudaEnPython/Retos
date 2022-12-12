# Enunciado Original

## Reto 3 - Fundamentos de Programación

Usted y un grupo de amigos ha decidio realizar una rifa de
1'000.000 de pesos para recaudar fondos en pro de los habitantes
de calle del municipio en el que usted habita.

La rifa se hará a través de un juego muy conocido, un "BINGO"; sin
embargo, ninguno de ustedes cuenta con una balotera.

Usted, como desarrollador en una compañia que se dedica a desarrollar
software para casinos y apuestas, se le ocurre diseñar un algoritmo
que genere las salidas de una balotera:

balotera(balotas)

La entrada de su función solución es una lista con las diferentes balotas,
es decir:

```python
balotas = [
    "B1", "B2", ..., "B15",
    "I16", "I17", ..., "I30",
    "N31", "N32", ..., "N45",
    "G45", "G47", ..., "G60",
    "O61", "062", ..., "O75",
]
```

Su algoritmo debe, en primer instancia resolver la lista `balotas` usando
la librería numpy o random, luego, después de haber revuelto las balotas,
devolver el mínimo de balotas que se necesitan para que la menos una tabla
gane (Suponiendo que todas las tablas juegan).

Las balotas revueltas se van sacando en el orden en el que van apareciendo
(De izquierda a derecha de la lista revuelta).

> __**NOTA**__: El enunciado original esta mal redactado.
