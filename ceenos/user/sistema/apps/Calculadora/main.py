#Aqui está um exemplo de uma calculadora de linha de comando em Python com um menu:
import subprocess

def soma():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 + num2
    print("A soma é", resultado)

def subtracao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 - num2
    print("A subtração é", resultado)

def multiplicacao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 * num2
    print("A multiplicação é", resultado)

def divisao():
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 / num2
    print("A divisão é", resultado)

def menu():
    print("Selecione a operação:")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        soma()
    elif opcao == 2:
        subtracao()
    elif opcao == 3:
        multiplicacao()
    elif opcao == 4:
        divisao()
    elif opcao == 0:
        subprocess.run(['python', 'kernel.py'])
    else:
        print("Opção inválida. Por favor, tente novamente.")

while True:
    menu()

