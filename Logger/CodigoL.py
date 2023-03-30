class Logger:
    def __init__(self, mensajes, llamadas, archivo):
        self.mensajes = mensajes
        self.llamadas = llamadas
        self.archivo = open(archivo, 'w')
        self.archivo.write("--Start log--\n")

    def log(self, mensaje):
        self.mensajes += 1
        self.archivo.write("Mensaje: " + mensaje + "\n")

    def __del__(self):
        self.archivo.write("Mensajes: " + str(self.mensajes) + "\n")
        self.archivo.write("Llamadas: " + str(self.llamadas) + "\n")
        self.archivo.write("--End log--\n")
        self.archivo.close()
    
class Test:
    def __init__(self, logger):
        self.logger = logger

    def test(self):
        self.logger.log("Test")
        self.logger.llamadas += 1


