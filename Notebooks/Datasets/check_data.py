#  Funciones para realizar exploración de los conjuntos de datos

# Función que carga los datos y los convierte a un formato estándar
def load_data(file_object):
    dataset = list()
    for line in file_object:
        temp_list = [float(x) for x in line.split(",")]
        attribs = temp_list[:len(temp_list)-2]
        category = int(temp_list[len(temp_list)-1])

        # Apendizando el ejemplo
        dataset.append((attribs, category))

    return dataset

def open_file(path_to_file):
    # Abriendo el archivo
    return open(path_to_file, "r")

def open_dataset(path_to_file, verbose):
    file = open_file(path_to_file)
    dataset = load_data(file)

    if verbose:
        print("***************************************************")
        print("Cantidad de ejemplos en el conjunto: ", len(dataset))
        print("Cantidad de atributos:", len(dataset[0][0]))
        print("Ejemplo de instancia: ", dataset[0])

    return dataset

def class_distribution(dataset):
    classes = list(set([sample[1] for sample in dataset]))
    print("Número de clases: ", len(classes))
    class_freq = [0 for element in range(len(classes))]

    for sample in dataset:
        class_freq[sample[1]] += 1

    print(class_freq)

def check_data(train_path, test_path):
    # Se especifican las rutas al conjunto de entrenamiento y prueba
    dataset1_train = open_dataset(train_path, True)
    dataset1_test = open_dataset(test_path, True)

    # Conjunto de datos unido (para validación cruzada)
    dataset1_completo = dataset1_train + dataset1_test

    print("Distribución de clases en todo el conjunto")
    class_distribution(dataset1_completo)

    print("Distribución de clases en entrenamiento")
    class_distribution(dataset1_train)

    print("Distribución de clases en prueba")
    class_distribution(dataset1_test)


check_data("Datos-S-Entrena.txt", "S-Prueba.txt")
