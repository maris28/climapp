import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred)
#jbdsakjasdfbjñkasdfnñksfda
db = firestore.client()


def showMenu():
    print("Selecciona una de las opciones:")
    print()
    print("1. Añade tu datos de meteo")
    print("2. Consultar todas las predicciones")
    print("3. Borrar Registros")
    print("0. Salir")

    try:
        opcion = int(input())
    except ValueError:
        print("Opción no válida. Introduzca nuevo valor: ")

    return opcion

def insertDate():
    print("Introduce el nombre de la ciudad: ")
    ciudad = input()
    print("Introduce el estado del cielo: ")
    cielo = input()
    print("Introduce los grados de temperatura: ")
    temperatura = int(input())
    print("Introduce la cantidad de precipitación: ")
    precipitacion = int(input())
    print("Introduce el día de la semana: ")
    diaSem = input()
    datos = {"ciudad": ciudad, "cielo": cielo, "temperatura": temperatura, "precipitacion": precipitacion, "diaSem": diaSem}
    db.collection("meteoros").add(datos)

def consultarTodasLasPredicciones():
    meteorosDb = db.collection("meteoros")
    docs = meteorosDb.stream()
    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")

def borrarRegistros():
    print("Introduce el nombre de la ciudad del registro a borrar: ")
    ciudad = input()
    meteorosDb = db.collection("meteoros")
    docs = meteorosDb.where("ciudad", "==", ciudad).stream()
    for doc in docs:
        meteorosDb.document(doc.id).delete()


while True:
    opcion = showMenu()

    if opcion == 1:
        insertDate()
    elif opcion == 2:
        consultarTodasLasPredicciones()
    elif opcion == 3:
        borrarRegistros()
    elif opcion == 0:
        break


    
    




