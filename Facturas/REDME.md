
# Sistema de Facturación en Python

Este programa consiste en un sistema básico de facturación desarrollado en Python utilizando Programación Orientada a Objetos (POO). El sistema permite emitir facturas solicitando únicamente el nombre del cliente y registra automáticamente la información en un archivo de texto llamado `facturas_emitidas.txt`, el cual se crea en la carpeta principal del proyecto.

Para ejecutar el programa, es necesario contar con Python 3 instalado. Una vez ubicado en la carpeta raíz del proyecto, se debe ejecutar el archivo principal mediante el comando `python main.py`. Al iniciar, el sistema mostrará un menú que permite emitir facturas o salir del programa.

El uso del método especial `__init__` se evidencia en la clase `RepositorioFacturas`. Este método se ejecuta automáticamente al crear el objeto repositorio y se encarga de inicializar los atributos del objeto, definir la ruta del archivo de facturas y abrir dicho archivo como un recurso externo, dejándolo listo para su uso durante la ejecución del programa.

El método especial `__del__` se utiliza para liberar los recursos cuando el objeto deja de existir. En este programa, el destructor se encarga de cerrar el archivo de facturas si aún se encuentra abierto, ya sea al finalizar el programa o cuando el objeto repositorio es eliminado, asegurando una correcta gestión de recursos.
##  Descripción
Este programa implementa un sistema básico de facturación usando Programación Orientada a Objetos (POO). Permite emitir facturas solicitando únicamente el nombre del cliente y registra la información en un archivo de texto. El objetivo principal es demostrar el uso de los métodos especiales `__init__` y `__del__`.

## Ejecución del programa
1. Asegúrese de tener Python 3 instalado.
2. Ubíquese en la carpeta raíz del proyecto.
3. Ejecute el archivo principal con el comando:

```bash



python main.py