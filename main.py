from Logic.CRUD import adaugareCarte
from Tests.TestAll import runAllTests
from UserInterface.Console import runMenu
from UserInterface.command_line_console import runMenu2


def main():
    runAllTests()
    lista = []
    lista = adaugareCarte(1, "Carte de bucate", "mancare", 50.0, "silver", lista)
    lista = adaugareCarte(2, "Colt Alb", "Roman de aventuri", 30.0, "gold", lista)
    lista = adaugareCarte(3, "Ion la furat", "Fabule", 25.0, "none", lista)

    print("1.Meniu principal")
    print("2.Meniu secundar")
    optiune = input("Alegeti meniul: ")
    if optiune == "1":
        return runMenu(lista)
    elif optiune == "2":
        return runMenu2(lista)
    else:
        print("Comanda gresita! Reincercati.")

main()