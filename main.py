
def showMenu():
    print("Selecciona una de las opciones:")
    print("1. Elegir Localización Favorita1")
    print("2. Cambiar Localización Favorita")
    print("3. Activar Alarma")
    print("4. Modificar Alarma")
    print("5. Eliminar Alarma")
    print("6. Consultar una predicción")
    print("0. Salir")

def ejecutarOption(opcion):
    if opcion ==1:
        chooseLocation()
    if opcion ==2:
        modifyLocation()
    if opcion ==3:
        activeAlarm()
    if opcion ==4:
        modifyAlarm()
    if opcion ==5:
        deleteAlarm()
    if opcion ==6:
        chceckPrediction()
    if opcion == 0:
        exit()

if __name__ == "__main__":
    opcion = -1

    while opcion != 0:
        showMenu()
        try:
            opcion = int(input())
        except ValueError:
            print("Opción no válida. Introduzca nuevo valor: ")
            
    






    
    




