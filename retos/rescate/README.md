# Rescate

Un audaz equipo de rescate tiene la gran misión de rescatar a un grupo
de exploradores que intentaban llegar al polo sur por el territorio
antártico chileno. Para ello, deben alcanzar la península O'Higgins
navegando a través del peligroso paso Drake, que en esta época del año
está plagada de grandes témpanos flotantes de hielo, zarpando desde
Puerto Williams.

Debido a extrañas condiciones climáticas, el boto puede navegar por
tres días consecutivos, avanzando a millas naúticas, pero luego debe
apagar máquinas y realizar reparaciones durante un día. En ese lapso,
las corrientes marinas alejan al barco de rescate b millas naúticas
del punto de destino.

Considere que el punto de destino se encuentra a c millas naúticas de
Puerto Williams.

- Asuma que la cantidad de días se redondea al entero mayor.
- Lea un archivo de texto, "entrada.txt", que en cada línea tiene
  tres valores enteros no negativos separados por un espacio, donde
  cada uno corresponde a los parámetros a, b, y c, respectivamente.
  Luego, use ambas funciones para calcular el tiempo de navegación y
  genere el archivo de texto "salida.txt", el cual debe contener los
  siguientes valores separados por un espacio: a, b, y c, la cantidad
  de días que tarda el barco en llegar, y el tiempo que tarda tanto la
  función en obtener la respuesta (tiempo de ejecución) para cada
  combinación de los parámetros a, b, y c.

##  Ejemplo

    Entrada.txt
    -----------
    200 67 15000
    198 70 50704
    30 40 60

    Salida.txt
    ----------
    200 67 15000 451 0.00002
    198 70 50704 1583 0.099
    30 40 60 -1 0 0

- Ordene los tiempos de ejecución de cada función en orden creciente
  y **construya un gráfico de líneas** que muestre dichos tiempos.
  Considere que las líneas para cada función deben tener colores y
  texturas diferentes y que el gráfico debe contar con un título,
  leyenda, y ejes debidamente rotulados. Tenga en cuenta que su
  solución debe funcionar para cualquier archivo de entrada válido,
  no solo para el ejemplo, independientemente de la cantidad de filas
  que este tenga.

**Construya un programa que:**

- Contenga al menos una función, que calcule cuántos días tarda el
  barco en alcanzar la península O'Higgins (si es que lo logra). En
  caso de no lograrlo considere que debe retornar el valor -1.
