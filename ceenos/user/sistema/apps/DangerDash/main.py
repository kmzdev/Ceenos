import time

t = time.sleep(2)

def seis():
    t
    print("Ao chegar na sala do trono,voce e recebido e o Rei pergunta:")
    t
    print("O que voce tem a dizer?:")
    t
    print("Mas depois de toda essa viagem voce nao se lembra bem do que aconteceu")
    t
    print("Entao o Rei pergunta...")
    t
    print("O seu Reino precisa de Ajuda ou vieste informar que o Reino ja esta bem?:")
    t
    escolha = input("Voce concorda com a primeira opcao?:")
    if escolha == "sim":
          print("Voce volta para casa acompanhado do exercito Hermita e pronto para Ganhar a guerra")
          t
          print("Voce vai para sua casa e se passam 2 semanas de guerra")
          t
          print("Voces ganham!!!!")
          t
          print("O Reino festeja alegre e tu e a tua familia tambem")
          t
          print("O voce ",nome,"Fica recordado como um/uma dos/das herois/heroinas")
          t
          print("FIM!")
                
    
    else:
         print("Voce volta para casa sem ajuda")
         print("Seu Rei fica chateado consigo")
         print("E voce passa a ser odeiado/a")
         print("O seu Reino perde a guerra")
         print("E voce ",nome,"morre e fica recordado/a como o/a incopetente") 
         


def cinco():
    t
    print("Voce continua a viagem e chega ao Reino Hermita")
    t
    print("Mas ao chegar ao portao os guardas te perguntam quem es e de onde vens")
    t
    print("E voce responde:")
    t
    print("Eu sou ",nome," e vim falar com o Rei")
    t
    escolha = input("Os guardas te perguntam se voce e do Reino Ngiza")
    
    if escolha == "sim":
        print("Eles abrem o portao e te levam a a sala do trono")
        seis()
    else:
        print("Else nao te deixam entrar e voce volta para casa")
        print("Voce volta para casa sem ajuda")
        print("Seu Rei fica chateado consigo")
        print("E voce passa a ser odeiado/a")
        print("O seu Reino perde a guerra")
        print("E voce ",nome,"morre e fica recordado/a como o/a incopetente") 
         

        
def quatro():
    t
    print("Voce encontra um percipicio,mas nao e assim tao grande")
    t
    escolha = input("Voce quer pular?:")
    if escolha == "nao":
        cinco()
    else:
        print("Voce nao consegue pular alto suficiente")
        print("Entao voce cai no burraco e morre")
        
def tres():
    t
    print("Voce entra na caverna,e ve agua e em seguida voce bebe")
    t
    print("Mas voce ouve o barrulho de morcego")
    t
    escolha = input("Procurar o morcego e matar?:")
    if escolha == "sim":
        print("Voce encotra o morcego e  mata")
        t
        print("E voce dorme e Acorda")
        t
        quatro()
    else:
        print("Enquanto voce dorme o morcego ataca voce,voce apanha voce uma infeccao e morre")

def dois():
    t
    print("Voce continua e encontra um local para descancar")
    t
    print("Mas voce sabe que pode ter alguem atras de ti")
    t
    escolha = input("Descancar?:")
    if escolha == "sim":
        tres()
    else:
        quatro()

def um():
    t
    print("Começamos com a viagem a pe,e se passam 9 horas")
    t
    print("Aparece um estranho e o oferece agua,e voce acabou a sua")
    t
    escolha = input("Aceitar?:")
    if escolha == "nao":
        dois()
    else:
        print("A agua era envenenada e voce morreu")

print("Bem vindo ao Danger-Dash")
time.sleep(2)
nome = input("Escolha um nome para o seu persongem:")
print(nome,'Voce esta num mundo chamado "Ngiza"')
time.sleep(2)
print('Seu objectivo',nome,'e ir ate o outro lado da montanha e entregar um comunicado real sobre uma alianca o com o povo "hermita"')
print("Mas a jornada nao vai ser facil,pois teras que passar por muitos desafios")
print("Mas Lembre-se",nome,"Voce apenas tem uma vida")
escolha = input("[s/n]Começar:")
if escolha == "s":
    um()
else:
    exit()
