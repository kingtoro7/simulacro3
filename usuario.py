class Usuario:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.amigos = []
        self.mensajes_recibidos = []

    def agregar_amigo(self, amigo):
        self.amigos.append(amigo)

    def eliminar_amigo(self, amigo):
        self.amigos.remove(amigo)

    def enviar_mensaje(self, amigo, mensaje):
        amigo.recibir_mensaje(self, mensaje)

    def recibir_mensaje(self, remitente, mensaje):
        self.mensajes_recibidos.append((remitente, mensaje))
    
    def listar_amigos(self):
        return self.amigos

    def listar_mensajes_recibidos(self):
        return self.mensajes_recibidos
 
    


        