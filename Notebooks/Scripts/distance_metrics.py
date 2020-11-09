# Distancia Minkowski
def minkowski(vector1, vector2, p):
    distancia = 0.0
    for i in range(len(vector1)-1):
        distancia += abs(vector1[i] - vector2[i])**p

    return (distancia)**(1/p)

# Distancia Manhattan o L1
def sad(vector1, vector2):
    return minkowski(vector1, vector2, 1)

# Distancia Euclidiana o norma L2
def euclidean(vector1, vector2):
    return minkowski(vector1, vector2, 2)

# Distancia Chebyshev
def chebyshev(vector1, vector2):
    differences = []
    for i in range(len(vector1)-1):
        differences.append(abs(vector1[i] - vector2[i]))

    return max(differences)
