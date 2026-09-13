# Restaurante App - Semana 13 (Interfaz Gráfica de Usuario).

## Información Académica
- **Estudiante:** Mayerli Melania Granda Quispe
- **Asignatura:** Programación Orientada a Objetos
- **Semestre:** Segundo Semestre
- **Paralelo:** "F"
- **MSC:** Kevin Bolívar Lascano Sánchez
- **Semana:** Semana 13
## Estructura del Proyecto

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
└── README.md
```
## Separación de Responsabilidades

 -**`datos/`**: Archivos JSON con la información persistente (`productos.json`, `usuarios.json`).
- **`modelos/`**: Clases que representan las entidades del sistema (`Producto`, `Usuario`).
- **`servicios/`**: Lógica de lectura de datos (`ArchivoServicio`) y gestión de operaciones del restaurante (`RestauranteServicio`).
- **`ui/`**: Vistas construidas en Tkinter(`LoginView`, `MainView`).La interfaz visual no lee archivos de datos directamente.
- **`main.py`**: Punto de entrada principal que instancia Tkinter, carga los servicios e inicia el flujo de la aplicación.

## Flujo de la Navegación

1. Inicio: Carga inicial de la interfaz en la vista `LoginView`.
2. Validación: Autenticación simulada utilizando los usuarios del archivo JSON (Ejemplo: usuario `admin`, clave `123`).
3. Menú principal: Transición a `MainView` con pestañas para visualizar productos y usuarios mediante tablas (`Treeview`).Opción Ventas identificada como funcionalidad pendiente.
4. Cierre de sección: Regresa a LoginView dentro de la misma ventana activa sin duplicar instancias de Tkinter.