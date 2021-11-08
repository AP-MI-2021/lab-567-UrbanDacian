from Domain.Cheltuiala import toString
from Logic.CRUD import adaugaCheltuiala, stergeCheltuiala, modificareCheltuiala


def help():
    '''
    In meniu comenzile sunt separate prin ; iar variabilele ce trebuie atribuite prin ,
    :return: meniul
    '''
    print("Add,Id,Nume,Clasa,Pret,Checkin")
    print("Delete,Id")
    print("Showall")
    print("Update,Id,Nume,Clasa,Pret,Checkin")
    print("Stop")


def showAllCL(lista):
    print(toString(lista))


def runMenuCL(lista):
    help()
    while True:
        option = input("Introduceti comanda: ")
        if option == "Meniu":
            help()
        elif option == "Stop":
            break
        else:
            part_split = option.split(";")
            for comanda in part_split:
                comanda_split = comanda.split(',')
                if comanda_split[0] == "Add":
                    try:
                        lista = adaugaCheltuiala(comanda_split[1], comanda_split[2], comanda_split[3], comanda_split[4], comanda_split[5], lista)
                    except ValueError as ve:
                        print("Eroare {}".format(ve))
                        return lista
                elif comanda_split[0] == "Delete":
                    lista = stergeCheltuiala(comanda_split[1], lista)
                elif comanda_split[0] == "Update":
                    try:
                        lista = modificareCheltuiala(comanda_split[1], comanda_split[2], comanda_split[3], comanda_split[4], comanda_split[5], lista)
                    except ValueError as ve:
                        print("Eroare {}".format(ve))
                        return lista
                elif comanda_split[0] == "Showall":
                    showAllCL(lista)
                elif comanda_split[0] == "Help":
                    help()