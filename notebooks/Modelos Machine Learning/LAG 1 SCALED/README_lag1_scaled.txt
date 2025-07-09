# README – Predicción bursátil por empresa (Lag = 1)
Para reducir el numero de archivo de las pruebas anteriores (lag1) se han realizado las predicciones de las distintas empresas en un mismo notebook.
Este notebook implementa un flujo completo de predicción bursátil para una empresa concreta del IBEX 35, con un horizonte de **1 día (lag = 1)**. 
Utiliza funciones definidas en la carpeta `lag1_funciones` y automatiza todo el proceso desde la carga de datos hasta la visualización final.

##  Objetivo

Entrenar y evaluar un modelo de predicción individualizado para una empresa del IBEX 35, utilizando ingeniería de variables temporales y técnicas de aprendizaje automático, con especial atención al tratamiento de datos y la selección del modelo óptimo.

##  Funcionalidad

- Carga del dataset completo y filtrado por nombre de empresa.
- Creación de variables de tipo temporal (año, mes, día de la semana, etc.).
- Generación de lags, medias móviles y desviaciones estándar con desplazamiento de 1 día.
- División en conjuntos de entrenamiento y prueba (corte: 1 de abril de 2022).
- Escalado de variables si es necesario.
- Entrenamiento y evaluación de varios modelos (Linear Regression, SVR, Random Forest, etc.) mediante GridSearchCV.
- Visualización comparativa de predicciones vs datos reales.
- Impresión del mejor modelo y su RMSE final.

## Requisitos
Python 3.8+

pandas, numpy, scikit-learn, matplotlib

Acceso a funciones de la carpeta src/lag1_funciones/