# Enunciado Original

## Título: Aplicación de gestión de inventarios

Una tienda vende diferente productos, usualmente frutas, dulces y algunos tipos
de carne. Con el propósito de mejorar el control sobre las ventas y el inventario
de la tienda, el gerente decide construir una aplicación que le permita almacenar
la información de los productos y realizar cálculos sobre los datos.

En la primera parte del reto se debe construir una base de datos que almacene la
información de los productos disponibles en la tienda. La base de datos será
representada mediante un diccionario en Python llamdo productos que tendrá por
llave el código del producto y por valor una lista formada por los atributos:
nombre, precio e inventario. La tabla 1 presenta los productos disponibles a la
fecha.

|código|nombre    |precio  |inventario|
|------|----------|--------|----------|
|    1 |Manzanas  | 5000.0 |       25 | 
|    2 |Limones   | 2300.0 |       15 | 
|    3 |Peras     | 2700.0 |       33 | 
|    4 |Arandanos | 9300.0 |        5 | 
|    5 |Tomates   | 2100.0 |       42 | 
|    6 |Fresas    | 4100.0 |        3 | 
|    7 |Helado    | 4500.0 |       41 | 
|    8 |Galletas  |  500.0 |        8 | 
|    9 |Chocolates| 3500.0 |       80 |
|   10 |Jamon     |15000.0 |       10 |

## Tabla 1: Productos disponibles en la tienda

Es necesario construir 3 funciones que representen las operaciones de: AGREGAR,
ACTUALIZAR y BORRAR los productos disponibles. Se debe implementar una función
independiente por cada una de las acciones mencionadas. En este caso, para poder
realizar las operaciones de ACTUALIZAR o BORRAR es necesario especificar todos
los atributos del producto.

Adicionalmente se está interesado en analizar los datos de los productos disponibles
y conocer: el nombre del producto con el precio mayor; el nombre del producto con
el precio menor; el promedio de precios de todos los productos y el valor total del
inventario a la fecha. Este último se obtiene multiplicando el precio de cada producto
por el inventario disponible y luego sumando todos los resultados. Por ejemplo, al
calcular estos 4 valores para los datos disponibles en la Tabla 1 obtendríamos:

Producto precio mayor: Jamon
Producto precio menor: Galletas
Promedio de precios: 4900.0
Valor del inventario: 101410.0

### Entrada

Cada uno de los casos de prueba estará compuesto por dos líneas.
La primera línea estará formada por una cadena de texto que identifica la operación
a realizar. En este caso, las operaciones válidas son:
- ACTUALIZAR
- BORRAR
- AGREGEGAR

La segunda línea estará formada por 4 valores (código, nombre, precio, inventario) que
representan el producto sobre el cual se quiere realizar la operación.
En el caso de la operación ACTUALIZAR la segunda línea debe contener el código y los
nuevos valores del producto.
En el caso de la operación BORRAR se deben especificar todos los atributos del producto
a eliminar.

### Salida

La salida estará representada por una única línea formada por cuatro valores:
- Nombre del producto con el precio mayor
- Nombre del producto con el precio menor
- Promedio de precios
- Valor del inventario

Estos 4 valores deben imprimirse después de realizar las operaciones solicitadas en la
entrada de datos.
Los valores númericos deben imprimirse con un número decimal.
En caso de solicitar ACTUALIZAR o BORRAR un producto que no existe (es decir, que el
código del producto no se encuentra en la base de datos), se debe imprimir "ERROR".
En caso de solicitar AGREGAR un producto cuyo código ya existe en la base de datos
se debe imprimir "ERROR".

### Casos de prueba

| Entrada                       | Salida Esperada                  |
|-------------------------------|----------------------------------|
|AGREGAR<br>11 Melon 70 13      |Jamon Melon 4460.9 1015010.0      |
|BORRAR<br>10 Jamon 15000 10    |Arandanos Galletas 3777.8 864100.0|
|ACTUALIZAR<br>7 Helado 65000 11|Helado Galletas 10950.0 1544600.0 |
|BORRAR<br>14 Maiz 45000 12     |ERROR                             |

### Dificultad

#### Instruciones
##### Instrucciones para la calificación automática

Cada caso de prueba se especifica con dos líneas.
Cada línea debe contener los valores de los parámetros requeridos separados por un 
espacio.
Es importante no utilizar ningún mensaje a la hora de capturar las entradas, es decir,
al utilizar la función input() no agregue ningún texto para capturar los datos.
Los resultados se muestran en una única línea. Los dos valores requeridos deben estar
separados por un espacio.
