from Domain.Cheltuiala import getPret, getId
from Logic.CRUD import getById, stergeCheltuiala


def ordonarePreturi(lista):
    '''
    Ordonarea rezervărilor descrescător după preț.
    :param lista: lista de dictionare
    :return: lista ordonata descrescator
    '''
    listaNoua = []
    pretMax = 0
    while len(lista) != 0:
        for cheltuiala in lista:
            if getPret(cheltuiala) > pretMax:
                pretMax = getPret(cheltuiala)
                id = getId(cheltuiala)
        listaNoua.append(getById(id, lista))
        stergeCheltuiala(id, lista)
    return listaNoua