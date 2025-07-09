# README – Predicción individual por empresa (Lag = 1)

Esta carpeta contiene una colección de notebooks, cada uno centrado en la **predicción del precio de cierre diario (lag = 1)** de una empresa específica del IBEX 35. Cada notebook aplica un pipeline estándar reutilizando funciones definidas en el módulo `lag1_funciones`.

##  Objetivo

Comparar el rendimiento de distintos modelos de machine learning en la predicción a corto plazo (1 día) de la evolución bursátil de cada empresa, evaluando el mejor modelo por separado para cada caso.

##  Estructura

Cada archivo `.ipynb` corresponde a una empresa distinta. 

##  Contenido de cada notebook

1. Carga y filtrado del dataset por nombre de empresa.
2. Generación de variables de tipo calendario, lags y medias móviles.
3. División en conjuntos de entrenamiento y prueba.
4. Entrenamiento de modelos con `GridSearchCV`:
   - Linear Regression
   - SVR
   - Random Forest
   - Otros modelos comparativos
5. Evaluación con RMSE.
6. Visualización comparativa entre valores reales y predichos.
7. Identificación del modelo con mejor rendimiento.

## Requisitos

- Python 3.8+
- Bibliotecas necesarias:
  - `pandas`, `numpy`, `scikit-learn`, `matplotlib`
- Acceso al módulo `src/lag1_funciones/` con las funciones importadas desde:
  - `preprocessing.py`, `features.py`, `model_training.py`, `scaling.py`, `visualization.py`

##  Comparación global de modelos

Además de los notebooks individuales por empresa, esta carpeta incluye un notebook especial (`modelo1_menor_rsme_medio.ipynb`) que:

- Aplica el pipeline de modelado a todas las empresas del IBEX 35.
- Evalúa todos los modelos definidos (Linear Regression, SVR, Random Forest, etc.).
- Calcula el **RMSE medio de cada modelo** en todas las series.
- Determina automáticamente el modelo con mejor rendimiento promedio.
- Permite visualizar y justificar cuál sería el modelo “global” óptimo para un sistema de predicción común.

Este enfoque es útil para decidir si conviene usar un único modelo para todo el índice o mantener modelos personalizados por empresa.
