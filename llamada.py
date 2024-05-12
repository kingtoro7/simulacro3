from usuario import Usuario
from sistemausuarios import SistemaUsuarios

sistema = SistemaUsuarios()

usuario1 = Usuario("Carlos", "Fernandez")
usuario2 = Usuario("Manuel", "Roman")
sistema.alta_usuario(usuario1)

usuario1.agregar_amigo(usuario2)

usuario1.enviar_mensaje(usuario2, "Hola amigo, como estas?")

print("Amigos de Carlos:", [amigo.nombre for amigo in usuario1.listar_amigos()])
print("\nMensajes recibidos por Manuel")
for remitente, mensaje in usuario2.listar_mensajes_recibidos():
    print(f"De: {remitente.nombre}, Mensaje: {mensaje}")