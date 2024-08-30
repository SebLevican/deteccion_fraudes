from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split
import pickle
import numpy as np
import pandas as pd


def fx_train_test_split(dataframe):
    """Función para dividir la data, manteniendo la proporción de clases
    del vector objetivo en train y test

    Args:
        dataframe (df): El dataframe

    Returns:
        objetos: devuelve los objetos X_train, X_test, y_train e y_test
    """
    X = dataframe.drop('fraud_bool', axis=1)
    y = dataframe['fraud_bool']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=y, random_state=42) # Con stratify mantenemos la proporción 99% clase 0 y 1% clase 1
    return X_train, X_test, y_train, y_test


def fx_modelos_con_sin_balanceo_clases(lista_nombres_modelos, modelo, lista_X_train, lista_y_train):
    """Función para iterar dentro de un modelo según ajuste o no del balanceo de clases

    Args:
        lista_nombres_modelos (list):lista con nombre de modelos
        modelo (object scikit-learn): objeto scikit-learn del modelo: ej. GaussianNB()
        lista_X_train (list): lista de variables X_train
        lista_y_train (list): lista de variables y_train
    """

    for X_train, y_train, nombre_modelo in zip(lista_X_train, lista_y_train, lista_nombres_modelos):
        # Entrenar el modelo
        modelo.fit(X_train, y_train)

        # Guardar modelo en un archivo serializado
        with open(f'./modelos/{nombre_modelo}.pkl', 'wb') as archivo:
            pickle.dump(modelo, archivo)


def fx_metricas(nombre_archivo_modelo, tipo_modelo, X_test, y_test):
    """
    Función que genera las métricas de desempeño del modelo a partir de un archivo
    serializado.

    Args:
        nombre_archivo_modelo (string): archivo modelo serializado formato pkl
        tipo_modelo(string): 2 opciones, "supervisados", "no_supervisados"
        X_test (variable): variable con X_test
        y_test (variable): variable con y_test

    Returns:
        metricas de desempeño del modelo:  accuracy, precision, recall, f1 y auc_roc
    """
    # Abrir el archivo serializado
    with open('./modelos/'+nombre_archivo_modelo, 'rb') as archivo:
        modelo = pickle.load(archivo)

    # Realizar predicciones en el conjunto de prueba
    if tipo_modelo == 'supervisado':
        y_pred = modelo.predict(X_test)
    elif tipo_modelo == 'no_supervisado':
        y_pred = pd.Series(modelo.predict(X_test)).replace({1:0, -1:1}) # -1 es anomalia y 1 es valor normal

    # métricas
    accuracy = round(accuracy_score(y_test, y_pred), 2)
    precision = round(precision_score(y_test, y_pred), 2)
    recall = round(recall_score(y_test, y_pred), 2)
    f1 = round(f1_score(y_test, y_pred), 2)
    auc_roc = round(roc_auc_score(y_test, y_pred), 2)

    return accuracy, precision, recall, f1, auc_roc

