# README – Modelos clásicos (ARIMA y SARIMA)

Esta carpeta contiene notebooks individuales dedicados al modelado clásico de series temporales para distintas empresas del IBEX 35, aplicando técnicas como **ARIMA** y **SARIMA** sobre los precios de cierre diarios.

## Objetivo

Evaluar el rendimiento de modelos estadísticos clásicos en la predicción bursátil, como alternativa o complemento a los modelos de machine learning.

## Empresas analizadas

- ACCIONA  
- ACCIONA ENERGÍA  
- ARCELORMITTAL  
- INDITEX  
- INM. COLONIAL  
- AENA  
- BBVA  
- SANTANDER

Cada notebook se centra en una empresa y sigue una metodología común.

##  Metodología

1. **Carga y limpieza de datos**
   - Conversión de fechas
   - Ordenación cronológica
   - Eliminación de valores nulos

2. **Descomposición y exploración de la serie**
   - Identificación visual de tendencia y estacionalidad

3. **Estacionariedad**
   - Test de Dickey-Fuller aumentado (ADF)
   - Aplicación de diferenciación si es necesario

4. **Selección de parámetros**
   - Análisis de ACF y PACF
   - Configuración manual o automática con `auto_arima`

5. **Ajuste de modelos**
   - ARIMA (p, d, q)
   - SARIMA (p, d, q)(P, D, Q, m), con estacionalidad semanal o mensual

6. **Validación**
   - Análisis de residuos
   - Q-Q plot y gráficos de densidad
   - Comprobación de ruido blanco

7. **Evaluación**
   - Predicción sobre conjunto de test
   - Cálculo del error mediante RMSE

##  Resultados esperados

- Modelos como ARIMA pueden ofrecer buenos ajustes en series estables.
- SARIMA puede capturar estacionalidad semanal o mensual si existe.
- Sin embargo, las predicciones tienden a ser suavizadas, y pueden no capturar bien la volatilidad de los mercados financieros.

##  Requisitos

- Python 3.8+
- `pandas`, `numpy`, `matplotlib`, `statsmodels`, `pmdarima`


