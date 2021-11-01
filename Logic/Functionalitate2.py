from Domain.Cheltuiala import getTitlu, getAbonament, getPret, getId, creeazaCarte


def modificareGen(titlu, gen, lista):
    '''
    Modifica genul unei carti folosindu-se de titlul acesteia
    :param titlu: titlul cartii careia urmeaza sa i se schimbe genul
    :param gen: genul care urmeaza sa fie aplicat unei carti
    :param lista: lista initiala, fara ca genul cartii sa fie schimbat
    :return: o noua lista in care genul cartii este schimbat
    '''
    listaNoua = []
    for carte in lista:
        if getTitlu(carte) == titlu:
            carteNoua = creeazaCarte(
                getId(carte),
                getTitlu(carte),
                gen,
                getPret(carte),
                getAbonament(carte)
            )
            listaNoua.append(carteNoua)
        else:
            listaNoua.append(carte)
    return listaNoua