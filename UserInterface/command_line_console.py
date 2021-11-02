from Logic.CRUD import modificareCarte, adaugareCarte, stergereCarte
from UserInterface.Console import showAll


def printmenu2():
    print("1)Adaugare:")
    print("2)ShowAll: ")
    print("3)Delete: ")
    print("4)Stop: ")


def adaugaCarte(lista):
    id = int(input("Dati ID: "))
    titlu = input("Titlu: ")
    gen = input("Genul: ")
    pret = float(input("Pretul: "))
    abonament = input("Abonament (none/silver/gold): ")
    return adaugareCarte(id, titlu, gen, pret, abonament, lista)


def stergeCarte(lista):
    return stergereCarte(id, lista)


def modificaCarte(lista):
    id = input("Dati ID ul comenzii de modificat: ")
    titlu = input("Titlu nou: ")
    gen = input("Genul nou: ")
    pret = input("Pretul nou: ")
    abonament = input("Noul abonament (none/silver/gold): ")
    return modificareCarte(id, titlu, gen, pret, abonament, lista)


def runMenu2(lista):
    while True:
        printmenu2()
        optiune = input("Introduceti optiunea: ")
        if optiune == "1":
            lista = adaugaCarte(lista)
        elif optiune =="2":
            print(showAll(lista))
        elif optiune =="3":
            lista = stergeCarte(lista)
        elif optiune =="4":
            break
        else:
            print("Optiune incorecta! Reincercati: ")