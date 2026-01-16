library(purrr)
#Creacion de tabla sin los numeros
data_reto_4 <- data.frame(
  HC=c(44.9, 45.6, 45.4, 44.9, 44.3), 
  HI=c(39.2, 47.0, 50.9, 52.9, 56.4),
  HT=c(93.5, 93.1, 93.2, 92.9, 92.5),
  HTP=c(43.7, 52.1, 49.5, 47.3, 45.9),
  U6E=c(51.3, 47.0, 45.3, 45.0, 43.0),
  UI6E=c(57.4, 59.5, 63.9, 65.8, 70.1),
  UCHE=c(51.3, 52.2, 46.8, 46.7, 44.6),
  UITI=c(12.8, 14.7, 20.4, 23.7, 27.2),
  UIFH=c(29.1, 20.5, 16.7, 13.4, 10.7),
  UTC6E=c(71.5, 73.6, 72.2, 73.5, 75.1)
)

nombres_columnas <- names(data_reto_4)
#Creo una copia del original para modificar los valores, y no se vea
#afectado el original por la creacion de los NA
data_reto_4_copia <- data_reto_4

FACTOR_DE_SUAVIZAMIENTO <- 0.5
formula_de_suavizamiento <- function(pronostico_demanda_anterior, valor_demanda_real_anterior){
  FACTOR_DE_SUAVIZAMIENTO * valor_demanda_real_anterior + (1 - FACTOR_DE_SUAVIZAMIENTO) * pronostico_demanda_anterior
}

for (nombre_columna in nombres_columnas){
  datos_de_columna_actual = data_reto_4_copia[[nombre_columna]]
  #Se utiliza la funcion reduce de programacion funcional, para calcular de forma
  #repetida el valor de prediccion
  valor_2020 <- datos_de_columna_actual |> purrr::reduce(formula_de_suavizamiento)
  #casilla 6 de la columna actual
  data_reto_4[6, nombre_columna] <- valor_2020
}

data_reto_4

anios_de_datos <- 2015:2020
matplot(anios_de_datos, data_reto_4, 
  type = "l",
  xlab = "Año",
  ylab = "Valores"
)
title(main = "Reto 4 - Eder Gutierrez", adj = 0)
legend("topleft", 
       legend = colnames(data_reto_4), 
       col = 1:10, 
       lty = 1, 
       cex = 0.4) 
