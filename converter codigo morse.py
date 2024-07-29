input = texto = ("escreva algo: ")
texto = texto.replace ('é','e')
texto=texto.lower()


substituicoes = {
    'e': './',
    't': '-/',
    'o': '---/',
    'x': '-..-/',
    's':'.../',
    'u':'..-/',
    'm':'--/',
    'p':'.--./',
    ' ':'      ',
    'l':'.-../',
    'a':'.-/',
    'b':'-.../',
    'c':'-.-./',
    'd':'-../',
    'f':'..-./',
    'g':'--./' ,
    'h':'....'
}

for antiga, nova in substituicoes.items():
    texto = texto.replace(antiga, nova)
texto = texto[:-1]
print(texto) 
