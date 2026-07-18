from restaurante_app.servicios.restaurante import Restaurante
from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.bebida import Bebida
from restaurante_app.modelos.cliente import Cliente

def mostrar_menu():
    print("\n=======================================")
    print("        SISTEMA DE RESTAURANTE         ")
    print("=======================================")
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("---------------------------------------")
    print("4. Listar productos")
    print("5. Listar clientes")
    print("---------------------------------------")
    print("6. Salir")
    print("=======================================")

def ejecutar_sistema():
    servicio_restaurante = Restaurante()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ").strip()

        if opcion == "1":
            print("\n--- Registrar Producto ---")
            codigo = input("Código: ").strip()
            nombre = input("Nombre: ").strip()
            categoria = input("Categoría: ").strip()
            try:
                precio = float(input("Precio: ").strip())
                nuevo_producto = Producto(codigo, nombre, categoria, precio)
                servicio_restaurante.registrar_producto(nuevo_producto)
            except ValueError:
                print("Error: El precio debe ser un número válido.")

        elif opcion == "2":
            print("\n--- Registrar Bebida ---")
            codigo = input("Código: ").strip()
            nombre = input("Nombre: ").strip()
            categoria = input("Categoría: ").strip()
            try:
                precio = float(input("Precio: ").strip())
                tamano = input("Tamaño: ").strip()
                tipo_envase = input("Tipo de envase: ").strip()
                nueva_bebida = Bebida(codigo, nombre, categoria, precio, tamano, tipo_envase)
                servicio_restaurante.registrar_producto(nueva_bebida)
            except ValueError:
                print("Error: El precio debe ser un número válido.")

        elif opcion == "3":
            print("\n--- Registrar Cliente ---")
            identificacion = input("Identificación: ").strip()
            nombre = input("Nombre completo: ").strip()
            correo = input("Correo electrónico: ").strip()
            nuevo_cliente = Cliente(identificacion, nombre, correo)
            servicio_restaurante.registrar_cliente(nuevo_cliente)

        elif opcion == "4":
            servicio_restaurante.listar_productos()

        elif opcion == "5":
            servicio_restaurante.listar_clientes()

        elif opcion == "6":
            print("\n¡Gracias por usar el sistema! Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo del 1 al 6.")

if __name__ == "__main__":
    ejecutar_sistema()