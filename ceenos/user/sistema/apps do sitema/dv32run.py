import os
import subprocess
main = input(">")

pasta = "Disc\\Apps\\" + main      
if os.path.isdir(pasta):               
    ficheiro = os.path.join(pasta, 'main.py') 
    if os.path.exists(ficheiro):
        subprocess.call(['python', ficheiro])
    else:
        print("Arquivo mae nao encontrado")
else:
    print("Pasta nao encontrada")


