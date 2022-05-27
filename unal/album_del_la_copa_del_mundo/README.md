# Enunciado Original

## Album de la copa del mundo

Continuando con la fiebre del mundial, nosotros hemos decidio crear un programa
en python que nos ayude a optimizar el proceso de llenado de album por lo cual
crearemos un modulo llamado "album" con un conjunto de funciones.

**1. La función `"tipolamina"`** que dada una lista de tipos de laminas (en la 
posición i-ésima de la lista está el tipo de la lamina), genera una lista con
los tipos unicos de laminas.

Por ejemplo data la siguiente lista con los siguientes tipos:

**`tipolamina`**(['escudo','equipo','entrenador','entrenador','equipo','jugador',jugador',jugador','escudo'])

la función debe retornar la lista
['escudo','equipo','entrenador',jugador]

Nótese que las clases aparecen solo una vez y en el orden como fueron apareciendo.

**2. La función `"mefaltalamina"`** que dada una lista con los números de las laminas
que me faltan y la lista de los tipos de cada lamina y un tipo de lamina se debe
retorne una lista con los números de las laminas que concuerdan con el tipo de lamina.

Por ejemplo si se ejecuta la función:

**`mefaltalamina`**([3,6,8],
['equipo','jugador','escudo','jugador','escudo','entrenador','equipo','jugador'],'jugador'])

debe retornar la lista

[3,8]

Nótese que los números que lo indices de las listas comienzan en cero

Por ejemplo si ejecutan la

función:

**`mefaltalamina`**([1,3,6,8],
['entrenador','escudo','jugador','jugador','jugador','equipo','escudo','entrenador','jugador','jugador'],'escudo'])

Se debe retornar la lista:

[1,6]

**3. La función `"notengo"`** que dada una lista con las figuritas que tiene otra persona
y una lista con las figuritas que tengo retorna la lista con las figuritas que me interesan
de la otra persona.

Por ejemplo si se llama:

**`notengo`**([3,5,7,10,15,16],[4,10,5,8])

Se debe retornar la lista:

[3,7,15,16]

**4. La función `"puedocambiar"`** que dada dos listas de figuras se diga el numero de figuras
que se estan interesadas en intercambiar, el numero de figuras interesadas en cambiar es el
minimo de la diferencia entre las dos listas

Por ejemplo, llamar la función:

**`puedocambiar`**([3,5,7,10,15,16],[4,10,5,8])

Debe retornar

2

Porque a la otra persona solo le interesan dos figuras que tiene ellos: [4,8], mientras que a
ellos les interesan cuatro figuras que la otra persona tiene: [3,7,15,16]

**Entrada:**

Este programa no requiere entrada. Ni generará salida. Se requiere que el estudiante genere
un archivo con el nombre **album.py** y que se respeten los nombres de las funciones dadas y
sus parámetros.

> __**NOTA**__: El enunciado original presenta demasiados errores ortográficos.

---

# Enunciado Modificado

## Album de la copa del mundo

Continuando con la fiebre del mundial, nosotros hemos decidio crear un programa
en Python que nos ayude a optimizar el proceso de llenado de album por lo cual
crearemos un modulo llamado `album.py` con un conjunto de funciones.

### La función `tipo_lamina`

Dada una lista de los tipos de lámina genera una lista con los tipos únicos de las
láminas.

Por ejemplo, dada la siguiente lista de laminas:
```python
tipo_lamina([
    "escudo",
    "equipo",
    "entrenador",
    "entrenador",
    "equipo",
    "jugador",
    "jugador",
    "jugador",
    "escudo",
])
```
La función debe retornar la lista:
```python
["escudo", "equipo", "entrenador", "jugador"]
```
> Nótese que los tipos de láminas aparecen solo una vez y en el orden como
> fueron apareciendo.

### La función `me_falta_lamina`

Dada una lista con los números de las láminas que me faltan, la lista de los tipos
de cada lámina y un tipo de lámina; se debe retornar una lista con los números de
las láminas que concuerden con el tipo de lámina.

Por ejemplo, si se ejecuta la función:
```python
me_falta_lamina(
    [3, 6, 8],
    [
        "equipo",
        "jugador",
        "escudo",
        "jugador",
        "escudo",
        "escudo",
        "entrenador",
        "equipo",
        "jugador",
    ],
    "jugador",
)
```
Debe retornar la lista:
```python
[3, 8]
```

> Nótese que los números de los índices comienzan en cero

Por ejemplo, si se ejecuta la función:
```python
me_falta_lamina(
    [1, 3, 6, 8],
    [
        "entrenador",
        "escudo",
        "jugador",
        "jugador",
        "jugador",
        "equipo",
        "escudo",
        "entrenador",
        "jugador",
        "jugador",
    ],
    "escudo",
)
```
Se debe retorna la lista:
```python
[1, 6]
```

### La función `no_tengo`

Dada una lista con las figuras que tiene otra persona y una lista con las figuras
que tengo, retornar la lista con las figuras que me intersan de la otra persona.

Por ejemplo, si se llama:
```python
no_tengo([3, 5, 7, 10, 15, 16], [4, 10, 5, 8])
```
Se debe retornar la lista:
```python
[3, 5, 7, 15, 16]
```

### La función `puedo_cambiar`

Dada dos listas de figuras retorne el número de figuras que estan interesadas en
cambiar (mínimo de la diferencia entre ambas).

Por ejemplo, llamar la función:
```python
puedo_cambiar([3, 5, 7, 10, 15, 16], [4, 10, 5, 8])
```
Debe retornar:
```python
2
```
> Mientras a una persona solo le interesan dos figuras: `[4, 8]`, la otra le interesa:
> `[3, 7, 15, 16]`

## Entrada y Salida

Este programa no requiere entrada ni generará salida. Se requiere que el estudiante genere
un archivo con el nombre `album.py` y qu se respeten los nombres de las funciones dadas y
sus parámetros.
