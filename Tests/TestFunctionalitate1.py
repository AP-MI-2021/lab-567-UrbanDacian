from Domain.Cheltuiala import getPret
from Logic.CRUD import adaugareCarte, getById
from Logic.Functionalitate1 import aplicareReduceri


def testAplicareReduceri():
    lista = []
    lista = adaugareCarte(1, "Colt Alb", "roman de aventura", 30, "none", lista)
    lista = adaugareCarte(2, "Ion la furat", "Fabula", 40, "gold", lista)
    lista = aplicareReduceri(lista)

    assert getPret(getById(2, lista)) == 36
    assert getPret(getById(1, lista)) == 30