import sys
sys.path.insert(0,'C:\\ceenos\\user\\sistema\\libs')
import recopy
import subprocess
import os
import time
import getpass
import shutil
import progress_bar as pb
import math

dr_universal = 'user\\sistema\\ficheiros do sistema\\'
dr_user = 'C:\\ceenos\\user\\'
atual_dir = 'C:\\ceenos\\'

if os.path.exists(dr_universal+'usuarios.txt'):
    os_n = open(dr_universal+"usuarios.txt", "r")
    n = os_n.read()
    os_n.close()
    v = n.split(":")
    name = v[0]
    osx = open(dr_universal+"os_v.txt","r")
    osx_v = osx.read()
    osx.close()

else:
    with open (dr_universal+"usuarios.txt","a") as arquivo:
        lk = arquivo.write("")

    

global clear_screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Kernel:    
    clear_screen()

    def read_content(self,fill):
        file = fill.split('ler ')[1]
        #file = input("ler ")
        ficheiro = "user\\" + file
        if file == '':
            pass
        elif os.path.exists(ficheiro):
            abrir = open( ficheiro , "r")
            texto = abrir.read()
            abrir.close()
            print(ficheiro,'\n','\n')
            print(texto)
       
        else:
            print("ficheiro não encontrado")
	    
    def write_content(self,fill):
        file = fill.split('escrever ')[1]
        fe = input(" ")
        ficheiro = "user\\" + file
        if file == '':
            pass
        elif 'user\\sistema' in ficheiro:
            print("Nao e possivel escrever em ficheiros do sistema")
        elif os.path.exists(ficheiro):
            abrir = open( ficheiro , "w")
            abrir.write(fe)
            abrir.close()
            #print(ficheiro,'\n','\n')
            #print(texto)
       
        else:
            print("ficheiro não encontrado")

    def obter(self,obj):
        print('Obtendo ficheiro da rede...')
        #pb.default()
        pb.text('fazendo download')
        print('\nO ficheiro '+obj.replace('obter','')+' foi baixado')
        

    def lista(self,fill):
        file = fill.split('ls ')[1]
        #file = input("list ")
        ficheiro = "user\\" + file
        if file.startswith("sistema"):
            
            print("Nao e possivel acessar a sistema")              
        elif os.path.exists(ficheiro):
            lista = os.listdir(ficheiro)
            for arq in lista:
                print(arq)
        elif file == 'user':
            ficheiro = "user\\"
            lista = os.listdir(ficheiro)
            for arq in lista:
                print(arq)
    
       
            
#        elif 'sistema' in ficheiro:
#           print("Nao e possivel acessar a sistema\\")
            
        elif file == " ":
            print("Insira um directório")

        else:
            print("directório não encontrado")

    def app(self,fill):
        file = fill.split('executar ')[1]
        #file = input("Insira o nome da app: ")
        ficheiro = "user\\sistema\\apps\\" + file + "\\main.py"
        aps = "user\\sistema\\apps\\jogos\\" + file + "\\main.py"
        if os.path.exists(ficheiro):
            with open(ficheiro,'r') as cdz:
                codew = cdz.read()
                cdz.close()
                try:

                    #exec(codew)
                    subprocess.run(['python',ficheiro])
#If an error occurs, it will be caught by the except block*
                    pass  # Replace 'pass' with your actual code
                except Exception as e:

                    print("Ops!...ocoreu um erro no sistema -> ", e)
                    with open(dr_universal+'relatorio.dr','a') as dvr:
                        rel = time.strftime('%d/%m/%Y %H:%M:%S') + ' -> ' + str(e) +'\n'
                        dvr.write(rel)
                        dvr.close()
                    print("O relatorio do erros serao guardados!")
                    kernel.main()
                
            #subprocess.Popen(['python3',ficheiro])
            #exec(ficheiro)
        # elif os.path.exists(aps):
            # #exec(aps)
            # #exec(open(aps).read())
            # with open(aps,'r') as cdz:
                # codey = cdz.read()
                # cdz.close()
                # exec(codey)
    
        elif file == "":
            print("Insira o nome da aplicaçao")
        else:
            print("Aplicaçao não encontrada")# \n Ou ficheiro main inexistente")

    def config(self):
        print("==================================")
        print("           Configurações          ")
        print("==================================")
        print("Comandos disponíveis:")
        print("1- Remover palavra-passe na tela de login")
        print("#2- Restaurar os sistema")
        print("3- Fazer cópia de sistema")
        print("#4- Reinstalar o sistema")
        print("#5- Ativar o sitema")
        print("#6- Apagar conteúdo na tela a cada comando")
        print("#7- Ativar inicialização rápida")
        print("#8- Ativar calculo a partir da linha de comando")
        print("9- Ativar modo desenvolvedor beta(instável)")
        print("10- Atualizar")
        print("11- Ver relatorio de erros")
     
        choice = input("Escolha uma opção: ")
        if choice == '1':
            with open(dr_universal+'slogin.txt','r') as slg:
                slgt = slg.read()
                slg.close()
            if slgt == 'login=False':
                print('Palavra-passe ja foi removida')
                print('\r'+'Digite "uss" para adicionar uma palavra-passe')
            else:
                x = input('Tem a certza que quer remover a palavra-passe?[s/n]:')
                if x == 's':
                    with open(dr_universal+'slogin.txt','a') as slg:
                    #slg.truncate(0)
                        slg.write('login=False')
                        slg.close()

                    print('Palavra-passe removida!')
                else:
                    pass
        elif choice == '3':
            print('Fazendo copia do ficheiros...')
            
            lista = os.listdir('user\\')
            for arq in lista:
                #print(arq)
                pb.text('A copiar')
                recopy.copiar_func(arq,'sistema\\ficheiros do sistema\\copia-do-sistema\\')
                
            print('\nO seu sistema foi copiado com sucesso!')
            
                
        elif choice == '9':
            with open(dr_universal+'sdev.txt','r') as slg:
                slgt = slg.read()
                slg.close()
            if 'dev=True' in slgt:
                with open(dr_universal+'sdev.txt','a') as slg:
                    
                    slg.write('dev=False')
                    slg.close()
                print('Modo de desenvolvedor desativado!')
               
            else:
            
                with open(dr_universal+'sdv.txt','a') as slg:
                   
                    slg.write('dev=True')
                    slg.close()
                print('Modo de desenvolvedor ativado!')
        elif choice == '10':
            print('Obtendo ataulizaçao da rede...')
            pb.default()
            print('\nA versao mais recente do CeenosOS foi baixada com sucesso!')
            time.sleep(5)
            clear_screen()
            print('A atualizar...')
            pb.text('A preparar o sistema')
            print('\nO sistema foi atualizado com sucesso para a versao mais recente do CeenosOS!')
            print('Disfrute!!!')
            print('O sistema vai ser reniciado!')
            time.sleep(5)
            kernel.restart()
                
        elif choice == '11':
            with open(dr_universal+'relatorio.dr','r') as dvr:
                print(dvr.read())
                dvr.close()             
        else:
            print('Indesponivel')
            
    def exdir(self,command):
        ds = dr_user + command.replace('ex-dir ','')
        if 'sistema' in ds:
            print("Nao e possivel remover a sistema\\")
        elif os.path.isdir(ds):
            fic = os.listdir(ds)
            for i in fic:
                filed =  ds + '/' + i     
                os.remove(filed)
                print('-> O ficheiro',i,'foi removido')
            os.rmdir(ds)
            print('O Directorio ',command.replace('ex-dir ',''),' foi removido!')
        else:
            print('Directorio ',command.replace('ex-dir ',''),' nao achado!')

    def cdir(self,command):
        ds = dr_user + command.replace('cr-dir ','')
        if os.path.isdir(ds):
            print('O directorio ',command.replace('cr-dir ',''),' ja existe!')
        elif 'user\\sistema' in ds:
            print("Nao e possivel criar directorios no sistema")
        else:
            os.mkdir(ds)
            print('Directorio ',command.replace('cr-dir ',''),' foi criado!')
                    
    def apps(self):
       
        ficheiro = "user\\sistema\\apps\\"
        jogos = "user\\sistema\\apps\\jogos\\"
        if os.path.exists(ficheiro):
            lista = os.listdir(ficheiro)
            for arq in lista:
                if arq == 'jogos':
                    pass
                else:
                    print(arq)
            lis = os.listdir(jogos)
            for arq in lis:
                if arq == 'py_cache':
                    pass
                else:
                    print(arq)
        
    
        else:
            print("Directório de apps não encontrado")


    def remove_file(self,fill):
        file = fill.split('ex-fi ')[1]
        ficheiro = "user\\" + file
        if ficheiro == "user\\":
            print("ficheiro não encontrado")
        elif 'user\\sistema' in ficheiro:
            print("Nao e possivel remover ficheiros do sistema")
        elif os.path.exists(ficheiro):
            os.remove(ficheiro)
            print("O ficheiro",file,"foi removido")
        else:
            print("ficheiro não encontrado")

    def create_file(self,fill):
        file = fill.split('criar ')[1]
        ficheiro = "user\\" + file
        if file == '':
            ficheiro == 'user\\'
        elif 'user\\sistema' in ficheiro:
            print("Nao e possivel criar ficheiros no sistema")
        else:
            abrir = open( ficheiro , "a")
            print("O ficheiro ",file," foi criado")

    def rename_file(self,fill):
        file = fill.split('re ')[1]
        ficheiro = "user\\" + file
        if 'user\\sistema' in ficheiro:
            print("Nao e possivel renomear ficheiros do sistema")
        elif os.path.exists(ficheiro):
            novo_nome = input("Novo nome: ")
            nv = "user\\" + novo_nome
            os.rename(ficheiro,nv)
            print("O ficheiro ",file," foi renomeado para ",novo_nome)
        
        else:
            print("ficheiro não encontrado")
    
    def info(self):
        
        with open(dr_universal+'cpu.txt') as fi:#'encoding='UTF-8'
            cpu= fi.readlines()
        with open(dr_universal+'ram.txt') as fo:#'encoding='UTF-8'
            ram = fo.readlines()
        with open(dr_universal+'arm.txt') as fp:#'encoding='UTF-8'
            arm= fp.readlines()
        with open(dr_universal+'pv.txt') as fd:#'encoding='UTF-8'
            pv= fd.readlines()
        with open(dr_universal+'arq.txt') as fs:#'encoding='UTF-8'
            arq= fs.readlines()
        with open(dr_universal+'fq.txt') as ff:#'encoding='UTF-8'
            fq= ff.readlines()
            
            #ram = dd[12]
            #arm = dd[17]
            #cpu = dd[2]
            #pv = dd[18]
            #fq = dd[6] #1073741824
            #arq = dd[20]
            
        spa = str(int(arm[2].replace('\x00','')) / 1073741824).split('.')[0]
        rm = int(ram[2].replace('\x00','')) / 1073741824
        hz = int(fq[2].replace('\x00','')) / 1000

        print("----INFO----")
        print("Usuario:",name)
        print("SO:",osx_v)
        print("------------")
        print("RAM:",rm,'GB')
        print("Armazenamento:",spa,'GB')
        print("Processador:",cpu[2].replace('\x00','').replace('\n',''))
        print("Frequência:",hz,'GHz')
        print("Arquitetura do SO:",arq[2].replace('\x00','').replace('\n',''))
        print("Placa de video:",pv[2].replace('\x00','').replace('\n',''))
        print("------------")
        print("Fabricante:",arq[10].replace('\x00','').replace('\n',''))
        print("Modelo:",arq[6].replace('\x00','').replace('\n',''))
        print("Tipo:",arq[14].replace('\x00','').replace('\n','').split('-')[0])
        print("------------")
        print('Desenvolvedor: <@Klit Zets>')
        
         
    
    def restart(self):
        x = input('Tem a certza que quer reniciar?[s/n]:')
        if x == 's':
            clear_screen()
            print('Reniciando...')
            time.sleep(5)
            #os.startfile('kernel.py')
            subprocess.run(['python','kernel.py'])
            exit()
            #boot.boot_process()
            #exit()
        else:
            pass
            
    def calc(self,expre):
        #expre = input('> ')
        expre = expre.replace('calc ','')
        #print(expre)
        try:
            print(eval(expre))
        except Exception:
            #or (ZeroDivisionError) or (TypeError) or (ValueError):
            print("Operação não pode ser realizada")
        
    def historico(self):
        with open(dr_universal+"historico.txt", "r") as arquivo:
            histo = arquivo.read()
            print(histo)

    def dv_exit(self):
        x = input('Tem a certza que quer sair?[s/n]:')
        if x == 's':
            clear_screen()
            print('A encerrar...')
            with open(dr_universal+"historico.txt", "w") as arquivo:
                #arquivo.write("")
                arquivo.truncate(0)
            time.sleep(5)
            exit()
        else:
            pass
        
    def uss(self):
        nome = input("Introduza o novo nome:")
        senha = input("Introduza a nova senha:")
        with open(dr_universal+"usuarios.txt", "a") as arq:
            arq.truncate(0)
            arq.write(f"{nome}:{senha}")
            arq.close()
        with open(dr_universal+"usuario.txt", "a") as arq:
            arq.truncate(0)
            arq.write(f"{nome}")
            arq.close()
        with open(dr_universal+'slogin.txt','w') as slg:
                    slg.truncate(0)
                    slg.write('login=True')
                    arq.close()
        #clear_screen()
        #print('Reniciando...')
        #time.sleep(5)
        #boot.boot_process()
            
    def draw_terminal(self):
        clear_screen()
        print("===================================")
        print("          CeenosOS             ")
        print("===================================")
        print("Digite 'ajuda' para obter ajuda")

    
    def instalador(self,fill):
        main = fill.split('instalador ')[1]
        hv = "user\\" + main + '_copia.py'
        appdir = "user\\sistema\\apps\\" + main
        ficheiro = "user\\" + main + '.py'
        shutil.copy(ficheiro,hv)
        if os.path.isdir(appdir):
                print('Essa aplicaçao ja esta instalada')
                f = input('Deseja instalar ela novamente, os seus dados serão perdidos[s ou n]: ')
                if f == 's':
                    os.remove(appdir)
                    pass
                else:
                    exit()
                
        print(ficheiro)
        if os.path.exists(ficheiro):
            os.mkdir(appdir)
            novo_dir = "user\\sistema\\apps\\" + main
            print(novo_dir)
            shutil.move(ficheiro,novo_dir)
            print(ficheiro)
            fileapp = "user\\sistema\\apps\\" + main + "\\" + "main.py"
            app = "user\\sistema\\apps\\" + main + "\\" + main + ".py"
            os.rename(app,fileapp)
            os.rename(hv,ficheiro)
            
            print("A aplica?",main,"foi instalada com sucesso!")
        else:
            print("Instalador não encontrada")
			


    def show_help(self):
        #clear_screen()
        print("======================")
        print("         Ajuda        ")
        print("======================")
        print("Comandos disponíveis:")
        print("- ajuda: Exibe esta mensagem de ajuda")
        print("- limpar: Limpa a tela")
        print("- tempo: Exibe a data e hora atuais")
        print("- sair: Sai do sistema")
        print("- gerc: Abrir Gerenciador de arquivos")
        print("- calc: executar calculos")
        print("- reniciar: Reniciar o sistema ")
        print("- editor: Abrir o editor de texto ")
        print("- script: Executar scripts específicos")
        print("- apps: Exibe as Apps instaladas")
        print("- executar: Executar aplicações")
        print("- info:Exibe as informações do pc e do usuário")
        print("- uss: Mudar o nome do usuário e senha")
        print("- comp: compilar scripts")
        print("- ler: ler conteúdo de ficheiros")
        print("- cr: criar arquivo vazio")
        print("- cr-dir: criar novo directório")
        print("- ex-dir: apagar directório")
        print("- ex-fi: apagar ficheiro")
        print("- obter: obter ficheiros da rede")
        print("- mov-dir: mover ficheiros de um diretório")
        print("- mov: mover ficheiros de um diretório")
        print("- cp: copiar um ficheiro")
        print("- cp-dir: copiar um ficheiro para outro directório")
        print("- ct: copiar conteudo de um ficheiro para outro")
        print("- ex-fi-ct: apagar conteúdo de um ficheiro")
        print("- ex-dir-ct: apagar conteúdo de um diretório")
        print("- re: renomear um ficheiro ou diretório")
        print("- ls: mostrar ficheiros de um diretório")
        print("- ins: instalar aplicações")
        print("- historico: ver histórico de comandos")
        
    def run(self,app):
        subprocess.run(['python', app])
        # with open(app) as ap:
                # code = ap.read()
                # exec(code)
        
    

    def show_current_time(self):
        #clear_screen()
        #print("======================")
        #print("      Data e Hora     ")
        #print("======================")
        print(time.strftime('%d/%m/%Y %H:%M:%S'))
    
      
    def main(self):
        #kernel.draw_terminal()

        while True:
            #command = input("\nDigite um comando: ")
            #command = input('@user-'+name+'>')
            #command = input(name+'@user-dvos>')
            #time.sleep(1)
            command = input('\r'+time.strftime('%d/%m/%Y %H:%M:%S ')+name+'@user\\>')

            with open(dr_universal+"historico.txt", "a") as arquivo:
                arquivo.write(f"{command}\n")
        
            palavras  = command.split()
                
            if command.lower().startswith('ajuda'):
                kernel.show_help()
            elif command.lower().startswith('calc '):
                kernel.calc(command)
            elif command.lower().startswith('historico'):
                kernel.historico()
            elif command.lower().startswith('limpar'):
                kernel.draw_terminal()
            elif command.lower().startswith('tempo'):
                kernel.show_current_time()
            elif command.lower().startswith('sair'):
                kernel.dv_exit()
            elif command.lower().startswith('apps'):
                kernel.apps()
            elif command.lower().startswith('gerc'):
                subprocess.run(['python', 'user\\sistema\\apps\\Gerenciador de arquivos\\main.py'])
            elif command.lower().startswith('calc '):
                subprocess.run(['python', 'calc.py'])
            elif command.lower().startswith('reniciar'):
                kernel.restart()
            elif command.lower().startswith('ler '):
                kernel.read_content(command)
            elif command.lower().startswith('escrever '):
                kernel.write_content(command)
            elif command.lower().startswith('ls '):
                kernel.lista(command)
            elif command.lower().startswith('editor'):
                kernel.run('user\\sistema\\apps\\Editor de texto\\main.py')   
            elif command.lower().startswith('script '):
                subprocess.run(['python', 'lm.py'])
            elif  command.lower().startswith('executar '):
                kernel.app(command)
            elif command.lower().startswith('script '):
                subprocess.run(['python', 'dbrun.py'])
            elif command.lower().startswith('app in prg '):
                subprocess.run(['python', 'dv32runPrg.py'])
            elif command.lower().startswith('comp '):
                subprocess.run(['python', 'compiler.py'])
            elif command.lower().startswith('info'):
                kernel.info()
            elif command.lower().startswith('uss'):
                kernel.uss()
            elif command.lower().startswith('config'):
                kernel.config()
            elif command.lower().startswith('cp '):
                recopy.copiar(command) 
            elif command.lower().startswith('cp-dir '):
                recopy.copiar_dir()
            elif command.lower().startswith('mov-dir '):
                recopy.copiar_dir()
            elif command.lower().startswith('excp '):
                recopy.apagar_conteudo(command)
            elif command.lower().startswith('mov'):
                recopy.movera()
            elif command.lower().startswith('ex-fi-ct '):
                recopy.apagar_conteudo(command)
            elif command.lower().startswith('cp-ct-fi '):
                recopy.conteudo(command)
            elif command.lower().startswith('ex-fi '):
                kernel.remove_file(command)
            elif command.lower().startswith('ex-dir '):
                kernel.exdir(command)
            elif command.lower().startswith('cr '):
                kernel.create_file(command)
            elif command.lower().startswith('cr-dir '):
                kernel.cdir(command)
            elif command.lower().startswith('ins '):
                kernel.instalador(command)
            elif command.lower().startswith('re '):
                kernel.rename_file(command)
            elif command.lower().startswith('ex-dir-ct '):
                recopy.apagar_conteudo_dir(command)
            elif command.lower().startswith('obter '):
                kernel.obter(command)
            else:
                #print(command)
                try:
                    eval(command) + 0
                    print(eval(command))
                except Exception:
                    #print("Operação não pode ser realizada")
                    print("Comando inválido. Digite 'ajuda' para obter ajuda.")
        
           

kernel = Kernel()

class Login:
    
    clear_screen()

    def log(self):
        with open (dr_universal+"usuarios.txt","r") as arquivo:
            lk = arquivo.read()
            arquivo.close()
        
        if lk == "":
            login.cadastrar_usuario()
        else:
            login.fazer_login()

    def cadastrar_usuario(self):
        print('---------Cadastro---------')
        nome = input("Digite seu nome: ")
        senha = getpass.getpass("Digite sua senha: ")

        with open(dr_universal+"usuarios.txt", "a") as arquivo:
            arquivo.truncate(0)
            arquivo.write(f"{nome}:{senha}\n")
            arquivo.close()
        with open(dr_universal+"usuario.txt", "a") as arquivo:
            arquivo.write(f"{nome}")
            arquivo.close()

        print("Usuário cadastrado com sucesso!")
        kernel.draw_terminal()
        kernel.main()

    def fazer_login(self):
        print('--------Login---------')
        nome = input("Digite seu nome: ")
        senha = getpass.getpass("Digite sua senha: ")

        with open(dr_universal+"usuarios.txt", "r") as arquivo:
            for linha in arquivo:
                usuario, senha_guardada = linha.strip().split(":")
                if usuario == nome and senha == senha_guardada:
                    print("Login bem-sucedido!")
                    #time.sleep(3)
                    clear_screen()
                    kernel.draw_terminal()
                    kernel.main()
                    return
                elif senha == 'SUDO':
                    kernel.uss()
                    
        clear_screen()
        print("===================================")
        print("             CeenosOS              ")
        print("===================================")
        print("Nome de usuário ou senha incorretos.")
        login.fazer_login()

    def main_login(self):
        while True:
            print("--- Menu ---")
            print("1 - Login")
            print("2 - Criar conta")
            print("3 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                login.fazer_login()
            elif opcao == "2":
                login.cadastrar_usuario()
            elif opcao == "3":
                break
            else:
                print("Opção inválida. Tente novamente.")

login = Login()

class Boot:
    def boot_process(self):
        
        os.startfile(dr_universal+'especs.cmd')
        time.sleep(2)
        
        #os.remove('user\\sistema\\ficheiros do sistema\\cpu.txt')
        recopy.copiarf('cpu.txt','user\\sistema\\ficheiros do sistema\\')
        os.remove('cpu.txt')

        #os.remove('user\\sistema\\ficheiros do sistema\\fq.txt')
        recopy.copiarf('fq.txt','user\\sistema\\ficheiros do sistema\\')
        os.remove(atual_dir+'fq.txt')

        #os.remove('user\\sistema\\ficheiros do sistema\\ram.txt')
        recopy.copiarf('ram.txt','user\\sistema\\ficheiros do sistema\\')
        os.remove(atual_dir+'ram.txt')

        #os.remove('user\\sistema\\ficheiros do sistema\\arm.txt')
        recopy.copiarf('arm.txt','user\\sistema\\ficheiros do sistema\\')
        os.remove(atual_dir+'arm.txt')

        #os.remove('user\\sistema\\ficheiros do sistema\\pv.txt')
        recopy.copiarf('pv.txt','user\\sistema\\ficheiros do sistema\\')
        os.remove(atual_dir+'pv.txt')

        #os.remove('user\\sistema\\ficheiros do sistema\\arq.txt')
        recopy.copiarf('arq.txt','user\\sistema\\ficheiros do sistema\\')
        os.remove(atual_dir+'arq.txt')
        
        clear_screen()
        print("\r\rIniciando o processo de boot...")
        #time.sleep(2)
        print("Inicializando hardware...")
        #time.sleep(2)
        print("Verificando memória...")
        #time.sleep(2)
        print("Carregando sistema operacional...")
        time.sleep(2)
        clear_screen()
        #pb.pb('Carregando')
        clear_screen()
        print("Pronto!")
        time.sleep(1)
        clear_screen()
	
        print("===================================")
        print("             CeenosOS              ")
        print("===================================")
        print("Bem-vindo!")
        time.sleep(2)
        with open(dr_universal+'slogin.txt','r') as slg:
            slgt = slg.readlines()
            slg.close()
        if 'login=True' in slgt:
            login.log()
        else:
            kernel.draw_terminal()
            kernel.main()



boot = Boot()
#kernel.calc()
#kernel.main()
#boot.boot_process()

while True:
    try:
#Your main code goes here*
        boot.boot_process()
        #kernel.main()
#If an error occurs, it will be caught by the except block*
        pass  # Replace 'pass' with your actual code
    except Exception as e:
        #clear_screen()
        print("Ops!...ocoreu um erro no sistema -> ", e)
        with open(dr_universal+'relatorio.dr','a') as dvr:
            rel = time.strftime('%d/%m/%Y %H:%M:%S') + ' -> ' + str(e) + '\n'
            dvr.write(rel)
            dvr.close()
        time.sleep(2)
        #print("Reniciando os sistema...")
        print("O relatorio do erros sera guardado!")
        kernel.main()
        




