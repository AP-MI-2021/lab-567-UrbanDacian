from Domain.Cheltuiala import creeazaCarte, getId


def adaugareCarte(id, titlu, gen, pret, abonament, lista):
    '''
    Adauga o carte la lista
    :param id: id-ul cartii - int
    :param titlu: titlul cartii - string
    :param gen: genul cartii - string
    :param pret: pretul cartii - float
    :param abonament: tipul de abonament - float
    :param lista: lista initiala
    :return: lista la care se adauga si noua carte
    '''
    carte = creeazaCarte(id, titlu, gen, pret, abonament)
    return lista + [carte]


def stergereCarte(id, lista):
    '''
    Sterge o carte din dictionar folosindu-se de id-ul acesteia
    :param id: id-ul cartii care sa fie sterse - int
    :param lista: libraria inainte de stergerea cartii
    :return: lista fara cartea care trebuia stearsa
    '''
    id = int(input("Dati id-ul cartii care sa fie sterse: "))
    return (carte for carte in lista if getId(carte) != id)


def modificareCarte(id, titlu, gen, pret, abonament, lista):
    '''
    Schimba o carte din lista cu una noua
    :param id: id-ul cartii - int
    :param titlu: titlul carti - string
    :param gen: genul cartii - string
    :param pret: pretul cartii - float
    :param abonament: tipul de abonament - string
    :param lista: lista initiala
    :return: o lista noua cu cartea modificata
    '''
    listaNoua = []
    for carte in lista:
        if getId(carte) != id:
            listaNoua.append(carte)
        else:
            carteNoua = creeazaCarte(id, titlu, gen, pret, abonament)
            listaNoua.append(carteNoua)
    return listaNoua


def getById(id, lista):
    '''
    Returneaza o carte cu ajutorul id-ului acesteia
    :param id: id-ul cartii cautate
    :param lista: lista de carti
    :return: cartea cautata
    '''
    for carte in lista:
        if getId(carte) == id:
            return carte