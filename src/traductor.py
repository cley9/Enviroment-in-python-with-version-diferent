from translate import Translator

texto = input("Ingresa un texto: ")
traductor = Translator("en", "es")
print(traductor.translate(texto))
