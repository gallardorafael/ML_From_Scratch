from Scripts.knn import classify

# Función que calcula la precisión
def accuracy(predictions, verbose):
    total_samples = len(predictions)
    correct = 0

    for i, pair in enumerate(predictions):
        if verbose:
            print("%d: Clase estimada: %d | Clase real: %d" %(i+1, pair[0], pair[1]))

        if pair[0] == pair[1]:
            correct += 1
    return correct / total_samples

# Función que divide el dataset en k folds
def get_k_folds(k, data):
    size = len(data)
    fold_size = size // k
    k_folds = list()
    print("Diviendo los datos en %d folds de tamaño %d" %(k, fold_size))

    begin = 0
    end = fold_size
    for i in range(k):
        k_folds.append(data[begin:end])
        begin += fold_size
        end += fold_size

    return k_folds

# Función que calcula y retorna la precision para los k_folds
def k_fold_cross_val(data, n_folds, k_neighbors, metric):
    # Obteniendo los k_folds
    k_folds = get_k_folds(n_folds, data)

    # Realizando las predicciones
    accuracies = []
    for i in range(n_folds):
        test = k_folds[i]
        train = [sample for n,fold in enumerate(k_folds) for sample in fold if n != i]
        predictions = classify(train, test, k_neighbors, metric)
        accuracies.append(accuracy(predictions, False))

    return accuracies
