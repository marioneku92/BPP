class ErrorCaracter(Exception):
    pass

class IndiceException(Exception):
    pass

def añadirLista(lista,a):
    if isinstance(a, int):
        lista.append(a)
    else:
        raise ErrorCaracter("No se puede introducir un caracter, debe ser un numero")
    

def quitarListaInd(lista,indice):
    if isinstance(indice, int):
        if indice < len(lista): 
            del lista[indice]
        else:
            raise IndiceException("El tamaño de la lista es menor que el indice introducido")
    else:
        raise ErrorCaracter("No se puede introducir un caracter, debe ser un numero")

def sumarLista(lista):
    return sum(lista)


def minimoLista(lista):
    return min(lista)

def maximoLista(lista):
    return max(lista)

