# Home Exam Machine Learning
# manhattan.py
# Created by Mauro J. Pappaterra on 13 of May 2019.
import sonarmini as data

def manhattan (a, b):
    """Given two 2D coordinate points A and B it calculates the Manhattan distance"""
    distance = abs(a[0] - b[0]) + abs(a[1] - b[1])
    return round(distance,5)

def all_distances (dataset, index):
    """Given a set of coordinates and an index returns all manhattan distances from all coordinates to
    the indexed coordinate"""
    a = dataset[index]
    result = []

    for i, coordinate in enumerate (dataset):
        result.append({'coordinate':coordinate,'index': i, 'distance': manhattan(a, coordinate)})

    return result

def closest3 (dataset, index):
    """Given a result array with all manhattan distances, it sorts it and returns the 3 closest coordinates"""
    manhattan_distances = all_distances(dataset,index)
    sort = sorted(manhattan_distances, key=lambda i: i['distance'])[1:4]

    for res in sort:
        print (str(res['coordinate']) + " Manhattan Distance: " + str(res['distance']))

closest3(data.sonarmini, 4)