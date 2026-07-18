from typing import List, Union
from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente

class Restaurante:
    def __init__(self):
        # Manejo centralizado de listas (SRI)
        self.productos: List[Union[Producto, Bebida]] = []
        self.clientes: List[Cliente] = []

    def registrar_producto(self, producto: Union[Producto, Bebida]) -> bool:
        # Validar que no se repitan códigos
        for p in self.productos:
            if p.codigo == producto.codigo:
                print(f"Error: Ya existe un producto con el código '{producto.codigo}'")
                return False
        
        # Guardado correcto fuera del ciclo for
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' registrado con éxito.")
        return True

    def registrar_cliente(self, cliente: Cliente) -> bool:
        # Validar que no se repitan identificaciones
        for c in self.clientes:
            if c.identificacion == cliente.identificacion:
                print(f"Error: Ya existe un cliente con la identificación '{cliente.identificacion}'")
                return False
        
        # Guardado correcto fuera del ciclo for
        self.clientes.append(cliente)
        print(f"Cliente '{cliente.nombre}' registrado con éxito.")
        return True

    def listar_productos(self) -> None:
        if not self.productos:
            print("No hay productos registrados en el sistema.")
            return

        print("\n--- LISTA DE PRODUCTOS Y BEBIDAS ---")
        for producto in self.productos:
            # Corregido: Se envuelve en un print() para mostrar el texto que devuelve el return
            if hasattr(producto, 'mostrar_informacion'):
                print(producto.mostrar_informacion())
            else:
                print(producto)

    def listar_clientes(self) -> None:
        if not self.clientes:
            print("No hay clientes registrados en el sistema.")
            return

        print("\n--- LISTA DE CLIENTES ---")
        for cliente in self.clientes:
            # Corregido: Se envuelve en un print() para mostrar el texto que devuelve el return
            if hasattr(cliente, 'mostrar_informacion'):
                print(cliente.mostrar_informacion())
            else:
                print(cliente)