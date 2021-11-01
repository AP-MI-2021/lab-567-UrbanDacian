def creeazaCarte (id, titlu, gen, pret, abonament):
    '''
    Creaza un dictionar care retine o cheltuiala
    :param id: id-ul cartii din dictionar - int
    :param titlu: titlul cartii din dictionar - string
    :param gen: genul cartii din dictionar - string
    :param pret: pretul cartii din dictionar - float
    :param abonament: gold/silver/none - string
    :return:
    '''
    return {
        "id": id,
        "titlu": titlu,
        "gen": gen,
        "pret": pret,
        "abonament": abonament
    }



def getId(carte):
    return carte["id"]


def getTitlu(carte):
    return carte["titlu"]


def getGen(carte):
    return carte["gen"]

def getPret(carte):
    return carte["pret"]


def getAbonament(carte):
    return carte["abonament"]


def toString(carte):
    return "{}, {}, {}, {}, {}".format(
        getId(carte),
        getTitlu(carte),
        getGen(carte),
        getPret(carte),
        getAbonament(carte)
    )