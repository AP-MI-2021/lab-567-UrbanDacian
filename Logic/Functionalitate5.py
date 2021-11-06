from Domain.Cheltuiala import getNume, getId, getPret


def suma(lista):
    '''
    Afișarea sumelor prețurilor pentru fiecare nume.
    :param lista: lista de dicitonare
    :return: suma pentru fiecare nume din lista
    '''
    arr = []
    brr = []
    for i in range(len(lista)):
        arr[i] = 0
    for j in range(len(lista)):
        brr[j] = 1
    for cheltuiala in lista:
        for cheltuiala2 in lista:
            if getNume(cheltuiala) == getNume(cheltuiala2) and brr[cheltuiala2] == 1:
                arr[getId(cheltuiala)] += getPret(cheltuiala2)
                brr[getId(cheltuiala2)] = 0

        