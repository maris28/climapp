from firebase_admin import firestore

def insertDate(db):
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
    db.collection("Meteoros").add(datos)
