#Claro! Segue um exemplo de um visualizador e editor de arquivos de texto em linha de comando em Python com menu:
import subprocess
import os

dr = 'C:\\ceenos\\user\\'

def exibir_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            conteudo = arquivo.read()
            print(conteudo)
    except FileNotFoundError:
        print("Arquivo não encontrado.")

def editar_arquivo(nome_arquivo):
    print("Digite 'editor-sair' para sair do editor")
    line = 0
    try:
        while True:
            line += 1
            with open(nome_arquivo, 'a') as arquivo:
                conteudo = input(str(line)+"-")
                if conteudo != 'editor-sair':
                    arquivo.write(conteudo+'\n')
                else:
                    break
            #print("Conteúdo adicionado com sucesso.")
    except FileNotFoundError:
        print("Arquivo não encontrado.")

def menu():
    print("===== MENU =====")
    print("1. Exibir arquivo")
    print("2. Editar arquivo")
    print("3. Sair")

    opcao = input("Escolha uma opção: ")
    return opcao

def visualizador_editor():
    nome = input("Digite o nome do arquivo: ")
    nome_arquivo = dr + nome
    #print(nome_arquivo)

    if not os.path.isfile(nome_arquivo):
        print("Arquivo não encontrado.")
        return

    while True:
        opcao = menu()

        if opcao == '1':
            exibir_arquivo(nome_arquivo)
        elif opcao == '2':
            editar_arquivo(nome_arquivo)
        elif opcao == '3':
            print("Saindo do programa...")
            break
            #subprocess.run(['python', 'kernel.py'])
        else:
            print("Opção inválida. Tente novamente.")

visualizador_editor()
