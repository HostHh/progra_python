# -*- coding: utf-8 -*-
"""2s2023_22_viaje.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vcP66cKbSevnWqJim6IAsGL-5vxdzf9K

> Es indispensable tomar el curso **JUPYTER NOTEBOOK, GOOGLE COLAB Y MARKDOWN**. Temas **BIENVENIDA, MARKDOWN Y GOOGLE COLAB**.

|Datos|datatype|Origen|variables|Fórmula|
|---|---|---|---|---|
|Dinero|float|Se tiene|dinero|``=600.00``|
|Velocidad|float|Se tiene|v|``=50.00``|
|Precio gas|float|Se pregunta|precio (float), _precio (str)||
|Litros|float|Se calcula|litros|``=dinero/precio``|
|Rendimiento|float|Se pregunta|rendimiento (float), _rendimiento (str)||
|Distancia|float|Se calcula|d|``=rendimento*litros``|
|Tiempo|float|Se calcula|t|``=d/v``|
|Horas|float|Se calcula|hh|``=int(t)``|
|Minutos|float|Se calcula|mm|``=(t-hh)*60``|

# **Viaje**

Tienes $600 pesos, y un coche que que viaja a una velocidad constante de de 50km/hora y tiene el tanque sin gasolina.

¿Qué distancia recorrerás con ese dinero?
¿En cuánto tiempo recorrerás esa distancia?

La distancia tiene que estar expresada en kilómetros, y el tiempo en minutos y segundos.
"""

dinero=600.00

v=50.00

# El precio no debe omitirse.
# El precio debe ser un número.
# El precio debe ser mayor a cero.
# El programa no deja de preguntar el precio, sino hasta que
# está correcto.
# Me debe mostrar errores específicos (error, causa, acción).

while True:
    _precio=input("Dame el precio por litro de gasolina: ")
    if (_precio==''):
        print("Entrada incorrecta. El precio no puede omitirse. Intenta de nuevo.")
        continue
    try:
        precio=float(_precio)
    except:
        print("Entrada incorrecta. El precio debe ser un número. Intenta de nuevo.")
        continue
    # Si llego aquí, ya tengo un valor numérico en precio.
    if (not precio>0):
        print("Entrada incorrecta. El precio debe ser mayor a cero. Intenta de nuevo.")
        continue
    # Si todo salió bien, se sale del while
    break

litros=dinero/precio

_rendimiento=input("Dame el rendimiento del coche: ")
rendimiento=float(_rendimiento)

d=rendimiento*litros
t=d/v
hh=int(t)
mm=int((t-hh)*60)

print(f"El recorrido será de {d:.2f} km, en {hh} horas y {mm} minutos")