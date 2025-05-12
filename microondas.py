import time
ligado= False
tempo= 0
potencia = 0


def ligar(novo_tempo, nova_potencia):
    global ligado, tempo, potencia
    if not ligado:
        ligado = True
        tempo= novo_tempo
        potencia= nova_potencia
        print (f' microondas ligado por {tempo} segundos na potencia {potencia}')
        iniciar_cronometro (tempo)
        desligar () # desligar automaticamente
    else: 
        print ("o microondas ja esta ligado")

def desligar ():
    global ligado
    if ligado:
        ligado = False
        print ("microondas esta ligado ")
    else:
        print(" microondas ja esta desligado")

def status ():
    if ligado:
         print (f" tempo: {tempo} segundos /n potência: {potencia}")
    else: 
        print( f"desligado")
def iniciar_cronometro(segundos):
    while segundos >0:
        print (f"tempo restante: {segundos} segundos", end="\r")
        time.sleep(1)
        segundos -= 1 # segundos = segundos
        print("\n tempo esgotado")

#pre definicioes
def pipoca():
    ligar( 30, 100)

#rodar a funçao
pipoca()