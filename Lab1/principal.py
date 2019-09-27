from calcientifica import calcucientifica
import numpy
calc=calcucientifica()

def menu():
    print ("calculadora cientifica")
    print ("seleccionar opcion")
    print ("1-suma")
    print ("2-resta")
    print ("3-multiplicacion")
    print ("4-division")
    print ("5-coseno")
    print ("6-seno")
    print ("7-tangente")
    print ("8-Raiz cuadrada")
    print ("9-Factorial")
    print ("10-Media")
    print ("0-salir")
    return int(input("introducir opcion: "))
while(True):
    operacion = menu()

    if(operacion==0):
        break
    elif(operacion==5):
        x=float(input("ingresar numero: "))
        calc.coseno(x)
    elif(operacion==6):
        x=float(input("ingresar numero: "))
        calc.seno(x)
    elif(operacion==7):
        x=float(input("ingresar numero: "))
        calc.tangente(x) 
    elif(operacion==8):
        x=float(input("ingresar numero: "))
        calc.sqrt(x)
    elif(operacion==9):
        x=float(input("ingresar numero: "))
        calc.factorial(x)
    elif(operacion==10):
        s=input("ingresar vector: ")#float(input("ingresar vector: "))
        sa=s[1:-1]
        x=numpy.array([int(i) for i in sa.split(",") if i.isdigit()])
        calc.media(x)
	    
    else:
        x=float(input("ingresar numero: "))
        y=float(input("ingresar numero: "))

        if(operacion==1):
            calc.suma(x,y)
        elif(operacion==2):
            calc.resta(x,y)
        elif(operacion==3):
            calc.multiplicacion(x,y)
        elif(operacion==4):
            calc.division(x,y)  
        else:
            print ("opcion invalida")
            
            
