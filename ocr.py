#!usr/bin/env python

DATA_DIR = './data'
TEST_DATA_FILENAME = f"{DATA_DIR}/t10k-images.idx3-ubyte"
TEST_LABELS_FILENAME = f"{DATA_DIR}/t10k-labels.idx1-ubyte"
TRAIN_DATA_FILENAME = f"{DATA_DIR}/train-images.idx3-ubyte"
TRAIN_LABELS_FILENAME = f"{DATA_DIR}/train-labels.idx1-ubyte"


def bytes_to_int(byte):
    return int.from_bytes(byte, "big")

def read_images(filename: str, n_max_images: int = None):
    images = []

    with open(filename, "rb") as file:
        file.read(4)
        n_images = bytes_to_int(file.read(4))

        if n_max_images: n_images = n_max_images

        n_rows = bytes_to_int(file.read(4))
        n_columns = bytes_to_int(file.read(4))

        for image_index in range(n_images):
            image = []
            for row_index in range(n_rows):
                row = []
                for col_index in range(n_columns):
                    pixel = file.read(1)
                    row.append(pixel)
                image.append(row)
            images.append(image)

       
    return images

def read_labels(filename: str, n_max_labels: int = None):
    labels = []

    with open(filename, "rb") as file:
        file.read(4)
        n_labels = bytes_to_int(file.read(4))

        if n_max_labels: n_labels = n_max_labels

        for label_index in range(n_labels):
            label = file.read(1)
            labels.append(label)
       
    return labels

def flatten_list(l):
    return [pixel for sublist in l for pixel in sublist]

def extract_features(X): 
    return [flatten_list(sample) for sample in X]

def knn(X_train, y_train, X_test, k: int = 3):
    y_pred = []

    return

def main():
    X_train = read_images(TRAIN_DATA_FILENAME)
    y_train = read_labels(TRAIN_LABELS_FILENAME)
    X_test = read_images(TEST_DATA_FILENAME)
    y_test = read_labels(TEST_LABELS_FILENAME)

    X_train = extract_features(X_train)
    X_test = extract_features(X_test)


if __name__ == "__main__":
    main()