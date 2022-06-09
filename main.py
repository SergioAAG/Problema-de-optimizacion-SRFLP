espacioLocales = []
matrizClientes = []

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
  

print("Ingrese la instancia que desea resolver:")
opcion = input("Opcion 1 para 'EjemploProfesora'\nOpcion 2 para 'QAP_sko56_04_n'\nOpcion 3 para 'QAP_sko100_04_n' ")
while(opcion != "1" and opcion != "2" and opcion != "3"):
  opcion = input("Ingrese una opcion valida: ")
if(opcion == "1"):
  nombre = "EjemploProfesora.txt"
if(opcion == "2"):
  nombre = "QAP_sko56_04_n.txt"
if(opcion == "3"):
  nombre = "QAP_sko100_04_n.txt"

cantidadPuestos = llenarVectorYMatriz(nombre)
print(cantidadPuestos)
print(espacioLocales)
print(matrizClientes)