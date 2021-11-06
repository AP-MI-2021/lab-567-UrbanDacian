from Domain.Cheltuiala import creeazaCheltuiala, getId


def adaugaCheltuiala(id, nume, clasa, pret, checkin, lista):
    '''
    Adauga o cheltuiala la o lista
    :param id: id-ul cheltuielii
    :param nume: numele cheltuielii
    :param clasa: clasa cheltuielii
    :param pret: pretul cheltuielii
    :param checkin: tipul de checkin
    :param lista: lista initiala
    :return: lista care contine noua cheltuiala
    '''
    return lista + [creeazaCheltuiala(id, nume, clasa, pret, checkin)]


def stergeCheltuiala(id, lista):
    listaNoua = []
    '''
    Sterge o cheltuiala din lista
    :param id: id-ul cheltuielii care urmeaza sa fie sterse
    :param lista: lista initiala
    :return: lista finala fara cheltuiala care trebuie stearsa
    '''
    for cheltuiala in lista:
        if getId(cheltuiala) != id:
            listaNoua.append(cheltuiala)
    return listaNoua


def modificareCheltuiala(id, nume, clasa, pret, checkin, lista):
    listaNoua = []
    '''
    Modifica o cheltuiala din lista
    :param id: id-ul cheltuielii care urmeaza sa fie modificate
    :param nume: numele noii cheltuieli
    :param clasa: clasa noii cheltuieli
    :param pret: pretul noii cheltuieli
    :param checkin: tipul de checkin al noii cheltuieli
    :param lista: lista initiala
    :return: lista finala cu cheltuiala care a fost modificata
    '''
    for cheltuiala in lista:
        if getId(cheltuiala) != id:
            listaNoua.append(cheltuiala)
        else:
            listaNoua.append(creeazaCheltuiala(id, nume, clasa, pret, checkin))
    return listaNoua


def getById(id, lista):
    '''
    Returneaza o cheltuiala cu ajutorul id-ului acesteia
    :param id: id-ul cheltuielii cautate
    :param lista: lista de cheltuieli
    :return: cheltuiala
    '''
    for cheltuiala in lista:
        if getId(cheltuiala) == id:
            return cheltuiala