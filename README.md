# Exploración y Preprocesamiento de Datos para Detección de Fraude

Este proyecto se centra en la exploración, preprocesamiento y visualización de datos relacionados con la detección de fraudes en solicitudes financieras. A continuación se describe el proceso realizado:

## Instalación de Librerías

Se utilizan las siguientes librerías de Python:

- **Pandas**: Para la manipulación y análisis de datos.
- **Seaborn y Matplotlib**: Para la visualización de datos.
- **NumPy**: Para operaciones numéricas.
- **Scikit-learn**: Para la implementación de modelos de machine learning.
- **Imbalanced-learn**: Para manejar el desbalanceo de clases en los datos.
- **Pickle**: Para guardar y cargar objetos en Python.
- **Scipy**: Para realizar pruebas estadísticas.

Además, se han creado funciones personalizadas para la generación de gráficos y el entrenamiento de modelos, contenidas en los archivos `fx_graficos_fraude.py` y `fx_modelos.py`.

## Descripción del Proceso

1. **Carga de Datos:**
   - Se carga el dataset principal `Base.csv` y se imprime una vista previa del dataframe.

2. **Manejo de Valores Faltantes:**
   - Se reemplazan valores específicos (-1) por `NaN` en algunas columnas indicadas.
   - Se eliminan columnas con demasiados datos faltantes.
   - Se eliminan registros con valores `NaN`.

3. **Transformación de Datos:**
   - Se convierten clases numéricas a cadenas de texto para facilitar la visualización y el procesamiento de variables categóricas.
   - Se ajustan tipos de datos, como convertir variables `float` a `int` donde corresponda.

4. **Análisis Exploratorio de Datos (EDA):**
   - Se generan gráficos de barras y boxplots para analizar la distribución de variables categóricas y numéricas.
   - Se describe estadísticamente el conjunto de datos, tanto para variables categóricas como numéricas.

5. **Visualización:**
   - Se utilizan funciones personalizadas para generar subplots que permiten visualizar múltiples variables en un solo gráfico.
   - Se describen y titulan gráficos para facilitar la interpretación de los datos.

6. **Análisis de Variables Numéricas:**
   - Se identifican y analizan variables numéricas con menos de 12 valores únicos y más de 12 valores únicos por separado.
   - Se generan gráficos que permiten visualizar mejor la distribución de estas variables.

## Resultados

Después del preprocesamiento, el dataset original, que contaba con 1 millón de registros, se redujo significativamente debido a la eliminación de valores nulos. El resultado final es un dataframe con un  porcentaje considerable de datos válidos para continuar con el análisis y la modelización.

Este proceso es clave para garantizar que el modelo de machine learning posterior se entrene con datos limpios y representativos.

## Consideraciones

- Este análisis se realizó ignorando advertencias de librerías (warnings).
- Los gráficos se configuran utilizando el estilo de `Seaborn` y la paleta de colores `Set2`.

Para más detalles sobre la implementación de los modelos de machine learning o las funciones gráficas utilizadas, revisa los archivos `fx_graficos_fraude.py` y `fx_modelos.py`.

