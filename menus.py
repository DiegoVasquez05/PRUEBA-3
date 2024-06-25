print("*******************************")
print("**       MUNDO LIBRO         **")
print("*******************************")

opciones = "Mantenedor de usuarios","Reportes","Salir"
contador = 0

for i in opciones:
    contador+=1
    print(f'({contador}){i}')

opcion=int(input("ingrese el numero de la opcion que quiera: "))


def menu_contenedor_usuario():
        print("*******************************")    
        print("**    MANTERNEDOR USUARIO    **")
        print("*******************************") 

        opciones_menu_mantenedor_usuario =("- Agregar usuario", "- Editar usuario", "- Eliminar usuario", "- Buscar usuario", "- Volver")
        contador_menu_mantenedor= 0

        for i in opciones_menu_mantenedor_usuario:
            contador_menu_mantenedor+=1 
            print(f'({contador_menu_mantenedor}){i}')
            
        opciones_menu_mantenedor_usuario=int(input("ingrese el numero de la opcion que quiera: ")) 

if opciones == 1:
     (menu_contenedor_usuario)