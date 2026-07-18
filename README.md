# Sistema de Gestión de Restaurante

  

**Estudiante:** Melany Mercedes Jaña Sambrano

  

## Descripción del Proyecto

Este es un sistema de consola interactivo desarrollado en Python para gestionar las operaciones esenciales de un restaurante. El software permite registrar y listar de forma eficiente clientes, platillos (productos estándar) y bebidas, garantizando la persistencia en memoria durante la ejecución y validando que no existan registros duplicados en el sistema.

  

---

  

## Estructura esperada del repositorio

  

restaurante_app/

│

├── modelos/

│ ├── __init__.py

│ ├── producto.py

│ ├── bebida.py

│ └── cliente.py

│

├── servicios/

│ ├── __init__.py

│ └── restaurante.py

│

├── main.py

└── README.md

  

### Descripción de los componentes:

* **`modelos/`**: Paquete que contiene las definiciones de datos y lógica propia de las entidades del sistema (`Producto`, `Bebida`, `Cliente`).

* **`servicios/`**: Paquete encargado de la lógica del negocio (`Restaurante`), aislando el almacenamiento y las validaciones de los datos puros.

* **`main.py`**: Punto de entrada de la aplicación. Gestiona exclusivamente la interfaz de consola y el menú de selección.

* **`__init__.py`**: Archivos requeridos por Python para reconocer los directorios como paquetes modulares, permitiendo las importaciones relativas limpias entre carpetas.

  

---

  

## Responsabilidad de cada Clase

  

* **`Restaurante`**: Encargada exclusiva de gestionar el almacenamiento centralizado en memoria (listas de productos y clientes) y aplicar las reglas de validación (evitar códigos e identificaciones duplicadas).

* **`Producto`**: Encargada de encapsular y representar los atributos básicos de un artículo de comida (código, nombre, categoría, precio) y de formatear sus datos de salida.

* **`Bebida`**: Especialización encargada de contener las propiedades exclusivas de un producto líquido (tamaño y tipo de envase).

* **`Cliente`**: Encargada de representar la información personal única de los consumidores (identificación, nombre completo, correo).

  

---

  

## Relación entre Producto y Bebida

La relación entre estas dos clases es de Herencia (`Bebida` hereda de `Producto`). Esto representa una relación del tipo *"Es un"*: una `Bebida` es un `Producto` especializado que comparte todas las características base (código, nombre, precio), pero extiende la funcionalidad agregando atributos únicos como tamaño y empaque. Por su parte la clase `Cliente` se mantiene aislada y no hereda de `Producto` ya que un cliente no comparte naturaleza con un artículo del menú.

  

---

  

## Principios de Diseño Aplicados (SOLID)

  

### 1. Single Responsibility Principle (SRP - Principio de Responsabilidad Única)

Se cumple rigurosamente al separar las tareas: `main.py` tiene la únicaresponsabilidad de interactuar con el usuario en consola; `Restaurante` se encarga únicamente de la gestión y reglas del negocio; mientras que las clases de la carpeta `modelos` solo guardan datos de entidades y retornan su información.

  

### 2. Open/Closed Principle (OCP - Principio de Abierto/Cerrado)

El sistema está abierto a la extensión pero cerrado a la modificación. Gracias al uso de la herencia, si el restaurante decidiera vender combos promocionales o postres con lógicas distintas, se pueden crear nuevas subclases heredando de `Producto` sin necesidad de alterar el código interno de la clase base ni la lógica de guardado de `Restaurante`.

  

### 3. Liskov Substitution Principle (LSP - Principio de Sustitución de Liskov)

Se aplica de forma perfecta en la lista general de productos. Dado que `Bebida` extiende correctamente a `Producto`, la clase `Restaurante` maneja una lista unificada de tipo `Union[Producto, Bebida]`. El sistema puede sustituir o tratar cualquier `Bebida` como si fuera un `Producto` general sin romper el programa y llamando a su comportamiento polimórfico de manera transparente.

  

---

  

## Aplicación de Polimorfismo Puro

En el método `listar_productos()`, el sistema recorre la lista genérica mediante un ciclo `for` y ejecuta:

  

producto.mostrar_informacion()

  

Aquí no se utilizan condicionales (`if/else`) para verificar manualmente si el objeto es un platillo o una bebida. Python, mediante el enlace dinámico del polimorfismo, detecta automáticamente la naturaleza del objeto en tiempo de ejecución y despliega el formato correcto diseñado para cada clase.

  

---

  

## Instrucciones de Ejecución

  

1. Abre la terminal o línea de comandos.

2. Navega hasta la carpeta raíz del proyecto (`restaurante_app`).

3. Inicia la aplicación ejecutando el archivo principal:

python main.py

  

---

  

## Reflexión: Importancia de Diseñar Proyectos Mantenibles

El diseño de software estructurado bajo principios SOLID y modularidad arquitectónica es indispensable en el desarrollo profesional. Construir código limpio y desacoplado, facilita que el software crezca de forma escalable en el futuro. Permite que múltiples desarrolladores trabajen en distintas secciones en paralelo sin generar conflictos y minimiza drásticamente la aparición de errores colaterales al modificar o depurar funciones específica, invertir tiempo en un buen diseño inicial ahorra semanas de mantenimiento técnico posterior.