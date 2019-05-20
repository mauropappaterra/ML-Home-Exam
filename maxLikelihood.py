# Home Exam Machine Learning
# maxLikelihood.py
# Created by Mauro J. Pappaterra on 20 of May 2019.
import sonarmini as data
import math

def average (data):
    """Given a dataset, calculates and returns the average value """
    total = 0
    for n in data:
        total += n

    return round(total / len(data),5)

def standardDeviation (data, mu, biased = False):
    """Given a dataset and an average value, calculates and returns the standard
    unbiased/biased deviation"""
    sum = 0

    for value in data:
        sum += (value - mu)**2

    if (biased):
        divisor = len(data) # biased
    else:
        divisor = (len(data) - 1) # unbiased (default)

    result = math.sqrt(sum / divisor)

    return round(result,5)

def mle (data, mu, sigma):
    """Given a dataset mu and sigma, returns the Maximum Likelihood Estimator (MLE)"""
    results = []

    for x in data:
        power = -1 / 2 * ((x - mu) / (sigma)) ** 2
        result = ((1 / (sigma * math.sqrt(2 * math.pi))) * math.e) ** power
        results.append(round(result,5))
    #print(results)
    return max(results)

def absolutDiff (a, b):
    """Given two values a and b returns the absolute difference"""
    return round(abs(a - b),5)

def main (data):
    mu = average(data)
    sigma = standardDeviation(data, mu)
    sigma_biased =  standardDeviation(data, mu, True)

    #print(mu)
    #print(sigma)
    #print(sigma_biased)

    mle_unbiased = mle(data,mu,sigma)
    mle_biased = mle(data,mu,sigma_biased)

    print("MLE Biased: " + str(mle_biased))
    print("MLE Unbiased: " + str(mle_unbiased))

    print("\nAbsolute Difference: " + str(absolutDiff(mle_biased, mle_unbiased)))

main (data.sonarmini_x)