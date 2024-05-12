class SistemaUsuarios:
    def __init__(self):
        self.usuarios = []

    def alta_usuario(self, usuario):
        self.usuarios.append(usuario)    

    def baja_usuario(self, usuario):
        self.usuarios.remove(usuario)

    def buscar_usuario(self, nombre):
        for usuario in self.usuarios:
            if usuario.nomnbre == nombre:
                return usuario
        return None