# Enunciado Original

Usted ha sido contratado por un prestigioso magnate, el cual trabaja con
criptomonedas realizando trading (negociación o compra y venta de activos),
minería (utilizar la potencia informática (hash), para procesar transacciones
y obtener recompensas) y staking (dejar bloqueadas en depósito criptomonedas
para recibir recompensas).

Debido a la naturaleza cambiante de los criptoactivos los precios de cada
moneda varia a diario y su equivalencia en dólares se ve afectada por distintos
sucesos que se presentan en el día a día, como son conflictos bélicos,
elecciones de gobernantes o adopción de políticas económicas por diferentes
países.

Teniendo en cuenta lo anterior el magnate posee inversiones en diferentes
criptomonedas, las cuales varían casi a diario por tanto el día de hoy puede
tener en su billetera digital (1 Bitcoin, 1 Solana y 1 Ethereum) y el día
siguiente (1 Polka Dot, 1 Shiba Inu, 1 Terra Luna, 1 APE Coin). De la misma
forma, algunos precios son determinados por la plataforma Binance, la cual
genera un diccionario a diario con los valores que representa cada token que
posee el magnate representadas en dólares.

Su misión es crear un programa en Python que reciba un diccionario que contiene
las criptomonedas y su respectivo valor en dólares, adicionalmente reciba el
listado de criptomonedas manejadas por el magnate separado por espacios.

La salida se representara en dos líneas, donde la primera mostrara una cadena
de texto con las llaves de las criptomonedas encontradas en el diccionario
separadas por espacio y luego en una línea aparte la suma total en dólares que
posee el magnate

| Entrada                                                                                                | Salida                     |
|--------------------------------------------------------------------------------------------------------|----------------------------|
|{"SOL": 50, "BTC": 29000, "DOT": 0.2, "SHIBA": 0.03548 , "LUNA": 2, "APE": 35}<br>BTC SHIBA BNB APE BUSD|BTC SHIBA APE<br>29035,03548|