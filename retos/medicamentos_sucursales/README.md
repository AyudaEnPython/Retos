# Enunciado Original

## Programación de Entregas de Medicamentos a Pacientes con Enfermedades no Transmisibles

En el año 2015, los líderes mundiales adoptaron un conjunto de objetivos globales
para erradicar la pobreza, proteger el planeta y asegurar la prosperidad para todos
como parte de una nueva agenda de desarrollo sostenible. Uno de estos objetivos es
el de salud y bienestar y una de sus metas busca reducir en un tercio la mortalidad
prematura por enfermedades no transmisibles mediante la prevención y el tratamiento.

Debido a esto, el ministerio de salud desea que usted construya un sistema para la
programar la entrega de existencias de un tipo de medicamento en varias sucursales
de una IPS para el tratamiento de vida de los ciudadanos.

Para ello, el sistema debe recibir como entrada la cantidad de sucursales (n) para la
entrega de medicamentos seguido de la cantidad total de pacientes a atender (m), si la
cantidad de sucursales es menor a 1 se debe leer nuevamente ambos valores hasta que se
ingrese un n válido. Luego, para las n sucursales (numeradas de 1 a n) se debe leer la
cantidad de existencias actuales del medicamento y esta debe ser mayor o igual a 1, y
en caso de que no se cumpla se debe leer valores hasta que se ingrese uno válido.
Finalmente, para los m pacientes se debe leer el número de la sucursal donde será
atendido, seguido de información de las presiones sistólica y diastólica del mismo.

Los rangos de valores de presión, así como su categoría y la cantidad y tipo de
medicamento entregado se listan en la siguiente tabla:

|Presión Sistólica|Presión Diastólica| Categoría             |Tipo de Medicamento|Número de Dosis|
|-----------------|------------------|-----------------------|-------------------|---------------|
| < 90            | < 70             | Hipotension           |         1         |       15      |
| [90 - 130)      | [70 - 90)        | Optima                |      Ninguno      |       0       |
| [130 - 140)     | [90 - 95)        | Normal                |      Ninguno      |       0       |
| [140 - 150)     | [95 - 100)       | Normal-alta           |         1         |       10      |
| [150 - 170)     | [100 - 110)      | HTA Grado 1           |         1         |       10      |
| [170 - 190)     | [110 - 120)      | HTA Grado 2           |         1         |       20      |
| >= 190          | >= 120           | HTA Grado 3           |         1         |       50      |
| >= 150          | < 100            | HTA Sistolica Aislada |         1         |       20      |

Si no se encuentra la categoría del paciente o la sucursal donde será atendido el
paciente no es válida, no se programa la entrega ninguna existencia del medicamento.

El programa debe mostrar por pantalla el número de la sucursal con la menor cantidad
de existencias, luego de realizar la entrega de las mismas, seguido de la cantidad antes
mencionada. Luego, en una nueva línea se debe mostrar el número de la sucursal con la
mayor cantidad de existencias, luego de realizar la entrega de las mismas, seguido de la
cantidad antes mencionada. Finalmente, para cada una de las sucursales (en orden ascendente
por número y en líneas distintas) se debe mostrar su número seguido de la proporción
porcentual de las existencias del medicamento programadas para entrega respecto a la
cantidad de existencias actuales del medicamento en la sucursal correspondiente, formateado
a 2 cifras decimales y separado por espacio.
Si hay más de una sucursal con iguales cantidades mínimas o máximas, se debe mostrar la
que tenga menor número.

### Ejemplo 1

| Entrada Esperada                                                                   |
|------------------------------------------------------------------------------------|
|3 5<br>137<br>233<br>904<br>1 148 96<br>2 105 88<br>3 148 95<br>2 118 84<br>2 134 90|

| Salida Esperada                               |
|-----------------------------------------------|
|1 127<br>3 894<br>1 7.30%<br>2 0.00%<br>3 1.11%|

### Ejemplo 2

| Entrada Esperada                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------|
|5 8<br>552<br>561<br>993<br>308<br>249<br>4 164 104<br>4 156 106<br>4 84 34<br>3 187 113<br>5 156 107<br>5 200 155<br>1 141 97<br>4 167 105|

| Salida Esperada                                                       |
|-----------------------------------------------------------------------|
|5 189<br>3 973<br>1 1.81%<br>2 0.00%<br>3 2.01%<br>4 14.61%<br>5 24.10%|


### Tests

Entrada 1.1

4 6 
530 
457 
491 
470 
3 165 38
3 173 121
1 137 99
2 145 106
1 167 120
1 130 119

Entrada 1.2
2 3
529
441
2 68 90
1 193 65
1 195 92

Entrada 1.3
3 4
450
173
427
3 127 147
3 84 77
3 174 47
2 172 105

Entrada 1.4
2 6
406
210
1 162 76
1 151 91
1 180 134
2 219 128
2 136 91
1 175 99

Entrada 1.5
3 6
400
252
248
3 138 61
2 138 108
1 106 114
2 165 91
1 164 45
1 199 101