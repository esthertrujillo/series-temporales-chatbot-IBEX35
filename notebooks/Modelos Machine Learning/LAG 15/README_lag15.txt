# README – Predicción bursátil IBEX 35 (Lag = 15)

Este notebook desarrolla un experimento de predicción bursátil centrado en anticipar los precios de cierre de empresas del IBEX 35 con un horizonte de **15 días (lag = 15)**. Se trata del caso más exigente del estudio, al requerir la estimación de movimientos de mercado a más largo plazo.

##  Objetivo

Evaluar el rendimiento de modelos de machine learning en escenarios de predicción bursátil a medio plazo, seleccionando empresas representativas de diferentes comportamientos históricos del mercado español.

##  Metodología

- Se utilizan 7 empresas seleccionadas por su representatividad en clústeres previos:
  - `ACCIONA`, `INDITEX`, `AENA`, `SANTANDER`, `BBVA`, `ARCELORMITTAL`, `INM. COLONIAL`

- Para cada empresa se realiza:
  1. Limpieza y transformación de datos (formato de fecha, tipo numérico).
  2. Generación de variables temporales: año, mes, día, trimestre, día de la semana, semana del año.
  3. Creación de variables desplazadas (lag = 15).
  4. Cálculo de medias y desviaciones móviles con ventanas de 7, 30 y 60 días, todas alineadas con el lag.
  5. División en conjuntos de entrenamiento y test a partir de una fecha de corte fija.
  6. Escalado de los datos (si el modelo lo requiere) y entrenamiento con diferentes algoritmos.
  7. Evaluación del rendimiento usando RMSE y visualización de resultados.

##  Modelos utilizados

- Linear Regression  
- Support Vector Regressor (SVR)  
- Random Forest Regressor  
- Otros modelos comparativos mediante GridSearchCV

##  Resultados

- Aumenta la incertidumbre conforme crece el horizonte de predicción.
- **SVR** se mantiene como el modelo más competitivo de forma generalizada.
- En algunos casos, modelos como **Random Forest** superan a SVR, aunque no de forma sistemática.
- La regresión lineal mostró limitaciones claras con lag 15, reflejando errores elevados.

##  Contenido del notebook

- Limpieza y preparación de datos por empresa
- Generación de features desplazados y móviles
- Entrenamiento por empresa
- Evaluación de errores (RMSE)
- Visualización de resultados por modelo
