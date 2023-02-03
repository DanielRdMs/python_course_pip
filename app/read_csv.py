import csv
from typing import List


def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header = next(reader)
        dataset = []
        for column in reader:
            iterable = zip(header, column)
            country_dict = {key: value for key, value in iterable}
            dataset.append(country_dict)
        return dataset


if __name__ == '__main__':
    dataset = read_csv('data.csv')
    print(dataset)
