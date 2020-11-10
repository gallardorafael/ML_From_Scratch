import numpy as np
import pandas as pd

# Función que imprime la matriz de confusión
def confusion_matrix(dataset, predictions):
    # Contando la cantidad de classes
    classes = list(set([sample[1] for sample in dataset]))

    # Creando la matriz de confusión
    matrix = np.zeros((len(classes),len(classes)), dtype=int)

    # Llenando la matriz de confusión
    for pair in predictions:
        if pair[0] == pair[1]:
            matrix[pair[0]][pair[1]] += 1
        else:
            matrix[pair[0]][pair[1]] += 1

    # Formateando la matriz
    df = pd.DataFrame(matrix, index=classes, columns=classes)
    df = df.rename_axis("Predicción", axis='columns')
    df = df.rename_axis("Real", axis='index')

    return df
