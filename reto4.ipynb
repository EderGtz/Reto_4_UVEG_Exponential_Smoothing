import numpy as np
from matplotlib import pyplot as plt

tabla_indicadores = {
    "HC": [44.9, 45.6, 45.4, 44.9, 44.3, None],
    "HI": [39.2, 47.0, 50.9, 52.9, 56.4, None],
    "HT": [93.5, 93.1, 93.2, 92.9, 92.5, None],
    "HTP": [43.7, 52.1, 49.5, 47.3, 45.9, None],
    "U6E": [51.3, 47.0, 45.3, 45.0, 43.0, None],
    "UI6E": [57.4, 59.5, 63.9, 65.8, 70.1, None],
    "UCHE": [51.3, 52.2, 46.8, 46.7, 44.6, None],
    "UITI": [12.8, 14.7, 20.4, 23.7, 27.2, None],
    "UIFH": [29.1, 20.5, 16.7, 13.4, 10.7, None],
    "UTC6E": [71.5, 73.6, 72.2, 73.5, 75.1, None]
}
#Elegi este factor de suavizamiento para tener un punto medio entre el pronostico de demanda y el valor real
FACTOR_DE_SUAVIZAMIENTO = 0.5
def formula_de_suavizamiento(pronostico_demanda_anterior, valor_demanda_real_anterior):
    return FACTOR_DE_SUAVIZAMIENTO * valor_demanda_real_anterior + (1 - FACTOR_DE_SUAVIZAMIENTO) * pronostico_demanda_anterior
#Function utilizada para generar el valor faltante
def calculo_pronostico_2020(tabla):
    for key in tabla_indicadores:
        #Se reinicia en cada iteracion de los indicadores porque no tiene utilidad fuera de este bloque
        lista_de_pronosticos_temporal = []
        #Se itera sobre todos los valores de cada indicador, para obtener uno a uno los
        #valores de pronostico, de tal manera que haya un historico
        for i in range(len(tabla_indicadores[key])):
            valor_real_actual = tabla_indicadores[key][i]
            valor_real_anterior = tabla_indicadores[key][i-1]
            #Entra en este if si el valor real anterior es None, lo cual se cumple para el valor 2015
            #ya que su valor anterior apunta hacia el final de la lista, la cual es None
            if not valor_real_anterior:
                primer_pronostico = formula_de_suavizamiento(valor_real_actual, valor_real_actual)
                lista_de_pronosticos_temporal.append(primer_pronostico)
                continue #Para continuar el bucle y que no se ejecute lo demas
            elif valor_real_actual is None:
                pronostico_2020 = formula_de_suavizamiento(lista_de_pronosticos_temporal[-1], valor_real_anterior)
                #Se utiliza el valor en i y no el valor de 6 hardcodeado
                #para utilizar el mismo codigo en listas de mayor longitud
                tabla_indicadores[key][i] = pronostico_2020
                continue
            #En caso de que ninguna condicional se cumpla, se recurre a estas lineas
            pronostico_actual = formula_de_suavizamiento(lista_de_pronosticos_temporal[-1],valor_real_anterior)
            lista_de_pronosticos_temporal.append(pronostico_actual)

def dibujar_grafico(tabla_indicadores):
    x = np.array(range(2015, 2021))
    for key in tabla_indicadores:
        plt.plot(x, tabla_indicadores[key], marker = '.', linewidth = '.5', label = key)

    plt.xlabel("Año")
    plt.ylabel("Valores")
    plt.title("Reto 4 - Eder Gutierrez", loc = "left")
    #Sacando a la tabla fuera del dibujo, para mejor visualizacion
    plt.legend(bbox_to_anchor=(0.60, 0.80,0.5,0.5), ncol=3)
    plt.show()

def main():
    calculo_pronostico_2020(tabla_indicadores)
    dibujar_grafico(tabla_indicadores)
main()
