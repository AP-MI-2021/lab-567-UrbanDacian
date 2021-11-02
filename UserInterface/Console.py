from Domain.Cheltuiala import toString
from Logic.CRUD import adaugareCarte, stergereCarte, modificareCarte
from Logic.Functionalitate1 import aplicareReduceri
from Logic.Functionalitate2 import modificareGen


def printMenu():
    print("1. Adaugare carte")
    print("2. Stergere carte")
    print("3. Modificare carte")
    print("4. Aplicarea reducerilor pe baza abonamentelor")
    print("5. Modificarea genul unei carti")
    print("a. Afisare carti")
    print("x. Iesire")


def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            lista = uiAdaugareCarte(lista)
        elif optiune == "2":
            lista = uiStergereCarte(lista)
        elif optiune == "3":
            lista = uiModificareCarte(lista)
        elif optiune == "4":
            lista = uiAplicareReduceri(lista)
        elif optiune == "5":
            lista = uiModificareGen(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")


def showAll(lista):
    for carte in lista:
        print(toString(carte))


def uiAdaugareCarte(lista):
    id = int(input("Dati id-ul cartii: "))
    titlu = input("Dati titlul cartii: ")
    gen = input("Dati genul cartii: ")
    pret = float(input("Dati pretul cartii: "))
    abonament = input("Dati tipul de abonament (none/silver/gold): ")
    return adaugareCarte(id, titlu, gen, pret, abonament, lista)


def uiStergereCarte(lista):
    return stergereCarte(id, lista)


def uiModificareCarte(lista):
    id = int(input("Dati id-ul cartii: "))
    titlu = input("Dati titlul cartii: ")
    gen = input("Dati genul cartii: ")
    pret = float(input("Dati pretul cartii: "))
    abonament = input("Dati tipul de abonament (none/silver/gold): ")
    return modificareCarte(id, titlu, gen, pret, abonament, lista)


def uiAplicareReduceri(lista):
    reducere = 0
    return aplicareReduceri(lista)


def uiModificareGen(lista):
    titlu = input("Dati titlul cartii care sa fie modificare: ")
    gen = input("Dati noul gen al cartii: ")
    return modificareGen(titlu, gen, lista)