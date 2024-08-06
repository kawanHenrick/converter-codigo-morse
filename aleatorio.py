import random
animais = []
while len(animais) < 4 :
    animal= input('escreva o nome de um animal: ')
    animais.append (animal)
sorteio = random.sample (animais,1)
print(sorteio)
    
