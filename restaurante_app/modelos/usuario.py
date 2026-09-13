class Usuario:
    def __init__(self, id_usuario: int, username: str, password: str, nombre: str, rol: str):
        self.id = id_usuario
        self.username = username
        self.password = password
        self.nombre = nombre
        self.rol = rol

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            id_usuario=data.get("id"),
            username=data.get("username", ""),
            password=data.get("password", ""),
            nombre=data.get("nombre", ""),
            rol=data.get("rol", "")
        )