import os
import sys
import pickle
import pandas as pd

# Añadir ruta de funciones
ruta_funciones = "/Users/luciamenendezfernandez/Desktop/TFM lucia/src/lag1_funciones"
if ruta_funciones not in sys.path:
    sys.path.append(ruta_funciones)

from preprocessing import cargar_datos
from features import crear_variables_lag_y_temporales
from model_training import dividir_train_test, definir_modelos, entrenar_y_evaluar_modelos
from scaling import escalar_datos

def entrenar_y_guardar_modelo_empresa(path_csv, empresa, lag, modelo_nombre, fecha_corte, output_dir):
    df = cargar_datos(path_csv, empresa)
    df = crear_variables_lag_y_temporales(df, empresa=empresa)

    if lag != 1:
        df["Precio_cierre"] = df["Precio_cierre"].shift(-lag)
        df.dropna(inplace=True)

    X_train, y_train, _, _ = dividir_train_test(df, fecha_corte)
    
    if X_train.empty or len(X_train) < 3:
        print(f"  {empresa} - lag {lag} → no tiene suficientes datos. Se omite.")
        return

    if modelo_nombre == "SVR":
        X_train, _ = escalar_datos(X_train, X_train)

    all_models, all_param_grids = definir_modelos()
    models = {modelo_nombre: all_models[modelo_nombre]}
    param_grids = {modelo_nombre: all_param_grids[modelo_nombre]}

    best_name, best_model, best_rmse = entrenar_y_evaluar_modelos(
        X_train, y_train, X_train, y_train, models, param_grids
    )

    os.makedirs(output_dir, exist_ok=True)
    nombre_archivo = f"{empresa.replace(' ', '_')}_lag{lag}.pkl"
    ruta_guardado = os.path.join(output_dir, nombre_archivo)

    with open(ruta_guardado, "wb") as f:
        pickle.dump(best_model, f)

    print(f" {empresa} - lag {lag} → guardado en {ruta_guardado} | RMSE: {best_rmse:.4f}")

# MAIN
if __name__ == "__main__":
    ruta_csv = "/Users/luciamenendezfernandez/Desktop/TFM lucia/data/IBEX35_cotizaciones_20_Limpio.csv"
    fecha_corte = "2022-04-01"
    salida_modelos = "modelos_por_empresa"
    empresas = pd.read_csv(ruta_csv)["Empresa"].unique()
    lags = [1, 7, 15]

    for empresa in empresas:
        for lag in lags:
            modelo = "Linear Regression" if lag == 1 else "SVR"
            entrenar_y_guardar_modelo_empresa(ruta_csv, empresa, lag, modelo, fecha_corte, salida_modelos)
