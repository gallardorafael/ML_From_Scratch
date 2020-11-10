# Función que obtiene los clusters del dataset etiquetado
def get_clusters(data, verbose):
    dataset = data.copy()
    # Obteniendo las clases en el dataset
    classes = set([class_id[1] for class_id in dataset])

    # Creando la lista que almacenará los samples por cluster
    clusters = [[[], -2] for x in range(len(classes))]

    for i, sample in enumerate(dataset):
        for class_id in classes:
            if sample[1] == class_id:
                if class_id == -1:
                    # print(i, sample, "in", class_id)
                    clusters[class_id][0].append(i)
                    clusters[class_id][1] = -1
                else:
                    # print(i, sample, "in", class_id)
                    clusters[class_id][0].append(i)
                    clusters[class_id][1] = class_id

    if verbose:
        for i, clus in enumerate(clusters):
            if clus[1] == -1:
                print("Ruido:",clus[0],"\n")
            else:
                print("Cluster",i,":",clus[0],"\n")


    return [cluster[0] for cluster in clusters]

def add_labels(data):
    dataset = data.copy()
    new_dataset = []
    for i, element in enumerate(dataset):
        # Se elimina el dato de clase y se modifica por la etiqueta
        new_dataset.append([element[0], -2])

    return new_dataset

# Funciones para DBSCAN
def RangeQuery(DB, dist, Q, eps):
    N = []
    for P in DB:
        if dist(Q[0], P[0]) <= eps:
            N.append(P)
    return N

# Implementación de la función DBSCAN
# -2 es indefinido
# -1 es ruido
# 0 en adelante son clusters
def DBSCAN(DB, dist, eps, minPts):
    c = 0                                           # Etiqueta para el primer cluster
    for p in DB:                                    # Se itera sobre cada punto
        if p[1] != -2:                     # Se evitan puntos ya procesados
            continue
        N = RangeQuery(DB, dist, p, eps)            # Se obtienen los vecinos iniciales
        if len(N) < minPts:                         # Los puntos no-núcleo se consideran ruido
            p[1] = -1
            continue
        p[1] = c                                    # Se etiqueta P
        S = []
        S.extend(N)
        S.remove(p)                                 # Se expande el vecindario (sin P)
        for q in S:
            if q[1] == -2:
                q[1] = c
            elif q[1] != -2:
                continue
            q[1] = c
            N = RangeQuery(DB, dist, q, eps)
            if len(N) < minPts:                    # Se revisa que sea punto núcleo
                continue
            S.extend(N)
        c = c + 1                                   # Etiqueta del siguiente cluster
    return DB
