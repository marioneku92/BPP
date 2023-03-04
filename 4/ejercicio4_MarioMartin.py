
listas = [[2, 4, 1], [1,2,3,4,5,6,7,8], [100,250,43]]

maximos = [max(lista) for lista in listas]
print(maximos)

def ObtenerPrimos(valor):
    if valor > 0:
        cont = 0
        for i in range(2,valor):
            resto = valor % i
            
            if resto == 0:
                cont+=1
        if cont == 0:
                return True

lista= [3, 4, 8, 5, 5, 22, 13]

primos = list(filter(ObtenerPrimos,lista))
print(primos)
