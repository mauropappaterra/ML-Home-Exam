# Home Exam Machine Learning
# maxLikelihood.py
# Created by Mauro J. Pappaterra on 20 of May 2019.
import sonarmini as data
import math

def average (data):
    """Given a dataset, calculates the average value """
    total = 0
    for n in data:
        total += n

    return round(total / len(data),5)

def standardDeviation (data, mu, bias = False):
    """Given a dataset and an average value, calculates the standard unbias/bias deviation"""
    sum = 0

    for value in data:
        sum += (value - mu)**2

    if (bias):
        divisor = len(data)
    else:
        divisor = (len(data) - 1)

    result = sum / divisor
    result = math.sqrt(result)

    return round(result,5)

def mxl (data):
    mu = average(data)
    sigma = standardDeviation(data, mu)
    sigma_bias =  standardDeviation(data, mu, True)
    #print(mu)
    #print(sigma)

    maxs = 1

    for x in data:
        power = -1/2 * ((x - mu)/(sigma))**2
        result = ((1 / (sigma * math.sqrt(2*math.pi)))* math.e)** power

        maxs *= result

        print (result)

        print ( "MAX: " + str(round(maxs,5)))
    return 0
    #return p ** xi * (1 - p) ** (1 - xi)

def absolutDiff (a, b):
    return abs(a - b)

mxl (data.sonarmini_x)


