# Enunciado Original

## Programación de Entregas de Multiples Medicamentos a Pacientes con Enfermedades no Transmisibles

En el año 2015, los líderes mundiales adoptaron un conjunto de objetivos globales
para erradicar la pobreza, proteger el planeta y asegurar la prosperidad para todos
como parte de una nueva agenda de desarrollo sostenible. Uno de estos objetivos es
el de salud y bienestar y una de sus metas busca reducir en un tercio la mortalidad
prematura por enfermedades no transmisibles mediante la prevención y el tratamiento.

Debido a esto, el ministerio de salud desea que usted construya un sistema para la
programar la entrega de existencias de un tipo de medicamento en varias sucursales
de una IPS para el tratamiento y prevención de la hipotensión y la hipertensión, en
pos del mejoramiento de la calidad de vida de los ciaudadanos.

Para ello, el sistema debe leer la información del archivo **data.csv**, que contiene
los siguientes campos/columnas:
- **first_name**: El primer nombre del paciente.
- **last_name**: El primer apellido del paciente.
- **gender**: El género del paciente ("**m**" para hombres o "**f**" para mujeres).
- **city_name**: El nombre de la ciudad donde se encuentra la sucursal.
- **department_name**: El nombre del departamento donde se encuentra la sucursal.
- **id_branch**: El número identificador de la sucursal (entre **1** y **32**).
- **medicine_type**: El tipo de medicamento que la persona está solicitando (entre **1** y **20**).
- **medicine_quantity**: Cantidad de existencias que el paciente está solicitando.
- **systolic_pressure**: El valor de la presión sistólica del paciente.
- **diastolic_pressure**: El valor de la presión diastólica del paciente.

Una sucursal solo se encuentra en una única ciudad y en un único departamento.

Los rangos de valores de presión, así como su categoría y si se programa o no la entrega
de existencias se listan en la siguiente tabla:

|Presión Sistólica|Presión Diastólica| Categoría                   |¿Se programa la entrega?|
|-----------------|------------------|-----------------------------|------------------------|
| < 91            | < 63             | Hipotension                 |          Sí            |
| [91 - 134)      | [63 - 77)        | Ideal                       |          No            |
| [134 - 162)     | [77 - 105)       | Normal                      |          No            |
| [162 - 188)     | [105 - 119)      | Normal-alta                 |          Sí            |
| [188 - 201)     | [119 - 126)      | HTA Grado 1                 |          Sí            |
| [201 - 214)     | [126 - 146)      | HTA Grado 2                 |          Sí            |
| >= 214          | >= 146           | HTA Grado 3                 |          Sí            |
| >= 152          | < 77             | Hipertension Solo Sistolica |          Sí            |

Adicionalmente, se debe recibir como entrada varios números identificadores de distintas
sucursales.

El programa debe mostrar por pantalla para cada una de las sucursales leídas previamente,
en orden ascendente, la siguiente información haciendo uso de los datos del archivo
**data.csv**:
- El número identificador de la sucursal, el nombre de la ciudad y el nombre del
  departamento donde se encuentra la sucursal.
- La cadena "scheduled patients"
- La cadena "male", seguido de la cantidad de hombres a los que se les programa la
  entrega de medicamentos en esa sucursal.
- La cadena "female", seguido de la cantidad de mujeres a las que se les programa
  la entrega de medicamentos en esa sucursal.
- La cadena "scheduled medicine quantity".
- La cadena "mean", seguido de la media (promedio) de la cantidad de medicamentos
  programados para entrega, independientemente del tipo, en esa sucursal, formateado
  a 2 cifras decimales.
- La cadena "total", seguida del total de medicamentos programados para entrega,
  independientemente del tipo.

### Ejemplo 1

|Entrada Esperada|
|----------------|
|1               |

| Salida Esperada                                                                                                                                |
|------------------------------------------------------------------------------------------------------------------------------------------------|
|1 Leticia Amazonas<br>scheduled patients<br>male 1089<br>female 1090<br>total 2179<br>scheduled medicien quantity<br>mean 150.45<br>total 327837|

### Ejemplo 2

|Entrada Esperada|
|----------------|
|3               |

| Salida Esperada                                                                                                                             |
|---------------------------------------------------------------------------------------------------------------------------------------------|
|3 Arauca Arauca<br>scheduled patients<br>male 1084<br>female 1106<br>total 2190<br>scheduled medicien quantity<br>mean 151.35<br>total 331450|

### Ejemplo 3

|Entrada Esperada|
|----------------|
|5               |

| Salida Esperada                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------------------------------------|
|5 Cartegena Bolivar<br>scheduled patients<br>male 1052<br>female 1122<br>total 2174<br>scheduled medicien quantity<br>mean 149.23<br>total 324436|

### Ejemplo 4

|Entrada Esperada| 
|----------------|
|10              |

| Salida Esperada                                                                                                                              |
|----------------------------------------------------------------------------------------------------------------------------------------------|
|10 Popayan Cauca<br>scheduled patients<br>male 1152<br>female 1073<br>total 2225<br>scheduled medicien quantity<br>mean 150.09<br>total 333956|

### Ejemplo 5

|Entrada Esperada|
|----------------|
|23              |

| Salida Esperada                                                                                                                               |
|-----------------------------------------------------------------------------------------------------------------------------------------------|
|23 Mocoa Putumayo<br>scheduled patients<br>male 1108<br>female 1089<br>total 2197<br>scheduled medicien quantity<br>mean 146.27<br>total 321346|

**Nota**: Por favor **NO** incluya mensajes en los inputs.

**Nota**: Las tildes y cualquier otro signo ortográfico han sido omitidos a propósito
en las entradas y salidas del programa. **Por favor NO use ningún signo dentro del
desarrollo de su solución** ya que estos pueden representar errores en la calificación
automática de Codegrade.

**Nota**: El archivo debe llamar **reto5.py**, de lo contrario no podrá ser cargado
en la plataforma de Codegrade.

**Nota**: El archivo **data.csv** debe encontrarse en la misma carpeta donde se encuentra
el archivo **reto5.py** y debe leerse usando la **ruta relativa** del mismo.

> __**NOTE**__: Se opta por nombrar el archivo como "main.py".
