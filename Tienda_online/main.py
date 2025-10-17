"""
Practica 01 "Tienda Online": Main
Gabriel Levin Cohen
21/09/2025
"""

from Services.Tienda_service import TiendaService
"""
Importamos la clase Tienda Service de nuestro modelo Tienda Service
"""
def main():
    tienda=TiendaService()

    c1=tienda.registrar_usuario("cliente", "Claudia", "claudia@uie.edu", "36202")
    c2=tienda.registrar_usuario("cliente", "Enrique", "kike@uie.edu", "36305")
    c3=tienda.registrar_usuario("cliente", "Eloy", "eloy@uie.edu", "36201")
    admin=tienda.registrar_usuario("administrador", "Gabriel", "gabriel@uie.edu","1")
    print("   Usuarios Registrados   ")
    for i in (c1, c2, c3, admin):
        print(f"{i.id} - {i.nombre} - admin? {i.is_admin()}")
    """
    Definimos la funcion principal Main
    Creamos una instancia de nuestro modelo tienda servide y lo asignamos a una variable tienda
    Registramos al primer cliente con los atributos requeridos
    Registramos al segundo cliente con los atributos requeridos
    Registramos al tercer cliente con los atributos requeridos
    Registramos al administrador con los atributos requeridos
    Imprimimos los usuarios registrados con un bucle for, para iterar las referencias previas de los usuarios
    Imprimimos el identificador unico y el nombre de cada usuario y llamamos a la funcion is_admin para comprobar el tipo de usuario
    """
  

    p1=tienda.añadir_producto("electronico", "Television - ", 500, 10, meses_garantia=24)
    p2=tienda.añadir_producto("electronico", "Laptop - ", 1000, 5, meses_garantia=36)
    p3=tienda.añadir_producto("electronico", "Audifonos - ", 200, 10, meses_garantia=12)
    p4=tienda.añadir_producto("ropa", "Playera - ", 25, 30, talla="Mediana", color="Blanco")
    p5=tienda.añadir_producto("ropa", "Pantalon - ", 35, 20, talla="Grande", color="Negro")
    print("\n Inventario  ")
    for prod in tienda.listar_productos():
        print(prod)
        """
        Registramos el primer producto con los atributos requeridos
        Registramos al segundo producto con los atributos requeridos
        Registramos el tercer producto con los atributos requeridos
        Registramos el cuarto producto con los atributos requeridos
        Registramos el quinto producto con los atributos requeridos
        Iteramos los productos registrados en el inventario para corroborar
        Imprimimos la lista de productos, el inventario
        """

    pedido1=tienda.realizar_pedido(
        c1.id, {p1.id:1, p4.id:2}
    )
    print("\n",pedido1)
    """
    Llamamos al metodo realizar pedido
    Proveemos al metodo de los datos requeridos para identificar al cliente que hace el pedido y los productos y cantidades
    Imprimimos el pedido
    """

    pedido2=tienda.realizar_pedido(
        c2.id, {p2.id:1, p4.id:2, p5.id:4}
    )
    print("\n",pedido2)
    """
    Llamamos al metodo realizar pedido
    Proveemos al metodo de los datos requeridos para identificar al cliente que hace el pedido y los productos y cantidades
    Imprimimos el pedido
    """

    pedido3=tienda.realizar_pedido(
        c3.id, {p2.id:1, p3.id:1, p5.id:1}
    )
    print("\n", pedido3)
    """
    Llamamos al metodo realizar pedido
    Proveemos al metodo de los datos requeridos para identificar al cliente que hace el pedido y los productos y cantidades
    Imprimimos el pedido
    """

    pedido4=tienda.realizar_pedido(
        c1.id, {p5.id:1}
    )
    print("\n", pedido4)
    """
    Llamamos al metodo realizar pedido
    Proveemos al metodo de los datos requeridos para identificar al cliente que hace el pedido y los productos y cantidades
    Imprimimos el pedido
    """

    print("\n Historial de Pedidos de: ", c1.nombre)
    historialc1=tienda.listar_pedidos_usuario(c1.id)
    for pedido in historialc1:
        print("\n", pedido)
        """
        Imprimimos el historial de pedidos de un cliente 
        Accedemos a la lista de pedidos asociados al identificador y buscamos el nombre del cliente
        Inicializamos un bucle dor que iterara cada pedido contenido en el historial del cliente
        Imprimimos los pedidos
        """

    print("\n Historial de pedidos de: ", c2.nombre)
    historialc2=tienda.listar_pedidos_usuario(c2.id)
    for pedido in historialc2:
        print("\n", pedido)
        """
        Imprimimos el historial de pedidos de un cliente 
        Accedemos a la lista de pedidos asociados al identificador y buscamos el nombre del cliente
        Inicializamos un bucle dor que iterara cada pedido contenido en el historial del cliente
        Imprimimos los pedidos
        """

    print("\n Inventario Actualizado")
    for producto in tienda.listar_productos():
        print(producto)
        """
        Imprimimos un encabezado
        Iteramos los productos del listado de productos para procesar las instancias
        Imprimimos esta instancia del producto al igual que sis atributos
        """
   



if __name__=="__main__":
    main()
    """
    Aseguramos que python ejecute el programa directamente desde el main
    Invocamos a la funcion main para ejecutar el programa
    """