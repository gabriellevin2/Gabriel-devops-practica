# Tienda Online (Practica 2)
## Gabriel Levin Cohen 
## 29/09/2025

Esta practica se compone de 2 modulos principales y un archivo main. Models y Tienda Service siendo los modulos.

Models se compone de pedido, usuario y producto.
El modulo define la clase Pedido, la cual se utiliza para modelar pedidos dentro de la tienda online.
Los pedidos contienen información sobre:
El cliente que realiza el pedido.
Los productos incluidos en el pedido.
La fecha de creación del pedido.
Un identificador unico del pedido (Generado utilizando random)


El modulo define la clase Usuario, la cual se utiliza para modelar los usuarios y sus entidades.
Usuario es la clase base que represnta a cualquier usuario del sistema.
Usuario Cliente es una subclase de usuario y añade informacion adicional (Codigo Postal)
Usuario Administrador es una subclase de usuario y contiene privilegios de administracion.


El modulo define la clase Producto, la cual se utiliza para modelar los productos dentro de la tienda online.
La clase producto permite:
Generar automaticamente identificadores unicos de los productos.
Controlar el inventario validando el stock de los productos.
Extensibilidad con la herencia de los distintos tipos de productos.
Representar cada producto con __str__


El siguiente modulo se compone de Tienda Service, el cual permite:
Centralizar la logica de la tienda online.
Gestionar los usuarios, productos y pedidos.
Controlar el inventario.
Asegurar que los pedidos solo se realicen si hay stock suciciente.

Finalmente el archivo main permite:
Inicializar una isntancia de la tienda online.
Registrar usuarios (clientes y administradores)
Añadir productos de distintas categorias.
Mostrar inventario y usuarios.
Simular la creacion de pedidos.
Imprimir pedidos.
Consultar historial de los pedidos.
Mostrar inventario actualizado.


