# Programación Orientada a Objetos - UNAL

## Clase 11: Modulos y Paquetes

En Python, a medida que los proyectos crecen, se vuelve necesario organizar el código en módulos y paquetes para facilitar su mantenimiento y legibilidad.

### Modulos
Un módulo es un archivo Python que contiene definiciones de clases, funciones y variables. Es la unidad básica de organización del código en Python.

```python 
class MyClass:
  def __init__(self, nombre):
    self.nombre = nombre

  def greet(self):
    print(f"Hola, mi nombre es {self.nombre}")

def my_function(argumento):
  print(f"La función recibió el argumento: {argumento}")
```

### Paquetes
Un paquete es una colección de módulos relacionados que se agrupan en una carpeta. Para que una carpeta se considere un paquete, debe contener un archivo especial llamado `__init__.py`.

```
estructura_archivos/
├── paquete/
│   ├── __init__.py
│   ├── modulo1.py
│   └── modulo2.py
└── main.py
```

**Ejemplo:**
```
estructura_archivos/
├── paquete/
│   ├── __init__.py
│   ├── saludar.py
│   └── despedirse.py
└── main.py
```

```python 
# main.py
import paquete.saludar as saludar
import paquete.despedirse as despedirse

def main():
  nombre = "Juan"
  saludo = saludar.Saludar(nombre)
  despedida = despedirse.Despedirse(nombre)
  print(saludo.saludar_casual())
  print(saludo.saludar_formal())
  print(saludo.saludar_educado())
  print(saludo.saludar_cordial())
  print(despedida.despedirse_formal())
  print(despedida.despedirse_casual())
  print(despedida.despedirse_educado())
  print(despedida.despedirse_cordial())

if __name__ == "__main__":
  main()  
```

```python 
# saludar.py
class Saludar():
  def __init__(self, nombre:str):
      self.nombre = nombre
  def saludar_casual(self):
    return f"Hola {self.nombre}"
  def saludar_formal(self):
    return f"Buenos días {self.nombre}"
  def saludar_educado(self):
    return f"Un placer saludarte {self.nombre}"
  def saludar_cordial(self):
    return f"Que gusto verte {self.nombre}" 
```

```python 
# despedirse.py
class Despedirse:
  def __init__(self, nombre:str):
    self.nombre  = nombre
  
  def despedirse_formal(self):
    return f"Adios {self.nombre}"
  
  def despedirse_casual(self):
    return f"Chao {self.nombre}"
  
  def despedirse_educado(self):
    return f"Hasta luego {self.nombre}"
  
  def despedirse_cordial(self):
    return f"Nos vemos {self.nombre}" 
```

### Ventajas de usar paquetes

- **Organización**: Permite dividir el código en unidades más pequeñas y manejables.
- **Reutilización**: Facilita la reutilización de código en diferentes proyectos.
- **Mantenimiento**: Simplifica el mantenimiento y la actualización del código.
- **Legibilidad**: Mejora la legibilidad y comprensión del código.


## Tipos de imports
### Imports Absolutos
Los imports absolutos especifican el camino completo desde el directorio raíz del proyecto hasta el módulo que deseas importar. Son preferidos por su claridad y son recomendados por PEP 8 cuando no provocan expresiones demasiado largas.

**Ejemplo:** Teniendo en cuenta el siguiente paquete:

 ```mermaid
classDiagram
    class Database {
        +connect()
    }
    class Product {
        -db Database
        +query()
    }
    Database <|-- Product: uses
```

```
ecommerce/
│   __init__.py
│   main.py
│
├── database/
│   │   __init__.py
│   │   database.py
│
└── products/
    │   __init__.py
    │   products.py

```


```python
# import absoluto
from ecommerce.database.database import Database
```

### Imports Relativos
Los imports relativos utilizan puntos para indicar el módulo actual o el directorio de paquetes. Son útiles para importar entre paquetes y módulos dentro de una misma aplicación sin necesidad de nombrar el paquete raíz.

**Ejemplo:**
```python
# import relativo
from .database import Database
```

### Recomendaciones:
- Mantener los imports al principio del archivo, justo después de cualquier comentario o cadena de documentación.
- Agrupar los imports en el siguiente orden: bibliotecas estándar, bibliotecas de terceros y finalmente, aplicaciones o bibliotecas locales.
- Separar cada grupo de imports con una línea en blanco.
- De preferencia usar imports absolutos a relativos, ya que son más legibles y tienden a ser mejores mantenidos.

## El famoso ` __name__ == "__main__"`
Esta estructura se utiliza para determinar si el script está siendo ejecutado como el programa principal o si ha sido importado como un módulo en otro script. Esto es útil para proporcionar dos comportamientos diferentes: uno cuando el módulo es ejecutado directamente, y otro cuando es importado.

Cuando Python ejecuta un archivo, antes de ejecutar el código, define algunas variables especiales. `__name__` es una de esas variables. Si el archivo es el punto de entrada principal, Python establece `__name__` igual a `__main__`. Si el archivo está siendo importado desde otro módulo, `__name__` se establece al nombre del archivo/módulo.

**Ejemplo:**
```python
# script.py
def funcion_principal():
    print("Función principal ejecutándose")

def otra_funcion():
    print("Otra función ejecutándose")

if __name__ == "__main__":
    funcion_principal()
```
Al ejecutar script.py directamente, verás el mensaje de funcion_principal. Pero si importas script.py en otro módulo, por ejemplo con import script, funcion_principal no se ejecutará automáticamente, evitando efectos secundarios no deseados en el módulo importador.

**Utilidad:** Esta característica permite que un módulo ejecute algún código de inicialización (como probar funciones o clases) solo cuando se está ejecutando como el programa principal. Esto evita que el código de prueba o inicialización se ejecute cuando el módulo se importa en otro script.

## Reto 5: 
1. Create a package with all code of class *Shape*, this exersice should be conducted in two ways:
 - A unique module inside of package *Shape*
 - Individual modules that import *Shape* in inheritates from it.

