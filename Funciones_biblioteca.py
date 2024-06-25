import json

def editar_cliente(id:int,credito:int):
    with open("biblioteca.json",mode="r") as Archivo.json:
    datos = json.load(Archivo.json)
    
    Clientes = datos["clientes"]
    for cliente in Clientes:
    if cliente["id"] == id:
        cliente["credito"]+= credito
        break

    with open ("biblioteca.json", mode="w") as archivo.json:
        json.dump(datos,Archivo,Json,indent=4)


def agregar_cliente(nombre:str,credito:int):
    with open("biblioteca.json", mode="r") as Archivo.json:
        datos = json.load(Archivo.json)

        cliente = {
            "id":len(datos["clientes"])+ 1,
            "nombre": nombre
            "credito": credito
        }
datos["clientes"].append(cliente)
with open("biblioteca.json",mode="w") as Archivo.json: