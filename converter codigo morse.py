import time
while True :
    def morse ():
        print('==========CONVERTOR DE CÓDIGO MORSE==========')
        escolha = input ('(1)Para tranformar letras em código morse.\n(2)Para transformar código morse em letras.\n\nDigite o tipo de tradução que você quer fazer: ')
        texto = input ("Escreva algo : ")
        texto = texto.replace ('ê','e')
        texto = texto.replace ('é','e')
        texto = texto.replace ('ã','a')
        texto = texto.replace ('â','a')
        texto = texto.replace ('á','a')
        texto = texto.replace('ç','c')
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
            'z':'--.. ',
            '0':'----- ',
            '1':'.---- ',
            '2':'..--- ',
            '3':'...-- ',
            '4':'....- ',
            '5':'..... ',
            '6':'-.... ',
            '7':'--... ',
            '8':'---.. ',
            '9':'----. '

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
            print('Opção invalida!')
        continuar = input('Deseja continuar traduzindo(1) ou escolher outra codificação(2): ')
        if continuar == '1':
            print(morse())
        elif continuar == "2":
            return
        time.sleep(3)
        print('____________________________________________________________')
    def binario():
        print('==========CONVERTOR DE CÓDIGO BINÁRIO==========')
        substituicoes = {
            '0': '0000 ',
            '1': '0001 ',
            '2': '0010 ',
            '3': '0011 ',
            '4': '0100 ',
            '5': '0101 ',
            '6': '0110 ',
            '7': '0111 ',
            '8': '1000 ',
            '9': '1001 '          
        }
        escolha = input('(1) Para converter número em binario.\n(2) Para converter binário em número.\n Escolha a forma de conversão: ')
        if escolha == '1':
          numero = input('Escreva os números que deseja converter: ')
          resultado = ''
        for digito in numero:
            if digito in substituicoes:
                resultado += substituicoes[digito]
            else:
                print('número invalido')
                print(binario())
        print('Número em binário:', resultado.strip())

        if escolha == '2':
            print('\\\\fazer////')
#Terminar escolha == 2  
        continuar = input('deseja continuar traduzindo(1) ou escolher outra codificação(2):')
        if continuar == '1':
            print(binario())
        elif continuar == "2":
            return  
    print('==========DECODIFICADOR==========')
    codigo = input ('Temos dois tipos de códigos:\n(1) para codigo morse\n(2) para código binario\nEscolha uma opção: ')
    if codigo == '1':
        print(morse())
    if codigo == '2':
        print(binario())