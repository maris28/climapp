import firebase_admin
from firebase_admin import credentials, firestore
from insertarEvento import insertDate

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
    print("6. Consultar todas las predicciones")
    print("0. Salir")

def buscarPorCiudad():
    print("Introduce la ciudad a consultar: ")
    ciudad = input()
    meteorosDb = db.collection("Meteoros")
    query = meteorosDb.where("Ciudad", "==", ciudad)
    docs = query.stream()
    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")

 
def ejecutarOption(opcion):
    if opcion ==1:
        insertDate(db)
    if opcion ==2:
        modifyLocation()
    if opcion ==3:
        activeAlarm()
    if opcion ==4:
        modifyAlarm()
    if opcion ==5:
        deleteAlarm()
    if opcion ==6:
        buscarPorCiudad()
    if opcion == 0:
        exit()

if __name__ == "__main__":
    opcion = -1

    while opcion != 0:
        showMenu()
        try:
            opcion = int(input())
            ejecutarOption(opcion)
        except ValueError:
            print("Opción no válida. Introduzca nuevo valor: ")
            
    


