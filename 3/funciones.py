"""Clase que nos permite manipular las listas    """

class ErrorCaracter(Exception):
    """Excepcion para controlar que los caracteres introducidos tiene valor numerico

        Parameters
        ----------
        Exception : Exception, 
            La excepcion salta si se intenta introducir un caracter que no sea numerico 
            

        Returns
        -------
        None
    """
    pass

class IndiceException(Exception):
    """Excepcion para controlar que el indice a eliminar sea menor que el tamaño de la lista

    Parameters
    ----------
    Exception : IndexError, 
        La excepcion salta si el indice a eliminar es mayor que el tamaño de la lista
        

    Returns
    -------
    None
    
    """
    pass

def añadirLista(lista,a):
    """Funcion para añadir un elemento al final de la lista

    Parameters
    ----------
    lista : List<int>, 
        Lista de entrada con valores numericos,
    a : int, Valor que se quiere introducir        

    Returns
    -------
    None
    
    Raises
    -----------
    ErrorCaracter: Se lanza la excepcion cuando el valor a introducir no es numerico
    """
    if isinstance(a, int):
        lista.append(a)
    else:
        raise ErrorCaracter("No se puede introducir un caracter, debe ser un numero")
    

def quitarListaInd(lista,indice):
    """Funcion para eliminar un valor de la lista a traves de su indice
    
    Parameters
    ----------
    lista : List<int>, 
        Lista de entrada con valores numericos,
    indice : int, Valor del indice de la lista que se solicita eliminar    

    Returns
    -------
    None
    
    Raises
    -----------
    IndiceException: Se lanza cuando el indice a eliminar es mayor que el tamaño de la lista
    ErrorCaracter: Se lanza la excepcion cuando el valor a introducir no es numerico

    """
    if isinstance(indice, int):
        if indice < len(lista): 
            del lista[indice]
        else:
            raise IndiceException("El tamaño de la lista es menor que el indice introducido")
    else:
        raise ErrorCaracter("No se puede introducir un caracter, debe ser un numero")

def sumarLista(lista):
    """Funcion que suma los valores de una lista numerica

    Parameters
    ----------
    lista : List<int>, 
        Lista de entrada con valores numericos  

    Returns
    -------
    int: Resultado de la suma de todos los valores de la lista pasada por argumento
        
    """
    return sum(lista)


def minimoLista(lista):
    """Funcion que saca el minimo valor de la lista

    Parameters
    ----------
    lista : List<int>, 
        Lista de entrada con valores numericos  

    Returns
    -------
    int: El valor minimo de la lista

    """
    return min(lista)

def maximoLista(lista):
    """Funcion que saca el maximo valor de la lista
    
    Parameters
    ----------
    lista : List<int>, 
        Lista de entrada con valores numericos  

    Returns
    -------
    int: El valor maximo de la lista
    """
    return max(lista)

