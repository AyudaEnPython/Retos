# 16208. [Las camisas de Jorgensen](https://omegaup.com/arena/problem/Las-camisas-de-Jorgensen/)

<table style="margin-left: auto; margin-right: auto;">
<tbody>
  <tr>
    <td>Puntos</td>
    <td>100</td>
    <td>Limite de memoria</td>
    <td>32 MiB</td>
  </tr>
  <tr>
    <td>Límite de tiempo (caso)</td>
    <td>1s</td>
    <td>Límite de tiempo (total)</td>
    <td>1m0s</td>
  </tr>
  <tr>
    <td>Tamaño límite de entrada (bytes)</td>
    <td>3906.25 KiB</td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

## Descripción

Jorgensen IBM desea incursionar en el mercado de las camisas. Para abaratar
costos y maximizar los beneficios, ha subcontratado una maquilaen algún lugar
del sudeste asiático. En dicha maquila manufacturalos lotes de sus camisas y
en México únicamente les pone un sello; para posteriormente vender sus productos
a los comerciantes.

Jorgensen desea vender dicha camisas en los Estados Unidos de Norteamérica (USA),
pero ha habido un mal entendido al momento de realizar los pedidos.

Cada lote de camisas tiene 12 camisas en su interior y los lotes están etiquetados
según su talla. Las etiquetas de los lotes vienen según el estándar mexicano, no
el estadounidense. Para exportar su producto, Jorgensen deberá declarar la cantidad
de paquetes siguiendo el estándar estadounidense. Las equivalencias de dichos
valores son los siguientes:

|Talla USA|Talla México|
|---------|------------|
| XS      | 32         |
| S       | 36         |
| M       | 38         |
| L       | 40         |
| XL      | 42         |

Deberás ayudar a Jorgensen a contabilizar sus lotes según el estándar de tallas de
Estados Unidos.

## Entrada

Un entero $N$ seguido de las $N$ etiquetas de los lotes de camisas en el
formato de tallas de México.

## Salida

Cada una de las tallas en el formato USA, seguidas de la cantidad de lotes que
corresponden en esa talla y el total de camisas de ese tipo.

Si no hay lotes de una talla en específico, se marcará la cantidad de lotes como
0 y el total de camisas como 0.

## Ejemplo

| Entrada              | Salida | Descripción |
|----------------------|--------|-------------|
|6<br>38 32 36 38 40 42|XS:1:12<br>S:1:12<br>M:2:24<br>L:1:12<br>XL:1:12|Caso donde hay, por lo menos, un lote de cada talla|
|3<br>38 32 36|XS:1:12<br>S:1:12<br>M:1:12<br>L:0:0<br>XL:0:0|Caso donde no hay lotes de una o más tallas|

## Límites

$1 \le N \le 1000$

---


`main.py`
```python
#!/usr/bin/python3

def _main() -> None:
    # TODO: fixme.
    pass

if __name__ == '__main__':
    _main()
```