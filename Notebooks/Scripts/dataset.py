# Función que recibe un archivo de texto y retorna
# los atributos y la clase en una tupla (lista, int)

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
