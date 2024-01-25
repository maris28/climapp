import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred)

#jbdsakjasdfbjñkasdfnñksfda

db = firestore.client()


def showMenu():
    print("Selecciona una de las opciones:")
    print("1. Añade tu datos de meteo")
    print("2. Cambiar Localización Favorita")
    print("3. Activar Alarma")
    print("4. Modificar Alarma")
    print("5. Eliminar Alarma")
    print("6. Consultar una predicción")
    print("0. Salir")

def insertDate():
    print("Introduce el nombre de la ciudad: ")
    ciudad = input()
    print("Introduce el estado del cielo: ")
    cielo = input()
    print("Introduce los grados de temperatura: ")
    temperatura = int(input())
    print("Introduce la cantidad de precipitación: ")
    precipitacion  = int(input())
    print("Introduce el día de la semana: ")
    diaSem = input()
    datos = {"ciudad": ciudad, "cielo": cielo, "temperatura": temperatura, "precipitacion": precipitacion, "diaSem": diaSem}
    db.collection("meteoros").add(datos)

 
def ejecutarOption(opcion):
    if opcion ==1:
        insertDate()
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
            insertDate()
            opcion = int(input())
        except ValueError:
            print("Opción no válida. Introduzca nuevo valor: ")
            
    





    
    




