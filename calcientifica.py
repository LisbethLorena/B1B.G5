from calculadora import calcul
import math

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
