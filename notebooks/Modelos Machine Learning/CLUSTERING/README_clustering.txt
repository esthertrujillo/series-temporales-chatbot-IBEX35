# README – Notebook de pruebas para clustering de empresas (IBEX 35)

Este notebook explora y prueba el proceso de clustering aplicado a series temporales de precios de cierre de las empresas que componen el IBEX 35. Su objetivo es identificar patrones comunes entre empresas a partir de estadísticas extraídas de sus series históricas, con vistas a entrenar modelos agrupados por comportamiento.

##  Objetivo

Agrupar empresas del IBEX 35 en clústeres con características similares basadas en sus series temporales de cotización, como paso previo al modelado de series por grupo.

##  Metodología aplicada

1. **Carga y filtrado de datos**
   - Importación del dataset limpio de cotizaciones (`IBEX35_cotizaciones_20_Limpio.csv`).
   - Separación en DataFrames individuales por empresa.

2. **Cálculo de características estadísticas**
   Para cada serie de precios se calcula:
   - Media
   - Desviación estándar
   - Asimetría (*skewness*)
   - Curtosis
   - Mínimo y máximo

3. **Normalización**
   - Aplicación de `StandardScaler` para escalar las variables y facilitar el clustering.

4. **Aplicación del algoritmo K-Means**
   - Prueba con diferentes valores de `k` y visualización del método del codo.
   - Asignación de etiquetas de clúster a cada empresa.

5. **Visualización**
   - Heatmap del número de empresas por clúster.
   - Visualización de centroides y agrupaciones.

## Resultados esperados

- Agrupación de empresas con patrones similares de volatilidad o comportamiento estadístico.
- Identificación de posibles grupos para entrenar modelos conjuntos (por clúster) y reducir carga computacional.

##  Archivo asociado

- `pruebas_clustering.ipynb`: contiene todo el flujo experimental y visualizaciones.

##  Requisitos

- Python 3.8+
- Bibliotecas: `pandas`, `numpy`, `scikit-learn`, `matplotlib`, `seaborn`, `scipy`

## NOTA
 Los resultados de clustering se han fijado a la versión original para garantizar coherencia
  en los análisis posteriores. Se utiliza un archivo congelado con las variables y el modelo.
