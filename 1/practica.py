import matplotlib.pyplot as plt
import csv



class ErrorExcel(Exception):
    pass
    
class ErrorColumna(Exception):
    pass
    
class ErrorDato(Exception):
    pass

def comprobarTipoFloat(n):
    try:
        numero=float(n.replace("'",""))
        if numero=="":
            raise ErrorColumna
        else:
            return numero
    except:
        raise ErrorDato
        

sumaEnero=0
sumaFebrero=0
sumaMarzo=0      
sumaAbril=0
sumaMayo=0
sumaJunio=0
sumaJulio=0
sumaAgosto=0
sumaSeptiembre=0
sumaOctubre=0
sumaNoviembre=0
sumaDiciembre=0
        
totalGastos = 0
totalIngresos = 0
        
try:
    with open("finanzas2020.csv","r") as f:
        reader = csv.reader(f,delimiter="\t")
        listaMeses=list(next(reader))
        
        if(len(listaMeses) < 12):
            raise ErrorExcel
                
        
        for row in list(reader):
            try:
                sumaEnero+=comprobarTipoFloat(row[0])
                sumaFebrero+=comprobarTipoFloat(row[1])
                sumaMarzo+=comprobarTipoFloat(row[2])      
                sumaAbril+=comprobarTipoFloat(row[3])
                sumaMayo+=comprobarTipoFloat(row[4])
                sumaJunio+=comprobarTipoFloat(row[5])
                sumaJulio+=comprobarTipoFloat(row[6])
                sumaAgosto+=comprobarTipoFloat(row[7])
                sumaSeptiembre+=comprobarTipoFloat(row[8])
                sumaOctubre+=comprobarTipoFloat(row[9])
                sumaNoviembre+=comprobarTipoFloat(row[10])
                sumaDiciembre+=comprobarTipoFloat(row[11])
                for i in row:
                    num=float(i.replace("'",""))
                    if num>0:
                        totalIngresos+=num
                    else:
                        totalGastos+=num
            except:
                continue
                    
                                                                                                                      


        listaAnual=[]
        listaAnual.append(sumaEnero)
        listaAnual.append(sumaFebrero)
        listaAnual.append(sumaMarzo)
        listaAnual.append(sumaAbril)
        listaAnual.append(sumaMayo)
        listaAnual.append(sumaJunio)
        listaAnual.append(sumaJulio)
        listaAnual.append(sumaAgosto)
        listaAnual.append(sumaSeptiembre)
        listaAnual.append(sumaOctubre)
        listaAnual.append(sumaNoviembre)
        listaAnual.append(sumaDiciembre)



        maxAhorrado = max(listaAnual)
        indMesMaxAhorrado = listaAnual.index(maxAhorrado)
        maxGastado = min(listaAnual)
        indMesMaxGastado = listaAnual.index(maxGastado)
        mediaGastos = sum(listaAnual)/len(listaAnual)
        
        print("El mes que mas se ha ahorrado ha sido "+str(listaMeses[indMesMaxAhorrado])+" que se ha ahorrado "+str(abs(maxAhorrado)))
        print("El mes que mas se ha gastado ha sido "+str(listaMeses[indMesMaxGastado])+" que se ha gastado "+str(abs(maxGastado)))
        print("La media de gastos ha sido "+str(mediaGastos))
        print("Los ingresos totales han sido "+str(totalIngresos))
        print("Los gastos totales han sido "+str(abs(totalGastos)))        
                
        plt.bar(listaMeses,listaAnual, label="Ingresos")
        plt.legend()

        # The following commands add labels to our figure.
        plt.xlabel('Meses')
        plt.ylabel('Ingresos')
        plt.title('Gastos y ganancias del año')

        plt.show()
        
except ErrorExcel:
    print("El numero de columnas no es valido, tienen que ser 12")
    pass
except ErrorColumna:
    print("No existe datos o no es valida la columna")
    pass
except ErrorDato:
    print("El dato es incorrecto")
    pass
except Exception as e:
    print(e)
        
else:
    print("Termino")
    
