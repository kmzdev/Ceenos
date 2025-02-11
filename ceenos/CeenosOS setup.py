import time
import subprocess
import os

#Instalacao
def instalacao():
    print("Criando directorio 'OsDir e D\' ")
    time.sleep(2)
    print("Extraindo e copiando ficheiros...")
    time.sleep(2)
    t = """
dvk.s
iu.s
apps.s
tema.s
config.s
boot.s
uss.s
gst.s
"""

    print(t)
    print("Ficheiros extraidos e copiados com sucesso")
    time.sleep(2)
    print("A iniciar com processo de configuraçao")
    nome = input("Insira um nome de usuario:")
    senha = input("Insira uma senha para o computador:")
    with open("usuarios.txt", "a") as arquivo:
        arquivo.truncate(0)
        arquivo.write(f"{nome}:{senha}\n")
    with open("usuario.txt", "a") as arquivo:
        arquivo.truncate(0)
        arquivo.write(f"{nome}")

    print("Usuário cadastrado com sucesso!")
    time.sleep(5)
    print("O DivinoOS foi instalado com sucesso no seu computador")
    print("O seu computador vai reniciar")
    print("Ate logo",nome,"!")
    time.sleep(5)
    os.system("cls")
    print("Reniciando...")
    time.sleep(5)
    os.system("cls")
    print("Bem vindo",nome)
    files = os.listdir('cnx\\')
    directory = 'cnx\\'
    # for filename in os.listdir(directory):
       # if filename == 'main.py':
           # with open(os.path.join(directory, filename), 'r') as file:
               # file_content = file.read()
                # #Modificar a variável "ativo" para "sim" no conteúdo do arquivo*
               # file_content = file_content.replace("ph='L:\\'","ph='"+main+"'")
           # with open(os.path.join(directory, filename), 'w') as file:
               # file.write(file_content)
      
    os.startfile("kernel.py")
    exit()
    
#Saudacao

    
print("Bem vindo ao instalador do DivinoOS")
print("Responda com 's'para sim e 'n' para nao")
print("Digite 'res' para reniciar o instalador") 
    
while True:
    x = input("Deseja continuar?: ")
    if x == "n":
        print("A encerrar instalador...")
        time.sleep(3)
        exit()
    elif x == "s":
        instalacao()
    elif x =="res":
       subprocess.run(["python","DivinoOS setup.py"])
    else:
        print("Por favor responda com sim ou nao")
        

