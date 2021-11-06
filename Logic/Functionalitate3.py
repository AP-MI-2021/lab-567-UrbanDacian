from Domain.Cheltuiala import getClasa, getPret


def pretulMaxim(lista):
    maxBusiness = 0
    maxEconomyPlus = 0
    maxEconomy = 0
    '''
     Determinarea prețului maxim pentru fiecare clasă.
    :param lista: lista de dicitonare
    :return: pretul maxim pentru fiecare clasa
    '''
    for cheltuiala in lista:
        if getClasa(cheltuiala) == "Business":
            if getPret(cheltuiala) > maxBusiness:
                maxBusiness = getPret(cheltuiala)
        elif getClasa(cheltuiala) == "Economy":
            if getPret(cheltuiala) > maxEconomy:
                maxEconomy = getPret(cheltuiala)
        else:
            if getPret(cheltuiala) > maxEconomyPlus:
                maxEconomyPlus = getPret(cheltuiala)
    return {
        "Pretul maxim pentru clasa Economy este: " + maxEconomy,
        "Pretul maxim pentru clasa EconomyPlus este: " + maxEconomyPlus,
        "Pretul maxim pentru clasa Business este: " + maxBusiness
    }        