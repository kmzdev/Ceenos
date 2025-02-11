import os
import subprocess
main = input(">")


          
def traduzir_codigo_c_para_cpp(codigo_c):
    codigo_cpp = ""

    # Adiciona os headers específicos de C++
    codigo_cpp += "import os"

    # Substitui as funções de entrada e saída de C pelas de C++


    if "var." or "until" or "show" or "\\" or "++" or "//" or ".create" or ".stay" or "uses" in codigo_c: 
                codigo_cpp = codigo_c.replace("//","#").replace("var.","").replace("until","while").replace("show","print").replace("\\","   ").replace("++","+=").replace("<",">").replace(">","<").replace("i=","==").replace("=i","<").replace(".create"," = Tk()").replace(".stay",".mainloop()").replace("uses","import")      
    else:
             codigo_cpp += ("#clean")

    return codigo_cpp
       

    

pasta = "Disc\\Apps\\" + main      # Junta o diretÃ³rio base com o nome da pasta fornecido
if os.path.isdir(pasta):               # Verifica se a pasta existe
    ficheiro = os.path.join(pasta, 'main.lm')  # Caminho completo para o arquivo main.py
    if os.path.exists(ficheiro):
        subprocess.call(['python', ficheiro])
    else:
        print("Ficheiro main.lm nao encontrado")
else:
    print("Pasta nao encontrada")
code = open( ficheiro , "r")
codigo_c = code.read()
codigo_cpp = traduzir_codigo_c_para_cpp(codigo_c)
print(codigo_cpp)
exec(codigo_cpp)






