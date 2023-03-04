from funciones import añadirLista,quitarListaInd,sumarLista,maximoLista,minimoLista,ErrorCaracter,IndiceException
import pytest

def test_1():
    lista = [5,80,3]
    añadirLista(lista,7)
    assert [5,80,3,7] == lista

def test_2():
    lista = [5,80,3]
    añadirLista(lista,20)
    assert [5,80,3,100] == lista

def test_11():
    lista = [5,80,3]
    with pytest.raises(ErrorCaracter):
        añadirLista(lista,"2")

def test_3():
    lista = [5,80,3]
    quitarListaInd(lista,0)
    assert [80,3] == lista

def test_4():
    lista = [5,80,3]
    quitarListaInd(lista,1)
    assert [80,3] == lista

def test_12():
    lista = [5,80,3]
    with pytest.raises(IndiceException):
        quitarListaInd(lista,10)

def test_5():
    lista = [5,80,3]
    suma = sumarLista(lista)
    assert 88==suma

def test_6():
    lista = [5,80,3]
    suma = sumarLista(lista)
    assert 87==suma
    
def test_7():
    lista = [5,80,3,83,100,2]
    max = maximoLista(lista)
    assert 100==max

def test_8():
    lista = [5,80,3,83,100,2]
    max = maximoLista(lista)
    assert 83==max

    
def test_9():
    lista = [5,80,3,83,100,2]
    min = minimoLista(lista)
    assert 2==min

def test_10():
    lista = [5,80,3,83,100,2]
    min = minimoLista(lista)
    assert 3==min
