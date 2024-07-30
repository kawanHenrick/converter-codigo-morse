texto = input ("Escreva algo : ")
texto = texto.replace ('é','e')
texto=texto.lower()


substituicoes = {
    ' ':'    ',
    'a':'.-/',
    'b':'-.../',
    'c':'-.-./',
    'd':'-../',
    'e': './',
    'f':'..-./',
    'g':'--./',
    'h':'..../',
    'i':'../',
    'j':'.---/',
    'k':'-.-/',
    'l':'.-../',
    'm':'--/',
    'n':'-./',
    'o':'---/',
    'p':'.--./',
    'q':'--.-/',
    'r':'.-./',
    's':'.../',
    't':'-/',
    'u':'..-/',
    'v':'...-/',
    'w':'.--/',
    'x':'-..-/',
    'y':'--.-/',
    'z':'--..'

}

for antiga, nova in substituicoes.items():
    texto = texto.replace(antiga, nova)
texto = texto[:-1]
print(texto) 