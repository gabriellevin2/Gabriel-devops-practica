"""
Practica 01 "Tienda Online": Models - Pedido
Gabriel Levin Cohen
21/09/2025
"""
import random
from datetime import datetime
"""
Importamos la libreria random, la cual nos permitira calcular un numero aleatorio dentro de los parametros que etablezcamos
Importamos la clase datetime que proviene de la libreria datetime, la cual nos permite trabajar directamente con las fechas (util para operaciones con fechas y horarios)
"""

class Pedido:
    def __init__(self, cliente, productos):
        self.id=random.randint(100000,999999)
        self.cliente=cliente
        self.productos=productos
        self.fecha=datetime.now()
        """
        Definimos la clase pedido
        Declaramos el constructor de la clase con los parametros cliente y productos, utilizando self como referencia a la instancia que estamos creando
        Llamamos a random para que nos de un numero entero entre 100,000 y 999,999, especificando que queremos enteros, esto sera el identificador unico
        Guardamos la referencia del cliente en esta instancia para poder acceder a ella mas adelante
        Almacenamos la lista que forma el atributo productos, para poder iterarlos despues
        Registramos la fecha en la que se crea el pedido
        """


    def calcular_total(self)->float:
        total=0
        for producto, cantidad in self.productos.items():
            total+=producto.precio*cantidad
        return total
    """
    Declaramos un metodo llamado calcular total, el cual calculara el importe total de cada pedido y aseguramos que devuelva un float con un type hint 
    Inicializamos un acumulador en 0 llamado total para ir sumando los importes de cada producto
    Inicializamos un bucle el cual iterara sobre el valor y la clave de productos, donde producto es la clave y cantidad el valor 
    Calculamos el total actual y lo vamos acumulando en total
    Devolvemos el valor acumulado en total tras interrumpir la ejecucion
    """
    
    
    def __str__(self)->str:
        lineas=[
            f"ID del pedido: {self.id}",
            f"Cliente: {getattr(self.cliente, "nombre", "desconocido")}",
            f"Fecha (año-mes-día): {self.fecha.strftime("%Y-%m-%d")}",
            "Productos"
        ]
        for producto, cantidad in self.productos.items():
            subtotal=producto.precio*cantidad
            lineas.append(f"{producto.nombre} * {cantidad}: {subtotal:.2f} euros")
        lineas.append(f"El total es: {self.calcular_total()} euros")
        return "\n".join(lineas)
    """
    Definimos la funcion especial que devuelve la representacion de producto como un string, de esta forma podemos mostrar el pedido
    Inicializamos una lista llamada lineas
    Imprimimos mediante un f-string el id del pedido utilizando una interpolacion para imprimir el dato
    Imprimimos mediante un f-string y utilizando un getattr el cual nos permite obtener un atributo dinamico dentro del objeto cliente, en caso de no encontrar ningun atributo nombre, arrojara desconocido por defecto
    Imprimimos mediante un f-string y la libreria datetime la fecha del pedido aclarando el formato utilizado
    Insertamos el string Productos a la lista llamada lineas
    Inicializamos un bucle for que recorrera los productos del pedido para imprimirlos en una sola linea con la cantidad de productos y el total acumulado de los mismos
    Calculamos el total acumulado de los productos iguales y lo guardamos en la variable subtotal
    Concatenamos el nombre del producto, la cantidad y el subtotal a la lista lineas
    Salimos del bucle for y concatenamos el calculo realizado para calcular el total de los pedidos a la lista lineas
    Imprimimos una cadena formada por todas las lineas unidas por saltos de linea para lograr una visualizacion mas interactiva y legible
    """