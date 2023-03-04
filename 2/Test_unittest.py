from funciones import añadirLista,quitarListaInd,sumarLista,maximoLista,minimoLista
import unittest



class Test_unittest(unittest.TestCase):
    def test_1(self):
        lista = [5,80,3]
        añadirLista(lista,7)
        self.assertEqual([5,80,3,7],lista)

    def test_2(self):
        lista = [5,80,3]
        añadirLista(lista,20)
        self.assertEqual([5,80,3,100],lista)
        
    def test_11(self):
        lista = [5,80,3]
        añadirLista(lista,"2")
        self.assertEqual([5,80,3,2],lista)
        
    def test_3(self):
        lista = [5,80,3]
        quitarListaInd(lista,0)
        self.assertEqual([80,3],lista)

    def test_4(self):
        lista = [5,80,3]
        quitarListaInd(lista,1)
        self.assertEqual([80,3],lista)
        
    def test_12(self):
        lista = [5,80,3]
        quitarListaInd(lista,10)
        self.assertEqual([5,80,3],lista)
        
    def test_5(self):
        lista = [5,80,3]
        suma = sumarLista(lista)
        self.assertEqual(88,suma)

    def test_6(self):
        lista = [5,80,3]
        suma = sumarLista(lista)
        self.assertEqual(87,suma)
        
    def test_7(self):
        lista = [5,80,3,83,100,2]
        max = maximoLista(lista)
        self.assertEqual(100,max)

    def test_8(self):
        lista = [5,80,3,83,100,2]
        max = maximoLista(lista)
        self.assertEqual(83,max)
        
    def test_9(self):
        lista = [5,80,3,83,100,2]
        min = minimoLista(lista)
        self.assertEqual(2,min)

    def test_10(self):
        lista = [5,80,3,83,100,2]
        min = minimoLista(lista)
        self.assertEqual(3,min)        
unittest.main()