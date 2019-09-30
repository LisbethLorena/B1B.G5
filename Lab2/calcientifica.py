from calculadora import calcul
import math
import numpy

class calcucientifica(calcul):
    def coseno(self, x):
        print("coseno de "+str(x)+" es: "+str(math.cos(x)))
    def seno(self, x):
        print("seno de "+str(x)+" es: "+str(math.sin(x)))
    def tangente(self, x):
        print("tangente de "+str(x)+" es: "+str(math.tan(x)))
    def sqrt(self, x):
        print("raiz cuadrada de "+str(x)+" es: "+str(math.sqrt(x)))
    def factorial(self, x):
        print("Factorial de "+str(x)+" es: "+str(math.factorial(x)))
    def sumavec(self, v1a, v2a):
        x=numpy.array([int(i) for i in v1a.split(",") if i.isdigit()])
        y=numpy.array([int(i) for i in v2a.split(",") if i.isdigit()])
        print("La suma es: "+str(x+y))
    def restavec(self, v1a, v2a):
        x=numpy.array([int(i) for i in v1a.split(",") if i.isdigit()])
        y=numpy.array([int(i) for i in v2a.split(",") if i.isdigit()])
        print("La resta es: "+str(x-y))
    def media(self, sa):
        x=numpy.array([int(i) for i in sa.split(",") if i.isdigit()])
        print("Media de "+str(x)+" es: "+str(numpy.mean(x)))
    
