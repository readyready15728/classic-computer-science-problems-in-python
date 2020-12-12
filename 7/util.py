from math import exp

def dot_product(xs, ys):
    return sum(x * y for x, y in zip(xs, ys))

def sigmoid(x):
    return 1 / (1 + exp(-x))

def derivative_sigmoid(x):
    s = sigmoid(x)
    return s * (1 - s)

def normalize_by_feature_scaling(dataset):
    for column_num in range(len(dataset[0])):
        column = [row[column_num] for row in dataset]
        maximum = max(column)
        minimum = min(column)

        for row_num in range(len(dataset)):
            dataset[row_num][column_num] = (dataset[row_num][column_num] - minimum) / (maximum - minimum)
