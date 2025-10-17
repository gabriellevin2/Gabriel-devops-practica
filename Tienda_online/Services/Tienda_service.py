"""
Practica 01 "Tienda Online": Services - Tienda Service
Gabriel Levin Cohen
21/09/2025
"""

import random
from datetime import datetime
from typing import List, Dict
"""
Importamos la libreria random
Importamos la clase datetime de la libreria datetime para trabajar con la fecha actual
Importamos las clases List y Dict de la libreria typing, las cuales son una lista y un diccionario respectivamente
"""

from Models.Pedido import Pedido
from Models.Producto import Producto, ProductoElectronico, ProductoRopa
from Models.Usuario import Cliente, Administrador
"""
Importamos la clase pedido de nuestro modelo Pedido
Importamos las clases Producto, Producto Electronico y Producto Ropa de nuestro modelo Producto
Importamos las clases Cliente y Administrador de nuestro modulo Usuario
"""

class TiendaService:
    def __init__(self):
        self.usuarios:Dict[int, Cliente | Administrador]={}
        self.productos:Dict[int, Producto]={}
        self.pedidos:List[Pedido]=[]
        """
        Definimos la clase tienda service
        Declaramos el constructor de la clase y la isntancia
        Creamos el atributo usuario como diccionario vacio, y las instancias seran los valores de las instancias de cliente y/o administrador
        Creamos el atributo productos como un diccionario vacio y los productos seran indexados por su identificador unico
        Creamos el atributo pedidos como una lista vacia en donde se almacenaran las instancias de los pedidos
        """

    def registrar_usuario(self, tipo:str, nombre:str, email:str, cp:int):
        tipo_lower=tipo.lower()
        if tipo_lower=="cliente":
            usuario=Cliente(nombre, email, cp)
        elif tipo_lower=="administrador":
            usuario=Administrador(nombre, email)
        else:
            raise ValueError
        self.usuarios[usuario.id]=usuario
        return usuario
    """
    Declaramos un metodo para registrar usuarios en el que declaramos la instancia, el tipo de usuario, el nombre, el email y el codigo postal del usuario, tambien definimos el tipo de variable
    Cambiamos la cadena tipo de usuario a minusculas
    Inicializamos una condicional para verificar si el usuario es cliente o administrador y se procede a crear una instancia ya sea de cliente o administrador
    Finalizamos la condicional una vez registrado el usuario o se presenta Value Error si no se encontro el tipo de usuario
    Registramos la instancia final del diccionario utilizando el identificador unico para poder buscarlo posteriormente
    Devolvemos esa instancia final
    """

    def añadir_producto(self,
                        categoria:str,
                        nombre:str,
                        precio:int,
                        stock:int,
                        meses_garantia:int=0,
                        talla:str="",
                        color:str=""):
        cat=categoria.lower()
        if cat=="electronico":
            producto=ProductoElectronico(nombre, precio, stock, meses_garantia)
        elif cat=="ropa":
            producto=ProductoRopa(nombre, precio, stock, talla, color)
        else:
            raise ValueError
        self.productos[producto.id]=producto
        return producto
    """
    Declaramos un metodo para añadir productos en el que declaramos la instancia, la categoria del producto, el nombre, el precio y el stock del producto al igual que la garantia, la talla y el color en caso de requerirlas, tambien definimos el tipo de variable
    Cambiamos la cadena tipo de categoria a minusculas
    Inicializamos una condicional para verificar si la categoria es electronico o ropa y se procede a crear una instancia con el tipo de producto
    Finalizamos la condicional una vez añadido el producto o se presenta Value Error si no se encontro la categoria del producto
    Registramos la instancia final del diccionario utilizando el identificador unico para poder buscarlo posteriormente
    Devolvemos esa instancia final
    """

    def eliminar_producto(self, producto_id:int):
        if producto_id not in self.productos:
            raise KeyError
        del self.productos[producto_id]
        """
        Declaramos un metodo para eliminar productos en el que declaramos la isntancia y el identificador unico del producto asi como el tipo de variable que es esta misma
        Inicializamos una condicional para verificar si el identificador unico no esta en el diccionario de productos
        Imprimimos KeyError en caso de que no este en el diccionario
        Eliminamos la entrada correspondiente a ese identificador unico del producto
        """

    def listar_productos(self)->List[Producto]:
        return list(self.productos.values())
    """
    Declaramos un metodo para crear un listado de los productos y declaramos la instancia, declaramos el valor como una lista
    Imprimimos la lista que construimos a partir de los valores del diccionario
    """

    def realizar_pedido(self, usuario_id:int, items:Dict[int, int])->Pedido:
        if usuario_id not in self.usuarios:
            raise KeyError
        cliente=self.usuarios[usuario_id]
        productos_para_pedido:Dict[Producto, int]={}
        for pid, cantidad in items.items():
            if pid not in self.productos:
                raise KeyError
            producto=self.productos[pid]
            if not producto.cantidad_stock(cantidad):
                raise ValueError(f"Stock Insuficiente")
            productos_para_pedido[producto]=cantidad
        for producto, cantidad in productos_para_pedido.items():
            producto.actualizar_stock(-cantidad)

        pedido=Pedido(cliente, productos_para_pedido)
        self.pedidos.append(pedido)
        return pedido
    """
    Declaramos un metodo para realizar pedidos en el que definimos la instancia, el identificador unico del usuario y un diccionario con los productos que eligio el cliente
    Verificamos, mediante una condicional, que exista registro del identificador unico del cliente
    Imprimimos KeyError si no existe ningun registro del identificador unico del cliente
    Recuperamos el identificador unico del cliente para utilizarlo en el pedido
    Inicializamos un diccionario vacio para mapear productos a cantidades
    Inicializamos un bucle for que iterara sobre el identificador unico del producto y la cantidad proporcionada por items
    Comprobamos, mediante una condicional, que cada identificador unico del producto exista dentro del inventario
    Imprimimos KeyError en caso de que el identificador unico del producto no se encuentre en el inventario
    Recuperamos el identificador unico del producto
    Verificamos que exista suficiente stock del producto mediante una condicional
    Imprimimos ValueError en caso de no haber el stock suficiente
    Añadimos la instancia producto cantidad al diccionario
    Inicializamos un bucle for que itera aquellas instancias producto cantidad para aplicar la reduccion de stock al inventario
    Descontamos la cantidad del pedido del inventario
    Creamos la instancia pedido con el cliente y el diccionario
    Registramos los pedidos y los concatenamos al pedido
    Imprimimos el pedido
    """


        

    
    def listar_pedidos_usuario(self, usuario_id:int)->List[Pedido]:
        pedidos_usuario=[
            pedido for pedido in self.pedidos
            if pedido.cliente.id==usuario_id
        ]
        return pedidos_usuario
    """
    Declaramos un metodo para ver la lista de los pedidos por usuario y definimos la instancia y los atributos y su tipo, indicamos tambien mediante un type hint que requerimos una lista
    Inicializamos una lista
    Creamos una lista para cada pedido utilizando listas de comprension
    Inicializamos una condicional para la lista de comprension, condicionando los pedidos solo si los identificadores unicos coinciden
    Imprimimos la lista de pedidos
    """