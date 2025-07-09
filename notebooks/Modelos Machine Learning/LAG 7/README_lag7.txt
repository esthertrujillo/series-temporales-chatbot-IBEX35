# README – Predicción bursátil IBEX 35 (Lag = 7)

Este notebook contiene un experimento de predicción bursátil aplicado a precios de cierre de empresas del IBEX 35 con un horizonte temporal de **7 días (lag = 7)**. Forma parte de un estudio más amplio orientado a integrar modelos predictivos en un sistema conversacional inteligente.

##  Objetivo

Evaluar el rendimiento de distintos modelos de aprendizaje automático (SVR, regresión lineal, Random Forest, entre otros) para anticipar la evolución bursátil semanal (lag=7), seleccionando una empresa representativa por clúster del IBEX 35.

##  Metodología

- Se seleccionan 7 empresas representativas de distintos clústeres:  
  `ACCIONA`, `INDITEX`, `AENA`, `SANTANDER`, `BBVA`, `ARCELORMITTAL`, `INM. COLONIAL`

- Para cada empresa:
  1. Se crean variables temporales (lags, medias móviles, atributos del calendario).
  2. Se ajusta la variable objetivo (`Precio_cierre`) desplazándola 7 días hacia atrás.
  3. Se divide el dataset en entrenamiento y test.
  4. Se escalan los datos cuando es necesario.
  5. Se entrenan y comparan varios modelos mediante `GridSearchCV`.
  6. Se evalúan los resultados con la métrica RMSE.

##  Resultados

- El modelo **SVR** obtuvo el mejor rendimiento medio para lag = 7, manteniéndose estable frente a la regresión lineal y otros modelos en este horizonte.
- Se observa un aumento lógico del error respecto al lag = 1, pero con predicciones razonables en la mayoría de los casos.

## Estructura del notebook

- **Carga de datos**
- **Filtrado por empresa**
- **Generación de variables**
- **Entrenamiento y evaluación por empresa**
- **Visualización de resultados**

