# metodo instacia 
from CodigoA import Palindromo
class Palindromotest(Palindromo):
    def __init__(self, texto):
        self.texto = texto
    def test(self):
        if self.texto == self.texto[::-1]:
            return True
        else:
            return False
    def __del__(self):
        print(self.texto.upper())
