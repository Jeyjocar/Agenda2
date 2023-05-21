"""
Agendas con archivos externos
17-01-2023
Jeyfrey Calero
"""

import email
import os
import pathlib


Salir = 0
Agregar = 1
Mostrar = 2
Buscar = 3
Borrar = 4


def mostrarMenu():
    os.system("cls")                                #para dar más rapidez de ejecución
    print(f'''Bienvenido a Mi Agenda
            {Agregar}) Insertar contacto
            {Mostrar}) Mostrar contacto
            {Buscar}) Buscar contacto
            {Borrar}) Borrar contacto
            {Salir}) Salir de Mi Agenda''')

def crearAgenda(agenda, nombreArchivo):
    if pathlib.Path(nombreArchivo, "r").exists():   #"r" abreviatura de READ
        with open(nombreArchivo) as contactos:      #para recorrer toda la lista usamos un bucle FOR
            for line in contactos:                  #se crean tres variables contacto, correo teléfono
                contacto, telefono, correo = line.strip().split(",")
                agenda.setdefault(contacto,(telefono, correo)) #para que queden mas ordenados y separados por ","
    else:
        with open(nombreArchivo, "w") as contactos: #eso es para que el archivo si no está creado, lo haga y guarde
            pass                                    #permite pasar de una función a otra función

def agregarContacto(agenda, nombreArchivo):
    os.system("cls")
    print("Agregar contacto a la agenda")
    nombre = input("Nombre contacto: ")
    if agenda.get(nombre):
        print("El contacto ya existe...")

    else:
        telefono = input("Ingrese el teléfono del contacto: ")
        correo = input("Ingrese el correo del contacto: ")
        agenda.setdefault(nombre,(telefono, correo))  #el ID lo da automático
        with open(nombreArchivo,"a") as contactos:
            contactos.write(f'{nombre}, {telefono}, {correo}\n')
            print("El Contacto se agregó con éxito")

def mostrarContacto(agenda):
    os.system("cls")
    print("Mostrar Contactos")
    if len(agenda)>0:
        #nombre = input("Cuál contacto desea buscar?")
        for contacto, datos in agenda.items():
            print(f'Nombre del contacto: {contacto}')
            print(f'Teléfono del contacto: {datos[0]}')
            print(f'Correo del contacto: {datos[1]}')
    
    else:
        print("No existen contactos en la agenda")


def buscarContacto(agenda):
    os.system("cls")
    print("Buscar Contactos")
    if len(agenda)>0:
        nombre = input("Ingrese el nombre del contacto que desea buscar: ")
        coincidencia = 0
        for contacto, datos in agenda.items():
            if nombre in contacto:
                print(f'Nombre del contacto: {contacto}')
                print(f'Teléfono del contacto: {datos[0]}')
                print(f'Correo del contacto: {datos[1]}')
                coincidencia += 1
                print('*'*30)

        if coincidencia == 0:
            print("El contacto no se encuentra en la agenda")
        else:
            print(f'Se encontraron: {coincidencia} contactos')
    
    else:
        print("La agenda no tiene contacto")


"""def borrarContacto(agenda):
    print("El contacto que usted seleccione, será eliminado de la lista.")
    if len(agenda) > 0:
        for i in range(len(agenda)):
            print(f"{i+1}. {agenda[i]}")
        print("0 cancelar el contacto")
            
        posicion = int(input(f"Ingrese la posicion del contacto que desea eliminar: (1-{len(agenda)})"))

        if 0 < posicion <= len(agenda):
                agenda.pop(posicion -1)
                print("El contacto ha sido eliminado con éxito")

        else:
                print("No es posible eliminar el contacto")
    else:
        print("No hay contactos en la agenda")"""





def main():
    continuar = True
    agenda = dict()                                         #DICT llamado de archivos externos
    nombreArchivo = "MisContactos.txt"
    crearAgenda(agenda, nombreArchivo)
    while continuar:
        mostrarMenu()
        opcion = int(input("Selecciona Una Opción: "))
        if opcion == Agregar:
            agregarContacto(agenda, nombreArchivo)
        elif opcion == Mostrar:
            mostrarContacto(agenda)
        elif opcion == Buscar:
            buscarContacto(agenda)
        #elif opcion == Borrar:
           # borrarContacto(agenda)
        elif opcion == Salir:
            continuar = False
        
        else:
            print("La opción ingresada no es válida")
        input("Presione ENTER para continuar: ")


if __name__ == "__main__":
    main()

