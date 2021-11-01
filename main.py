from Logic.CRUD import adaugareCarte
from Tests.TestAll import runAllTests
from UserInterface.Console import runMenu


def main():
    runAllTests()
    lista = []
    lista = adaugareCarte(1, "Carte de bucate", "mancare", 50.0, "silver", lista)
    lista = adaugareCarte(2, "Colt Alb", "Roman de aventuri", 30.0, "gold", lista)
    lista = adaugareCarte(3, "Ion la furat", "Fabule", 25.0, "none", lista)
    runMenu(lista)

main()