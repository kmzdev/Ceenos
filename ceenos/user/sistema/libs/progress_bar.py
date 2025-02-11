""" this module aloud you to craete progress bar whit personalized configuration
    such as icon,time to wait,unity to craete per second,and the limit of unitys and text """

import time
import os 

def bar(icon,wait,unity,limit,text):
    tm = 0
    per = 1
    progress = ""

    while tm != limit:
        
        tm += 1
        per += unity
        f = str(per)
        c = f.split(".")
    
        progress += icon 
        #os.system("cls")
        print(text,c[0],"%")
        print(progress)
        time.sleep(wait)

def pb(text):
    tm = 0
    per = 1
    progress = ""
    #print('Processando...')

    while tm != 32:
        
        tm += 1
        per += 3.1
        f = str(per)
        c = f.split(".")
    
        progress += "#"
        #os.system("cls")
        print(text,c[0],"%",progress,end='\r')
        #print(progress)
        time.sleep(0.25)

        
def default():
    tm = 0
    per = 1
    progress = ""
   # print('Processando...')
    while tm != 32:
        
        tm += 1
        per += 3.1
        f = str(per)
        c = f.split(".")
    
        progress += "#"
        #os.system("cls")
        print("Processando",c[0],"%",progress,end='\r')
        #print(progress)
        time.sleep(0.25)


def timer(timing):
    tm = 0
    per = 1
    progress = ""
    #print('Processando...')
    while tm != 32:
        
        tm += 1
        per += 3.1
        f = str(per)
        c = f.split(".")
    
        progress += "#"
        #os.system("cls")
        print("Processando",c[0],"%",progress,end='\r')
        #print(progress)
        time.sleep(timing)

        
def text(tex):
    tm = 0
    per = 1
    progress = ""
    #print('Processando...')
    while tm != 32:
        anim = ['|','/','-','\\','|','/','-','\\']
        tm += 1
        per += 3.1
        f = str(per)
        c = f.split(".")
    
        progress += "#"
        #os.system("cls")
        for i in anim:
           print(tex,i,c[0],'%',end='\r')
           time.sleep(0.05)
            
        #print("Processando",c[0],"%",progress,end='\r')
        #rint(progress)
        #time.sleep(timing)
 
 
""" to create progress bar you can use the user defined function : bar("ðŸš¾",0.5,1,7,wait to bathroom) or default() for default configuration """

