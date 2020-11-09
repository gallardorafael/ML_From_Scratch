# Bibliotecas
from statistics import mode
from Scripts.distance_metrics import * 

def euclidean_point(point, points):
    distances = list()
    for element in points:
        distances.append((euclidean(point, element[0]), element[1], element[0]))

    return distances

def minkowski_point(point, points, p):
    distances = list()
    for element in points:
        distances.append((minkowski(point, element[0], p), element[1], element[0]))

    return distances

def chebyshev_point(point, points):
    distances = list()
    for element in points:
        distances.append((chebyshev(point, element[0]), element[1], element[0]))

    return distances

def manhattan_point(point, points):
    distances = list()
    for element in points:
        distances.append((sad(point, element[0]), element[1], element[0]))

    return distances

# Función que calcula distancias de un punto a los restantes
def point_to_points(point, points, distance):
    if distance == 'euclidean':
        return euclidean_point(point, points)
    elif distance == 'minkowski':
        p = int(input("Valor p: "))
        return minkowski_point(point, points, p)
    elif distance == 'manhattan':
        return manhattan_point(point, points)
    elif distance == 'chebyshev':
        return chebyshev_point(point, points)
    else:
        return "ERROR: Elige una función de distancia válida."

# Función que retorna los k vecinos más cercanos al nuevo punto
def k_neighbors(new_point, dataset, k, metric):
    # Obteniendo las distancias
    distances = point_to_points(new_point, dataset, metric)
    distances.sort(key=lambda tup: tup[0])

    # Obteniendo los k mas cercanos
    neighbors = list()
    for i in range(k):
        neighbors.append(distances[i][1])

    return neighbors, mode(neighbors), distances[:k]


# Función que predice las clases para todas las muestras
# de un conjunto nuevo
def classify(train_data, test_data, k, metric):
    xy = [-1, -1]
    predicted = list()
    for sample in test_data:
        xy[0] = k_neighbors(sample[0], train_data, k, metric)[1]
        xy[1] = sample[1]
        predicted.append((xy[0], xy[1]))

    return predicted
