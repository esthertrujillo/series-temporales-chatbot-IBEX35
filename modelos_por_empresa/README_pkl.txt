# README – Modelos entrenados por empresa y horizonte (archivos .pkl)

Esta carpeta contiene los modelos de predicción entrenados para cada empresa del IBEX 35, almacenados como archivos `.pkl`. Cada empresa tiene tres modelos correspondientes a distintos horizontes temporales (lag = 1, 7 y 15 días).

##  Estructura de archivos

Cada archivo sigue la siguiente convención de nombres:

<NOMBRE_EMPRESA>_lag<k>.pkl

Donde:
- `<NOMBRE_EMPRESA>` corresponde al nombre limpio de la empresa (sin espacios).
- `<k>` representa el horizonte de predicción en días:
  - `lag1`: predicción a 1 día
  - `lag7`: predicción a 7 días
  - `lag15`: predicción a 15 días

##  Uso de los modelos

Los modelos están listos para ser cargados en un entorno de ejecución y utilizados para hacer predicciones directamente sobre los datos preprocesados de cada empresa.
