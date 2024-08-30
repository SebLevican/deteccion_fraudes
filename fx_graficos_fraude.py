import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def fx_grafico_barra_simple(variable, dataframe, nombre_eje_x, nombre_eje_y, titulo_grafico, tamano_etiqueta_datos, bool_nuevo_eje_x, lista_nuevo_eje_x):
    """Función para generar un gráfico de barra simple

    Args:
        variable (string): la variable a graficar
        dataframe (df): el dataframe a graficar
        nombre_eje_x (string): nombre del eje x
        nombre_eje_y (string): nombre del eje y
        titulo_grafico (string): titulo del gráfico
        tamano_etiqueta_datos (int): tamaño de la etiqueta de datos
        bool_nuevo_eje_x (bool): True o False, en caso de True se cambia el eje x por una lista que da el usuario, en caso de False se mantiene eje x original
        lista_nuevo_eje_x (list): lista con los nombre del nuevo eje x, en caso de haber escogido false, poner cualquier elemento en este argumento (se sugiere 0)
    """

    var = pd.Series(round(dataframe[variable].value_counts(normalize=True)*100,1))
    g = sns.barplot(x=var.index, y=var.values)
    plt.xlabel(nombre_eje_x)
    plt.ylabel(nombre_eje_y)
    plt.title(titulo_grafico, fontweight='bold')
    for p in g.patches:
        g.annotate("%.1f" % p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()),
            ha='center', va='center', fontsize=tamano_etiqueta_datos, color='white', xytext=(0, 0),
            textcoords='offset points',bbox={'facecolor':'1', 'color':'Black', 'boxstyle':'round','pad':0.3})

    if bool_nuevo_eje_x:
        g.set_xticklabels(lista_nuevo_eje_x)
        plt.tight_layout()
        plt.show()
    else:
        plt.tight_layout()
        plt.show()


def fx_grafico_barra_subplots(dataframe, n_cols, tupla_figura, lista_variables, orden_bool, lista_orden, lista_nombre_eje_x, lista_titulos):
    """Función para generar gráficos de barra con subplots

    Args:
        dataframe (df): el dataframe a graficar
        n_cols (int): el número columnas deseado
        tupla_figura (tuple): una tupla con el tamaño de la figura deseado
        lista_variables (list): una lista con las variables a graficar
        orden_bool (bool): una lista con booleano True o False, según se desee o no cambiar el orden de la categoría del eje x en caso de variables categóricas, en caso de haber escogido false, poner cualquier elemento en este argumento (se sugiere 0)
        lista_orden (list): una lista con las clases de la variable a graficar, según el orden deseado en eje x en caso de variables categóricas
        lista_nombre_eje_x (list): una lista con los nombres de los ejes x deseados para cada variable
        lista_titulos (list): una lista con los nombres de los titulos de los gráficos
    """
    if len(lista_variables)%n_cols != 0:
        n_rows = int(len(lista_variables)/n_cols) + 1
    else:
        n_rows = int(len(lista_variables)/n_cols)

    fig, axes = plt.subplots(nrows=n_rows, ncols=n_cols, figsize=tupla_figura)

    for i, ax in zip(range(len(lista_variables)), axes.flatten()):
        if orden_bool[i]:
            orden_categorias = pd.Categorical(dataframe[lista_variables[i]], categories=lista_orden[i], ordered=True)
            # Ordenar el DataFrame según el orden específico
            dataframe[lista_variables[i]] = orden_categorias
            dataframe = dataframe.sort_values(lista_variables[i])

        s = pd.Series(round(dataframe[lista_variables[i]].value_counts(normalize=True)*100,1))

        g = sns.barplot(ax=ax, x=s.index, y=s.values)
        ax.set_xlabel(lista_nombre_eje_x[i])
        ax.set_ylabel('Porcentaje (%)')
        ax.set_title(lista_titulos[i], fontweight='bold')

        for p in g.patches:
            g.annotate("%.1f" % p.get_height(), (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', fontsize=10, color='white', xytext=(0, 0),
                textcoords='offset points',bbox={'facecolor':'1', 'color':'Black', 'boxstyle':'round','pad':0.3})

        diferencia = n_rows*n_cols - len(lista_variables)
        if diferencia > 0:
            for i in range(1, diferencia+1):
                fig.delaxes(axes.flatten()[-i])
        plt.tight_layout()


def fx_grafico_boxplot(dataframe, n_cols, tupla_figura, lista_variables, lista_nombre_eje_x, lista_titulos):
    """Función para generar de tipo boxplot

    Args:
        dataframe (df): el dataframe sobre el que se hará el gráfico
        n_cols (int): el número columnas deseado
        tupla_figura (tuple): una tupla con el tamaño de la figura deseado
        lista_variables (list): una lista con las variables a graficar
        posicion (tupla): posicion del estilo axes[0,0]
        lista_nombre_eje_x (list): una lista con los nombres de los ejes x deseados para cada variable
        lista_titulos (list): una lista con los nombres de los titulos de los gráficos
    """
    if len(lista_variables)%n_cols != 0:
        n_rows = int(len(lista_variables)/n_cols) + 1
    else:
        n_rows = int(len(lista_variables)/n_cols)

    fig, axes = plt.subplots(nrows=n_rows, ncols=n_cols, figsize=tupla_figura)

    for i, ax in zip(range(len(lista_variables)), axes.flatten()):
        g = sns.boxplot(ax=ax, x=dataframe[lista_variables[i]])
        ax.set_xlabel(lista_nombre_eje_x[i])
        ax.set_title(lista_titulos[i], fontweight='bold')
        diferencia = n_rows*n_cols - len(lista_variables)
    if diferencia > 0:
        for i in range(1, diferencia+1):
            fig.delaxes(axes.flatten()[-i])
    plt.tight_layout()