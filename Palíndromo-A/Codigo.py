class palindromoA:
    def __init__(self, frase):
        self.frase = frase
        self.frase = self.frase.replace(" ", "")
        self.frase = self.frase.lower()
        self.frase = self.frase.replace("á", "a")
        self.frase = self.frase.replace("é", "e")
        self.frase = self.frase.replace("í", "i")
        self.frase = self.frase.replace("ó", "o")
        self.frase = self.frase.replace("ú", "u")
        self.frase = self.frase.replace("ñ", "n")
        self.frase = self.frase.replace("ü", "u")
        self.frase = self.frase.replace("¿", "")
        self.frase = self.frase.replace("?", "")
        self.frase = self.frase.replace("¡", "")
        self.frase = self.frase.replace("!", "")
        self.frase = self.frase.replace(",", "")
        self.frase = self.frase.replace(".", "")
        self.frase = self.frase.replace(":", "")
        self.frase = self.frase.replace(";", "")
        self.frase = self.frase.replace("(", "")

    def palindromo(self):
        if self.frase == self.frase[::-1]:
            return True
        else:
            return False
print ("Ingrese una frase")
frase = input()
palindromoA = palindromoA(frase)
if palindromoA.palindromo():
    print ("Es palindromo")
else:
    print ("No es palindromo")