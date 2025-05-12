import time
ligado= False
tempo= 0
temperatura=0

def ligar(novo_tempo,nova_temperatura):
    global ligado, tempo, temperatura
    if not ligado:
        ligado = True
        tempo= novo_tempo
        temperatura= nova_temperatura
        print (f' maquina de louças ligado por {tempo} segundos na temperatura {temperatura}')
        iniciar_cronometro (tempo)
        desligar () # desligar automaticamente
    else: 
        print ("o a maquina de louças ja esta ligada")

def desligar ():
    global ligado
    if ligado:
        ligado = False
        print ("a maquina de louças esta ligada ")
    else:
        print(" a maquina de louças ja esta desligada")
def status ():
    if ligado:
         print (f" tempo: {tempo} segundos /n temperatura: {temperatura}")
    else: 
        print( f"desligada")    
def iniciar_cronometro(segundos):
    while segundos >0:
        print (f"tempo restante: {segundos} segundos", end="\r")
        time.sleep(1)
        segundos -= 1 # segundos = segundos
        print("\n tempo esgotado")

def vidro():
    ligar( 120, 100)

vidro()

def plastico():
    ligar( 60, 21)

plastico()

def metal():
    ligar( 120, 30)

metal()

escolha= input (" digite oque voce deseja lavar: 1 para vidro, 2 para plastico, 3 para metal")
if input==1:
    vidro()
elif input==2:
    plastico()
elif input==3:
    metal()
else:
    print("digite um numero valido")