#!/usr/bin/env python

def Cuadratica(x):
    return 1/(1+x**2)

def Riemann(extInf,extSup,rect,imagenFunc):

    subIntervalo = (extSup-extInf)/rect #Se realiza una partición del intervalo total en "rect" rectángulos
    suma = 0.0 #El contador donde se dará el resultado
    for cont in range(rect): #Iterar sobre todos los rectángulos
        puntoMedio = subIntervalo/2+subIntervalo*cont #El punto medio, con un cambio de "subIntervalo" en cada iteración
        suma += imagenFunc(puntoMedio)*subIntervalo #Área: Base por altura del rectángulo
    return suma

n = int(input("Rectángulos: "))
print(4*Riemann(0,1,n,Cuadratica)) #Imprime el valor de la integral*4, para aproximar pi
        
