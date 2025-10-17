"""
Practica 01 "Tienda Online": Models - Usuario
Gabriel Levin Cohen
21/09/2025
"""
import random
"""
Importamos la libreria random
"""

class Usuario:
    def __init__(self, nombre:str, email:str):
        self.id=random.randint(100000,999999)
        self.nombre=nombre
        self.email=email

    def is_admin(self)->bool:
        return False
    """
    Definimos la clase usuario
    Definimos la instancia y los parametros de la clase junto con su tipo
    Llamamos a random para que nos de un numero entero entre 100,000 y 999,999, especificando que queremos enteros, esto sera el identificador unico
    Guardamos el nombre del cliente y su correo electronico en la instancia
    Declaramos un metodo en la instancia para corroborar si el usuario es cliente o administrador mediante un valor booleano
    Declaramos que un usuario normal por defecto no es administrador
    """


class Cliente(Usuario):
    def __init__(self, nombre:str, email:str, cp:int=""):
        super().__init__(nombre, email)
        self.cp=cp
"""
Declaramos la subclase Cliente la cual extiende la clase usuario
Llamamos al constructor de la calse usuario e incluimos el codigo postal como un nuevo atributo de cliente, definimos tambien el tipo de cada variable
Inicializamos los atributos heredados
Añadimos el codigo postal del cliente en el atributo cp de la instancia
"""

class Administrador(Usuario):
    def is_admin(self)->bool:
        return True
"""
Declaramos la subclase Administrador la cual extiende la clase usuario
Llamamos a la funcion is_admin y cambiamos el valor booleano de False a True indicando que el usuario es administrador
"""