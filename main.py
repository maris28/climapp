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
    print("2. Consulta tu predicción")
    print("3. Modificar la predicción")
    print("4. Borrar la predicción")    
    print("0. Salir")

def buscar():
    print("Introduce la ciudad a consultar: ")
    ciudad = input()
    meteorosDb = db.collection("Meteoros")
    query = meteorosDb.where("ciudad", "==", ciudad)
    docs = query.stream()
    for doc in docs:
        print(f"{doc.to_dict()}")

def update():
    ciudad = input("Introduce la ciudad a modificar: \n")
    try:
        query = db.collection("Meteoros").where("Ciudad", "==", ciudad)
        resultado = query.stream()
        for result in resultado:
            print(f"Documento id: {result.id}")
            datos = result.to_dict()
            print("Datos actuales:", datos)
            newDay = input("Intruce nuevo valor: ")
            datos["DiaSem"] = newDay
            db.collection("Meteoros").document(result.id).update(datos)
            print("Valor modificado correctamente.")
    except Exception as e:
        print(f"Error: {e}")
    
def consultarTodasLasPredicciones():
    meteorosDb = db.collection("Meteoros")
    docs = meteorosDb.stream()
    for doc in docs:
        datos = doc.to_dict()
        print("\n")
        for clave, valor in datos.items():
            print(f"{clave.capitalize()}: {valor}", end=", ")
           
 
def ejecutarOption(opcion):
    if opcion ==1:
        insertDate(db)
    if opcion ==2:
        consultarTodasLasPredicciones()
    if opcion ==3:
        update()
    if opcion ==4:
        buscar()         
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
            
    


