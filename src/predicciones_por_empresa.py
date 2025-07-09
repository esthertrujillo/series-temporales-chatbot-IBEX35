import os
import sys
import pickle
import pandas as pd
import numpy as np
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error

# Ruta a funciones
ruta_funciones = "/Users/luciamenendezfernandez/Desktop/TFM lucia/src/lag1_funciones"
if ruta_funciones not in sys.path:
    sys.path.append(ruta_funciones)

from preprocessing import cargar_datos
from features import crear_variables_lag_y_temporales
from model_training import dividir_train_test
from scaling import escalar_datos
from visualization import graficar_predicciones

def predicciones(nombre_empresa, horizonte, path_csv, modelos_dir, fecha_corte="2022-04-01"):
    lag = int(horizonte)
    nombre_archivo = f"{nombre_empresa.replace(' ', '_')}_lag{lag}.pkl"
    modelo_path = os.path.join(modelos_dir, nombre_archivo)

    if not os.path.exists(modelo_path):
        raise FileNotFoundError(f" No se encuentra el modelo: {modelo_path}")

    with open(modelo_path, "rb") as f:
        modelo = pickle.load(f)

    df = cargar_datos(path_csv, nombre_empresa)
    df = crear_variables_lag_y_temporales(df, empresa=nombre_empresa)

    if lag != 1:
        df["Precio_cierre"] = df["Precio_cierre"].shift(-lag)
        df.dropna(inplace=True)

    X_train, y_train, X_test, y_test = dividir_train_test(df, fecha_test=fecha_corte)

    if isinstance(modelo, SVR):
        X_train, X_test = escalar_datos(X_train, X_test)

    y_pred = modelo.predict(X_test)
    graficar_predicciones(y_test, y_pred, titulo=f"{nombre_empresa} - lag {lag}")

    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    ultima_pred = y_pred[-1]
    print(f" RMSE para {nombre_empresa} con lag {lag}: {rmse:.4f}")
    print(f" Última predicción: {ultima_pred:.2f} €")

    return y_pred, y_test, rmse, ultima_pred
