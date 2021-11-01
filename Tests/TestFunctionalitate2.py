from Domain.Cheltuiala import getGen
from Logic.CRUD import adaugareCarte, getById
from Logic.Functionalitate2 import modificareGen


def testModificareGen():
    lista = []
    lista = adaugareCarte(1, "Colt Alb", "roman de aventura", 30, "none", lista)
    lista = adaugareCarte(2, "Ion la furat", "Fabula", 40, "gold", lista)
    lista = modificareGen("Ion la furat", "povesti pentru copii", lista)

    assert getGen(getById(2, lista)) == "povesti pentru copii"
    assert getGen(getById(1, lista)) == "roman de aventura"