from random import *
pontos = 0 
print('''
      Porta Da Fortuna
      ================================================
      
      Existe um premio atras dessas portas \n
      _________________
      |               |
      |               |
      |      /|       |  
      |       |       |  
      |       |    O  |  
      |       |       |  
      |    _______    |  
      |               |
      |               |
      -----------------
      _________________
      |               |
      |               |
      |      ____     |  
      |     (   /     |  
      |        /   O  |  
      |       /       |  
      |      /        |
      |     ------    |       |
      |               |
      -----------------
      _________________
      |               |
      |    ______     |
      |          |    |  
      |          |    |  
      |    ------| O  |  
      |          |    |  
      |    ______|    |  
      |               |
      |               |
      -----------------  
    
    '''
)

while pontos < 21:
    porta = int(input('Escolha Um Porta: 1 2 3:\n '))

    Certa = randint(1,3)

    if porta == Certa:
        print("Porta Certa !!!")
        pontos += 1
        print(F"Voce Fez {pontos} pontos")
    else:
        print("Porta Errada !!!")
        print(F"Voce Tem {pontos} pontos")
    print('================================================')

print("Voce Ganhou!!!")