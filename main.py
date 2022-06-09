#print("Ingrese la instancia que desea resolver:")
#opcion = print("Opcion 1 para 'EjemploProfesora'\n Opcion 2 para 'QAP_sko56_04_n'\n Opcion 3 para 'QAP_sko100_04_n'")



espacioLocales = []
matrizConcurrencia = []

def llenarVectorYMatriz():
  archivoInstancia = open("EjemploProfesora.txt")
  lineaLeer = archivoInstancia.readline().strip().split(",")
  cantidadLocales = int(lineaLeer[0])

  lineaLeer = archivoInstancia.readline().strip().split(",")
  for x in lineaLeer:
    espacioLocales.append(int(x))

  for x in range(0,5):
    lineaLeer = archivoInstancia.readline().strip().split(",")
    for j in range(0,5):
      lineaLeer[j] = int(lineaLeer[j])
    matrizConcurrencia.append(lineaLeer)
  return cantidadLocales


cantidadPuestos = llenarVectorYMatriz()
print(cantidadPuestos)
print(espacioLocales)
print(matrizConcurrencia)