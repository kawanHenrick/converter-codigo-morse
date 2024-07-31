import time
print('==========CONVERTOR DE CÓDIGO MORSE==========')
while True :
 escolha = input ('(1)Para tranformar letras em código morse.\n(2)Para transformar código morse em letras.\n\nDigite o tipo de tradução que você quer fazer:')

 texto = input ("Escreva algo : ")
 texto = texto.replace ('ê','e')
 texto = texto.replace ('é','e')
 texto = texto.replace ('ã','a')
 texto = texto.replace ('â','a')
 texto = texto.replace ('á','a')
 texto=texto.lower()

 substituicoes = {
    ' ':'    ',
    'a':'.- ',
    'b':'-... ',
    'c':'-.-. ',
    'd':'-.. ',
    'e': '. ',
    'f':'..-. ',
    'g':'--. ',
    'h':'.... ',
    'i':'.. ',
    'j':'.--- ',
    'k':'-.- ',
    'l':'.-.. ',
    'm':'-- ',
    'n':'-. ',
    'o':'--- ',
    'p':'.--. ',
    'q':'--.- ',
    'r':'.-. ',
    's':'... ',
    't':'- ',
    'u':'..- ',
    'v':'...- ',
    'w':'.-- ',
    'x':'-..- ',
    'y':'--.- ',
    'z':'--.. '

 }
 inversao = {v.strip(): k for k,v in substituicoes.items()}

 if escolha == '1':
            for antiga, nova in substituicoes.items():
                texto = texto.replace(antiga, nova)
            texto = texto[:-1]
            print(texto)
        
 elif escolha == '2':
            letras = texto.split(' ')
            resultado = ''
            for letra in letras :
                if letra in inversao:
                    resultado += inversao[letra]
                elif letra == '':
                    resultado += ' '
            print (resultado.strip())
            
 else:
    print('opção invalida')
 time.sleep(3)
 print('____________________________________________________________')