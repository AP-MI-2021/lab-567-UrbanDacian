from Domain.Cheltuiala import getAbonament, getPret, creeazaCarte, getId, getTitlu, getGen


def aplicareReduceri(lista):
    '''
    Afiseaza o lista cu pretul cartilor dupa aplicarea unor reduceri in functie de tipul de abonament
    :param reducere: pretul dupa reducere
    :param lista: lista initiala
    :return: lista cu preturile modificate
    '''
    listaNoua = []
    for carte in lista:
        if getAbonament(carte) == "silver":
            reducere = getPret(carte) - 1/20 * getPret(carte)
            carteNoua = creeazaCarte(
                getId(carte),
                getTitlu(carte),
                getGen(carte),
                reducere,
                "silver"
            )
            listaNoua.append(carteNoua)
        elif getAbonament(carte) == "gold":
            reducere = getPret(carte) - 1 / 10 * getPret(carte)
            carteNoua = creeazaCarte(
                getId(carte),
                getTitlu(carte),
                getGen(carte),
                reducere,
                "gold"
            )
            listaNoua.append(carteNoua)
        else:
            listaNoua.append(carte)
    return listaNoua