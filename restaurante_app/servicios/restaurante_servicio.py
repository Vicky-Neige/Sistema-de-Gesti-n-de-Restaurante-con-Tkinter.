from modelos.producto import Producto
from modelos.usuario import Usuario
from servicios.archivo_servicio import ArchivoServicio

class RestauranteServicio:
    def __init__(self, ruta_productos: str, ruta_usuarios: str):
        self.ruta_productos = ruta_productos
        self.ruta_usuarios = ruta_usuarios
        self.productos = []
        self.usuarios = []
        self.cargar_datos()

    def cargar_datos(self):
        raw_productos = ArchivoServicio.cargar_json(self.ruta_productos)
        self.productos = [Producto.from_dict(p) for p in raw_productos]

        raw_usuarios = ArchivoServicio.cargar_json(self.ruta_usuarios)
        self.usuarios = [Usuario.from_dict(u) for u in raw_usuarios]

    def validar_acceso(self, username: str, password: str) -> Usuario:
        for usuario in self.usuarios:
            if usuario.username == username and usuario.password == password:
                return usuario
        return None

    def obtener_productos(self) -> list:
        return self.productos

    def obtener_usuarios(self) -> list:
        return self.usuarios