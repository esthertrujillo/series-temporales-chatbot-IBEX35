README - Módulo de funciones para predicción bursátil (lag = 1)

Este módulo contiene todas las funciones necesarias para llevar a cabo la predicción del precio de cierre de empresas del IBEX 35 usando modelos de aprendizaje automático con un horizonte temporal de 1 día (lag = 1).

Estructura de archivos:
------------------------

- preprocessing.py
  Funciones para carga y filtrado de datos:
    - cargar_datos(path_csv, empresa)

- features.py
  Generación de variables predictoras:
    - crear_variables_lag_y_temporales(df, empresa=None)

- model_training.py
  Funciones para división de datos y entrenamiento:
    - dividir_train_test(df, fecha_test="2022-04-01")
    - definir_modelos()
    - entrenar_y_evaluar_modelos(X_train, y_train, X_test, y_test, models, param_grids)

- scaling.py
  Escalado de variables predictoras:
    - escalar_datos(X_train, X_test)

- visualization.py
  Representación gráfica de resultados:
    - graficar_predicciones(y_test, y_pred, titulo=None)

Uso:
----

Importar las funciones desde un script o notebook y seguir los pasos:

1. Cargar y preparar los datos de una empresa
2. Crear variables temporales y desplazadas (lag)
3. Dividir en entrenamiento y test
4. Escalar si el modelo lo requiere
5. Entrenar y evaluar los modelos definidos
6. Visualizar las predicciones