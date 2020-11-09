# Función que realiza el conteo de los elementos
# clasificados para cada clase
def count_samples(dataset, predictions):
    classes = list(set([sample[1] for sample in dataset]))
    class_count = [0 for x in range(len(classes))]

    # Revisando todas las predicciones y realizando el conteo
    for pred in predictions:
        class_count[pred[1]] += 1

    return classes, class_count

# Función que imprime la matriz de confusión
def confusion_matrix(dataset, predictions):
    classes, predictions_count = count_samples(dataset, predictions)
    print("\t\t"+" ".join(str([c for c in classes])))
