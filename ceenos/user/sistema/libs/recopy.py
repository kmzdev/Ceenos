import os 
#criar um ficheiro sem nome
#copiar os dados do ficheiro para o fichero sem nome
#mudar o nome do ficheiro sem nome para o nome do ficheiro principal
#apagar o ficheiro pricipal

dr = 'C:\\ceenos\\user\\'

def copiar():
    file = input("copiar ")
    org = "user\\" + file
    if org == 'user\\':
        pass
    elif os.path.exists(org):
        x = file.split('.')
        y = x[0] + "_copia" + "." + x[1]
        read = open( org , "r")
        dados = read.read()
        ficheiro = "user\\" + y  
        abrir = open( ficheiro , "a")
        colar_dados = abrir.write(dados)
        print("O ficheiro ",file," foi copiado")
    else:
        print("ficheiro nao encontrado")

def copy(file):
    org = file
    if org == 'user\\':
        pass
    elif os.path.exists(org):
        x = file.split('.')
        y = x[0] + "_copia" + "." + x[1]
        read = open( org , "r")
        dados = read.read()
        ficheiro = y  
        abrir = open( ficheiro , "a")
        colar_dados = abrir.write(dados)
        print("O ficheiro ",file," foi copiado")
    else:
        print("ficheiro nao encontrado")

def copy_main(file):
    org = file
    if org == 'user\\':
        pass
    elif os.path.exists(org):
        x = file.split('.')
        y ="main" + "." + x[1]
        read = open( org , "r")
        dados = read.read()
        ficheiro = y  
        abrir = open( ficheiro , "a")
        colar_dados = abrir.write(dados)
        print("O ficheiro ",file," foi copiado")
    else:
        print("ficheiro nao encontrado")

def copy_tmp(file):
    org = file
    if org == 'user\\':
        pass
    elif os.path.exists(org):
        x = file.split('.')
        y ="main" + "." + x[1]
        read = open( org , "r")
        dados = read.read()
        ficheiro = "user\\tmp\\" + y  
        abrir = open( ficheiro , "a")
        abrir.write(dados)
        print("O ficheiro ",file," foi copiado")
    else:
        print("ficheiro nao encontrado")

def tmp(file):
   
    
    if os.path.exists(file):
        read = open( file , "r")
        dados = read.read()
        ficheiro = "user\\apps\\tmp\\main.py"  
        abrir = open( ficheiro , "a")
        abrir.trucate(0)
        abrir.write(dados)
        print("O ficheiro ",file," foi copiado")
    else:
        print("ficheiro nao encontrado")


def copiar_dir():
    file = input("copiar ")
    dire = input("dir ")
    ex = "user\\" + file
    exes = "user\\"+ dire + "\\" + file
    xe = "user\\"+ dire
    print(ex," ",xe)
    if file == 'user\\' or dire == 'user':
        pass
    elif os.path.exists(ex) and os.path.isdir(xe):
        
        def mover_accao():
            org = "user\\" + file
            red = open( org , "r")
            dados = red.read()
            ficheiro = "user\\" + "\\" +  dire + "\\" + file 
            abrir = open( ficheiro , "a")
            colar_dados = abrir.write(dados)
            red.close()
            print("O ficheiro ",file," foi copiado para",dire)
    

        if os.path.exists(exes):
            org = "user\\" + file
            x = file.split('.')
            y = x[0] + "_copia" + "." + x[1]
            read = open( org , "r")
            dados = read.read()
            ficheiro = "user\\" + y  
            abrir = open( ficheiro , "a")
            colar_dados = abrir.write(dados)
            print("O ficheiro ",file," foi copiado")
        else:
             mover_accao()
    else:
        print("ficheiro nao encontrado")




def mover():
    name = input("mover ")
    file = input("mover de ")
    dire = input("para ")
    ex = "user\\" + file
    exes = "user\\"+ dire + "\\" + file
    xe = "user\\"+ dire
    print(ex," ",xe)
    if file == 'user\\' or dire == 'user' or name == 'user':
        pass
    
    elif os.path.exists(ex) and os.path.isdir(xe):
        
        def mover_accao():
            org = "user\\" + file + "\\" + name
            red = open( org , "r")
            dados = red.read()
            ficheiro = "user\\" +  dire + "\\" + name
            abrir = open( ficheiro , "a")
            colar_dados = abrir.write(dados)
            red.close()
            os.remove(org)
            print("O ficheiro ",name," foi movido para",dire)
    

        if os.path.exists(exes):
            print("O ficheiro ",file,"ja existe em ",dire)
            while True:
                r = input("Pretende mover mesmo assim? ")
                if r == "s" or r == "sim":
                    mover_accao()
                elif r == "n" or r == "nao":
                    print("O ficheiro nao foi movido")
                    break
                else:
                    print("Resposta invalida")
        else:
             mover_accao()
    else:
        print("ficheiro nao encontrado")

def mover_all():
    file = input("mover de ")
    dire = input("dir ")
    ex = "user\\" + file
    exes = "user\\"+ dire + "\\" + file
    xe = "user\\"+ dire
    print(ex," ",xe)
    if file == 'user\\' or dire == 'user':
        pass
    elif os.path.exists(ex) and os.path.isdir(xe):
        
        def mover_accao_all():
            lista = os.listdir(ex)
            for arq in lista:
                print(arq)
                org = "user\\" + file
                red = open( org , "r")
                dados = red.read()
                ficheiro = "user\\" + "\\" +  dire + "\\" + file 
                abrir = open( ficheiro , "a")
                colar_dados = abrir.write(dados)
                red.close()
                os.remove(org)
                print("O ficheiro ",file," foi movido para",dire)
    

        if os.path.exists(exes):
            print("O ficheiro ",file,"ja existe em ",dire)
            while True:
                r = input("Pretende mover mesmo assim? ")
                if r == "s" or r == "sim":
                    mover_accao_all()
                elif r == "n" or r == "nao":
                   break
                else:
                    print("Resposta invalida")
        else:
             mover_accao_all()
    else:
        print("ficheiro nao encontrado")

def conteudo():
    file = input("cont ")
    dire = input("para ")
    org = "user\\" + file
    ficheiro = "user\\" + dire
    if org == 'user\\' or ficheiro == 'user':
        pass
    elif os.path.exists(org) and os.path.exists(ficheiro):
        read = open( org , "r")
        dados = read.read()
        abrir = open( ficheiro , "a")
        colar_dados = abrir.write("\n",dados)
        print("O conteudo do ficheiro ",file," foi copiado para",dire)
    else:
        print("ficheiro nao encontrado")
    

def apagar_conteudo(org):
    if org == 'user\\':
        pass
    elif os.path.exists(org):
        re = open( org , "a")
        re.write("")
        arquivo.truncate(0)
        print("O conteudo do ficheiro de ",re," foi apagado")
    else:
        print("ficheiro nao encontrado")

def apagar_conteudo_dir(org):
    if org == 'user\\':
        pass
    elif os.path.isdir(org):
        lista = os.listdir(org)
        for arq in lista:
           
            re = open( org , "a")
            re.write("")
            arquivo.truncate(0)
            print("O conteudo do ficheiro de ",re," foi apagado")
    else:
        print("ficheiro nao encontrado")

def copiar_func(file,dire):
    print(file," ",dire)
    
    
    if os.path.exists(dr+file):
        if '.' in str(file):                                         
        
            org = dr+file
            red = open( org , "r")
            dados = red.read()
            ficheiro = "user\\" +  dire + "\\" + file 
            abrir = open( ficheiro , "a")
            colar_dados = abrir.write(dados)
            red.close()
            print("O ficheiro ",file," foi copiado para",dire)
    

        
            
    else:
        print("ficheiro nao encontrado")
        
def copiarf(file,dire):
    print(file," ",dire)
    
    
    if os.path.exists(file):
        if '.' in str(file):                                         
        
            org = file
            red = open( org , "r")
            dados = red.read()
            ficheiro =  dire + "\\" + file 
            abrir = open( ficheiro , "a")
            colar_dados = abrir.write(dados)
            red.close()
            print("O ficheiro ",file," foi copiado para",dire)
    

        
            
    else:
        print("ficheiro nao encontrado")
        
def movera():
    file = input("mover ")
    dire = input("para ")
    name = file.split('\\')[-1]
    print(name)
    ex = "user\\" + file
    exes = "user\\"+ dire + "\\" + file
    xe = "user\\"+ dire
    print(ex," ",xe)
    if file == 'user\\' or dire == 'user':
        pass
    
    elif os.path.exists(ex) and os.path.isdir(xe):
        
        def mover_accao():
            org = "user\\" + file 
            red = open( org , "r")
            dados = red.read()
            ficheiro = "user\\" +  dire + "\\" + name
            abrir = open( ficheiro , "a")
            colar_dados = abrir.write(dados)
            red.close()
            os.remove(org)
            print("O ficheiro ",name," foi movido para",dire)
    

        if os.path.exists(exes):
            print("O ficheiro ",file,"ja existe em ",dire)
            while True:
                r = input("Pretende mover mesmo assim? ")
                if r == "s" or r == "sim":
                    mover_accao()
                elif r == "n" or r == "nao":
                   break
                else:
                    print("Resposta invalida")
        else:
             mover_accao()
    else:
        print("ficheiro nao encontrado")



 

    
        

    
