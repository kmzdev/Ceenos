import time

saldo = 5000

intel = {"nome" : "Intel Core I5","freq" : "2Ghz","preco" : 700}
pxram = {"geracao" : "DDR3","capacidade" : "2GB","preco" : 200}
hdrx = {"tipo" : "HD","capacidade" : "320GB","preco" : 500}
rtx= {"nome" : "AMD RTX","freq" : "2Ghz","preco" : 500}
	
	 
proc = 700
espa = 200
ram = 500





def montar_pc():
    
   saldo = 5000
    
   proce = input ("Escolha os processador:")
   if "1" == proce:
        process = "Intel"
        saldo = saldo - 2100
        print("ficou com",saldo,"pc")
   elif "2" == proce:
        process = "AMD" 
        saldo = saldo - 2000
        print("ficou com",saldo,"pc")
   elif "3" == proce:
        process ="Qualcomm" 
        saldo = saldo - 1200
        print("ficou com",saldo,"pc")
   else:
        print ("Opção invalida")
    
   print("O seu computador possui um",process)

   proce = input ("Escolha os placa grafica:")

   if "1" == proce:
        grafica = "AMD RTX"
        saldo = saldo - 1100
        print("ficou com",saldo,"pc")
   elif "2" == proce:
        grafica = "Nvidia GTX" 
        saldo = saldo - 1000
        print("ficou com",saldo,"pc")
   elif "3" == proce:
        grafica = "PROX GTX" 
        saldo = saldo - 1200
        print("ficou com",saldo,"pc")
   else:
        print ("Opção invalida")
    
   print("O seu computador possui:",grafica)

   proce = input ("Escolha uma memoria:")

   if "1" == proce:
        ram = "DDR2(4GB)"
        saldo = saldo - 200
        print("ficou com",saldo,"pc")
   elif "2" == proce:
        ram = "DDR3(8GB)" 
        saldo = saldo - 500
        print("ficou com",saldo,"pc")
   elif "3" == proce:
        ram = "DDR4(8GB)" 
        saldo = saldo - 700
        print("ficou com",saldo,"pc")
   elif "4" == proce:
        ram = "RamPROX(16GB)" 
        saldo = saldo - 900
        print("ficou com",saldo,"pc")
   else:
        print ("Opção invalida")
    
   print("Comprou",ram)


   proce = input ("Escolha a unidade de armazenamento:")

   if "1" == proce:
        armazen = "HD(500GB)"
        saldo = saldo - 900
        print("ficou com",saldo,"pc")
   elif "2" == proce:
        if saldo == 900:
            print("saldo insuficiente")
        else:
            armazen = "SSD(200GB)" 
            saldo = saldo - 1000
            print("ficou com",saldo,"pc")
   elif "3" == proce:
         if saldo == 900:
            print("saldo insuficiente")
         else:
            armazen = "SSD NVMe(500GB)" 
            saldo = saldo - 1200
            print("ficou com",saldo,"pc")
   else:
        print ("Opção invalida")
    
   print("Comprou",armazen)

   montar = input ("Montar computador?:")

   if montar == "sim":
        print ("Montado...")
        time.sleep(4)
        print ("Computador montado")
        print ("O seu computador esta equipado com um processador:",process,",uma memoria ram:",ram,",uma unidade de armazenamento:",armazen,"uma placa grafica:",grafica)
        if saldo <= 200:
            print ("É um PC de alta performance")
        elif  saldo  <=500:
            print ("É um PC de media performance")
        elif saldo  <= 700:
            print ("É um PC de baixa performance")    
        print ("O seu saldo é:",saldo,"pc")
        

   elif montar == "nao":
        print ("Vendendo peças...")
        time.sleep(4)
        exec(montar_pc())  
   exit ()

print ("Bem vindo ao PC builder")
print ("Você tem 5000 pc na conta,compre componentes e monte um pc")
print  ("Loja:")
print ("Processadores: Intel(2100pc),AMD(2000pc),Qualcomm(1200pc)")
print ("Placa Grafica: AMD RTX(1000pc),NVIDIA GTX (1000pc),PROX GTX(1200pc)")
print ("Memorias: DDR2(200pc),DDR3(500pc),DDR4(700pc),RamPROX(900pc)")
print ("Armazenamento: HD(900pc),SSD(1000pc),SSD+(1200pc)")
  
montar_pc()

print ("O seu computador esta equipado com um processador:",process,",uma memoria ram:",ram,",uma unidade de armazenamento:",armazen,"uma placa grafica:",grafica)
if saldo <= 200:
    print ("É um PC de alta performance")
elif  saldo  <=500:
    print ("É um PC de media performance")
elif saldo  <= 700:
    print ("É um PC de baixa performance")
    
print ("O seu saldo é:",saldo,"pc")


    

    

