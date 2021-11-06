from Domain.Cheltuiala import getNume, getClasa, creeazaCheltuiala, getId, getPret, getCheckin


def crestereClasa(nume, lista):
    '''
    Trecerea tuturor rezervărilor făcute pe un nume citit la o clasă superioară.
    :param nume: numele
    :param lista: lista de cheltuieli
    :return: lista noua
    '''
    listaNoua = []
    for cheltuiala in lista:
        if getNume(cheltuiala) == nume:
            if getClasa(cheltuiala) == "economy":
                cheltuialaNoua = creeazaCheltuiala(
                    getId(cheltuiala),
                    getNume(cheltuiala),
                    "economy plus",
                    getPret(cheltuiala),
                    getCheckin(cheltuiala)
                )
                listaNoua.append(cheltuialaNoua)
            elif getClasa(cheltuiala) == "economy plus":
                cheltuialaNoua = creeazaCheltuiala(
                    getId(cheltuiala),
                    getNume(cheltuiala),
                    "business",
                    getPret(cheltuiala),
                    getCheckin(cheltuiala)
                )
                listaNoua.append(cheltuialaNoua)
        else:
            listaNoua.append(cheltuiala)
    return listaNoua
