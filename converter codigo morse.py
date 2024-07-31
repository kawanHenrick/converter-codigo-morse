escolha = input ('(1)Para tranformar letras em código morse.\n(2)Para transformar código morse em letras.\n\nDigite o tipo de tradução que você quer fazer:')

texto = input ("Escreva algo : ")
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
substituicoesc = {
    '    ':' ',
    '.- ':'a',
    '-... ':'b',
    '-.-. ':'c',
    '-.. ':'d',
    '. ':'e',
    '..-. ':'f',
    '--. ':'g',
    '.... ':'h',
    '.. ':'i',
    '.--- ':'j',
    '-.- ':'k',
    '.-.. ':'l',
    '-- ':'m',
    '-. ':'n',
    '--- ':'o',
    '.--. ':'p',
    '--.- ':'q',
    '.-. ':'r',
    '... ':'s',
    '- ':'t',
    '..- ':'u',
    '...- ':'v',
    '.-- ':'w',
    '-..- ':'x',
    '--.- ':'y',
    '--.. ':'z'

}
if escolha == '1':
            for antiga, nova in substituicoes.items():
                texto = texto.replace(antiga, nova)
            texto = texto[:-1]
            print(texto)
#corrigir código morse com saida incompleta 
elif escolha == '2':
            for antiga, nova in substituicoesc.items():
                texto = texto.replace(antiga, nova)
            print(texto)
#loop de repetição infinita do código 
#break caso escolha numero diferente de 1 ou 2