from Domain.Cheltuiala import getTitlu, getPret, getGen, getId
from Logic.CRUD import adaugareCarte, getById, stergereCarte, modificareCarte


def testAdaugareCarte():
    lista = []
    lista = adaugareCarte(1, "Colt Alb", "roman de aventura", 30, "none", lista)

    assert len(lista) == 1
    assert getTitlu(getById(1, lista)) == "Colt Alb"
    assert getPret(getById(1, lista)) == 30.0
    assert getGen(getById(1, lista)) == "roman de aventura"


def testModificareCarte():
    lista = []
    lista = adaugareCarte(1, "Colt Alb", "roman de aventura", 30, "none", lista)
    lista = adaugareCarte(2, "Ion la furat", "Fabula", 40, "gold", lista)
    lista = modificareCarte(2, "Ghita si oaia", "Povesti porcaresti", 45, "none", lista)

    assert len(lista) == 2
    assert getTitlu(getById(2, lista)) == "Ghita si oaia"
    assert getGen(getById(2,lista)) == "Povesti porcaresti"
