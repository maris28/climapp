from firebase_admin import firestore

def borrarRegistros(db):
    print("Introduce el nombre de la ciudad del registro a borrar: ")
    ciudad = input()
    meteorosDb = db.collection("Meteoros")
    docs = meteorosDb.where("ciudad", "==", ciudad).stream()
    for doc in docs:
        meteorosDb.document(doc.id).delete()