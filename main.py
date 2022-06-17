import random
from math import e
import time
import matplotlib.pyplot as plt
import statistics
from numpy import var
#Se eligen dos numeros aleatorios entre 0 y la cantidad de locales para luego
#hacer un swap dentro de las posiciones del vector para generar el vecino
def generarVecino(cantidadLocales):
    numeroRandomA = random.randrange(cantidadLocales)
    numeroRandomB = numeroRandomA
    while(numeroRandomB == numeroRandomA):
        numeroRandomB = random.randrange(cantidadLocales)
    aux = vecino[numeroRandomA]
    vecino[numeroRandomA] = vecino[numeroRandomB]
    vecino[numeroRandomB] = aux
    return
    
#Se lee el archivo txt y se consigue tanto la matriz de flujo , como los espacios
#de cada local , tambien la cantidad total de locales
def llenarVectorYMatriz(nombre):
  archivoInstancia = open(nombre)
  lineaLeer = archivoInstancia.readline().strip().split(",")
  cantidadLocales = int(lineaLeer[0])

  lineaLeer = archivoInstancia.readline().strip().split(",")
  for x in lineaLeer:
    espacioLocales.append(int(x))

  for x in range(0,cantidadLocales):
    lineaLeer = archivoInstancia.readline().strip().split(",")
    for j in range(0,cantidadLocales):
      lineaLeer[j] = int(lineaLeer[j])
    matrizClientes.append(lineaLeer)
  return cantidadLocales

def calcularDistanciaEntrePuestos(primeraPos, segundaPos,vector):
  distancia = 0.0
  for i in range(primeraPos + 1,segundaPos):
    distancia = distancia + vector[i]
  distancia = distancia + vector[primeraPos]/2 + vector[segundaPos]/2
  return distancia 

#Se realiza la funcion objetivo calculando la distancia entre los locales multiplicandolo por el flujo
def calcularFuncionObjetivo(cantidadTotalPuestos,vector):
    total = 0.0;
    for i in range (cantidadTotalPuestos):
      for j in range(i+1,cantidadTotalPuestos):
        indiceI = espacioLocales.index(vector[i])
        indiceJ = espacioLocales.index(vector[j])
        total = total + (calcularDistanciaEntrePuestos(i,j,vector) * matrizClientes[indiceI][indiceJ])
    return total
      
#Se realiza el criterio de metropolis restando la funcion objetivo nueva con la anterior(la mejor actual), luego se hace el criteo y se selecciona un numero aleatorio entre 0 - 1, para luego compararla con el criterio
def criterioMetropolis(comparar, temperatura):
    print("∆s: ",comparar)
    criterio = e**(-comparar/temperatura)
    print("P:", criterio)
    numeroRandom = random.random()
    print("Numero Generado Aleatoriamente:",numeroRandom)
    if(numeroRandom > criterio):
        print("El criterio es menor a un numero aleatorio entre 0 - 1, por lo tanto no es aceptado.")
        print("")
        return False
    print("El criterio es mayor a un numero aleatorio entre 0 - 1, por lo tanto es aceptado.")
    print("")
    return True

#Main del programa donde se realiza el procedimiento
espacioLocales = []
matrizClientes = []
funcionesObjetivo = []
numeroIntentoFuncionObjetivo = []
print("Ingrese la instancia que desea resolver:")
opcion = input("Opcion 1 para 'EjemploProfesora'\nOpcion 2 para 'QAP_sko56_04_n'\nOpcion 3 para 'QAP_sko100_04_n' Ingrese Opcion: ")
while(opcion != "1" and opcion != "2" and opcion != "3"):
  opcion = input("Ingrese una opcion valida: ")
if(opcion == "1"):
  nombre = "EjemploProfesora.txt"
if(opcion == "2"):
  nombre = "QAP_sko56_04_n.txt"
if(opcion == "3"):
  nombre = "QAP_sko100_04_n.txt"

#Inicializador de contador de tiempo
start = time.time()

temperatura = float(input("Ingrese Temperatura: "))
while(temperatura < 0.2):
  temperatura = float(input("Ingrese Temperatura valida: "))
lam = float(input("Ingrese Lambda: "))
while(lam < 0 or lam > 1):
  lam = float(input("Ingrese Lambda entre 0 y 1: "))
cantidadPuestos = llenarVectorYMatriz(nombre)
mejorVector = espacioLocales.copy()
random.shuffle(mejorVector)
funcionObjetivoMejor = calcularFuncionObjetivo(cantidadPuestos,mejorVector)



print("Primera Solucion: ")
print("*****************************************")
print("Funcion Objetivo:",funcionObjetivoMejor)
print("Locales:",mejorVector)
print("*****************************************")
print("")
funcionesObjetivo.append(funcionObjetivoMejor)
numeroIntentoFuncionObjetivo.append(1)


i = 2
while(temperatura > 0.2):
    if(i != 1):
        print("Mejor Solucion Actual")
        print("*****************************************")
        print("Funcion Objetivo:",funcionObjetivoMejor)
        print("Locales:",mejorVector)
        print("*****************************************")
        print("")

    vecino = mejorVector.copy()
    generarVecino(cantidadPuestos)
    funcionObjetivoVecino = calcularFuncionObjetivo(cantidadPuestos,vecino)

    print("*****************************************")
    print("Nueva Solucion numero",i,":", funcionObjetivoVecino)
    print("Locales: ", vecino)
    print("*****************************************")
    print("")
    if(funcionObjetivoVecino < funcionObjetivoMejor):
        print("La nueva solucion es mejor, por lo tanto se selecciona como mejor")
        print("")
        funcionesObjetivo.append(funcionObjetivoVecino)
        numeroIntentoFuncionObjetivo.append(i)
        funcionObjetivoMejor = funcionObjetivoVecino
        mejorVector = vecino.copy()

    else:
        print("A pesar de que la solucion no es mejor, se aplica el criterio de metropolis para ver si es aceptada.")
        print("")
        aceptarVecino = criterioMetropolis((funcionObjetivoVecino - funcionObjetivoMejor), temperatura)
        if(aceptarVecino == True):
            funcionesObjetivo.append(funcionObjetivoVecino)
            numeroIntentoFuncionObjetivo.append(i)
            funcionObjetivoMejor = funcionObjetivoVecino
            mejorVector = vecino.copy()
         
    #Se disminuye la temperatura
    temperatura = temperatura*lam
    i += 1
#Se termina el contador de tiempo
end = time.time()
print("")
print("*****************************************")
print("Mejor Solucion:")
print("Funcion objetivo",funcionObjetivoMejor)
print("Locales: ",mejorVector)
print("*****************************************")
print("Tiempo De Ejecucion:",end-start,"Segundos")
print("Desviacion Estandar De Las Funciones Aceptadas:",statistics.pstdev(funcionesObjetivo))
print("Varianza De Las Funciones Aceptadas:",var(funcionesObjetivo))

#Creacion del grafico para ver el comportamiento
plt.plot(numeroIntentoFuncionObjetivo,funcionesObjetivo,"-ok")
plt.xlabel("Numero De Intento")
plt.ylabel("Funcion Objetivo")
plt.show()