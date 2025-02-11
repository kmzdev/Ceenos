import time

#Menu
print("---Calculadora de Dizimo---")
print("1-Calcular o Dízimo")
print("2-O que é dizimo")
print("3-Porque devemos tirar o dizimo")
print("4-Sair")

#opções
def main():

    res = input("Selecione uma opção:")

    if res == '1' :
        salario = input("Quanto você recebeu ou ganhou este mês?: ")#float(input("Quanto você recebeu ou ganhou este mês?:"))
        salario = int(salario)
       
        dizimo = float(salario) * 0.1
        print("O valor do seu dizimo é:", dizimo,"MT")
        time.sleep(5)

    elif res == '2':
        print("Dízimo é a décima parte de qualquer produto ou dinheiro que é o fruto de trabalho")
        time.sleep(5)

    elif res == '3':
        print("Leia Malaquias capítulo 3")
        time.sleep(5)

    elif res == '4':
        exit()
        time.sleep(5)
    elif res == '':
        main()
     
    else:
        print("opção inválida")
        #time.sleep(5)
        main()

main()        


         
    
