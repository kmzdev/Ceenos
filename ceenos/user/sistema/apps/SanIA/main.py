import os
import time

dr = 'G:\\The own\\Projects\\osDiscv3\\user\\sistema\\apps\\SanIA\\'

#Nome da IA
ia = "SanIA"
empty = ""

with open (dr+"name.txt","r") as arquivo:
        nome = arquivo.read()
        x = arquivo.read()
        
    
if nome == empty:
    
    print("Ola,eu sou a",ia)
    nome = input("E tu como te chamas? ")
    with open (dr+"name.txt","a") as arquivo:
    #apagar nome anterior
        arquivo.truncate(0)
    #guardar novo nome
        arquivo.write(nome)
    print("Ola",nome,"prazer em conhecer voce")
else:
    print("Bem vindo de volta",nome,"!")

#Guardar nome do usuario

    

#Obter nome do usuario

#Resto do codigo

def ct():
    while True:
        res = input("Alguma pergunta? ")
        if res == "Quem criou voce?":
            print("Eu fui criada pelo Klit e a Sannys")
        elif res == "Quem e o MrBeast?":
            print("E um dos maiores youtubers")
        elif res ==  "Alex":
            print("E quem meteu o c* no Durex")
        elif res == "Quem e o Klit?":
            print("E o meu programador")
        elif res == "Quem e a Sannys":
            print("Quem?")
            print("Desconheço essa pessoa")
        elif res == "Nao":
            print("Tudo bem,estarei sempre disponivel para ajudar")
        elif res == "reset":
            with open (dr+"name.txt","a") as arquivo:
    #apagar nome anterior
                arquivo.truncate(0)
            #est()
            #os.startfile("main.py")
            break
        elif res == "sair":
            break
        else:
            print("Nao entendi")



def est():
    resposta = ""
    while resposta != "bem" or resposta != "mal":
        resposta = input("Como esta? ")

        if resposta == "bem":
            print("Que bom!")
            ct()
            break
        elif resposta == "mal":
            print("Que noticia triste")
            ct()
            break
        else:
            print("Nao entendi")
            
est()



