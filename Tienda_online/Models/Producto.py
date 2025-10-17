"""
Practica 01 "Tienda Online": Models - Producto
Gabriel Levin Cohen
21/09/2025
"""

import random
"""
Importamos la libreria random
"""
class Producto:
    def __init__(self, nombre:str, precio:int, stock:int):
        self.id=random.randint(100000,999999)
        self.nombre=nombre
        self.precio=precio
        self.stock=stock
        """
        Definimos la clase producto
        Declaramos el constructor de la clase con los parametros nombre, precio y stock, y el tipo de cada una de estas, de igual manera definimos self como la instancia
        Llamamos a random para que nos de un numero entero entre 100,000 y 999,999, especificando que queremos enteros, esto sera el identificador unico
        Guardamos el nombre del producto, el precio y su stock como argumentos para poder acceder a ellos posteriormente
        """


    def cantidad_stock(self, cantidad:int)->bool:
        return self.stock>=cantidad
    """
    Declaramos un metodo para verificar la cantidad de stock disponible en base a la cantidad solicitada
    Accedemos al atributo para devolver el resultado de la comparacion del stock con el pedido
    """

    def actualizar_stock(self, cantidad:int)->None:
        if cantidad<0 and not self.cantidad_stock(-cantidad):
            raise ValueError(
                f"Stock insuficiente. La disponibilidad es: {self.stock}"
            )
        self.stock+=cantidad
    """
    Declaramos un metodo que actualiza el inventario en funcion de la cantidad en el pedido
    Inicializamos una condicional en donde se comprueba si el stock estan en valores negativos, y tras verificar el stock permite restar la cantidad
    Especificamos con un raise que si la condicion no se cumple el programa debera arrojar value error y especificar que el stock es insuficiente, al igual que la cantidad en el stock mediante una interpolacion
    En dado caso de que la condicional no se cumpliera, se modifica la cantidad en el stock de forma controlada
    """


    def __str__(self)->str:
        return(
            f"{self.id} {self.nombre}"
            f"Precio: {self.precio} euros - Stock disponoble: {self.stock}"
        )
    """
    Definimos la funcion especial que devuelve la representacion del producto como un string
    Inicializamos un return para concatenar e imprimir f-strings
    Imprimimos mediante un f-strings e interpolaciones el identificador unico y el nombre del producto
    Imprimimos mediante un f-strings e interpolaciones el precio del producto y el stock disponible 
    """

class ProductoElectronico(Producto):
    def __init__(self, nombre:str, precio:int, stock:int, meses_garantia:int):
        super().__init__(nombre, precio, stock)
        self.meses_garantia=meses_garantia

    def __str__(self)->str:
        base=super().__str__()
        return f"{base} - Garantia: {self.meses_garantia} meses"
    """
    Declaramos la subclase Producto Electronico, la cial extiende la clase Producto
    Definimos los la estancia y los parametros del producto y su tipo e integramos el nuevo parametro llamado garantia al cual tambien le asingamos el tipo de variable
    Invocamos al constructor de la clase padre (Producto) para evitar diplicar codigo
    Añadimos el atributo nuevo de la subclase.
    Definimos la funcion especial que devuelve la representacion de la garantia como un string
    Implementamos esta funcion especial de la clase padre Producto y la almacenamos en una variable
    Concatenamos a los atributos de la clase padre el nuevo atributo de la sub clase
    """

class ProductoRopa(Producto):
    def __init__(self, nombre:str, precio:int, stock:int, talla:str, color:str):
        super().__init__(nombre, precio, stock)
        self.talla=talla
        self.color=color

    def __str__(self)->str:
        base=super().__str__()
        return f"{base} - Tallas: {self.talla} - Color: {self.color}"
    """
    Declaramos la subclase Producto Ropa, la cual extiende la clase Producto
    Definimos la estancia y los parametros del producto y su tipo e integramos los nuevos parametros llamados talla y color a los cuales tambien le asingamos el tipo de variable
    Invocamos al constructor de la clase padre (Producto) para evitar duplicar codigo
    Añadimos el atributo nuevo de la subclase.
    Definimos la funcion especial que devuelve la representacion de la talla y el color como un string
    Implementamos esta funcion especial de la clase padre Producto y la almacenamos en una variable
    Concatenamos a los atributos de la clase padre los nuevos atributos de la sub clase
    """