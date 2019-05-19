# Home Exam Machine Learning
# sampleMean.py
# Created by Mauro J. Pappaterra on 19 of May 2019.

def sampleMean (data):
    """A non-recursive solution approach"""
    total = 0
    for n in data:
        total += n

    return total / len(data)

def sampleMeanRecursive (data, x):
    """A recursive solution approach"""
    if (x == 0): # base case
        mean = data[x]
    else: # recursive call
        mean = sampleMeanRecursive(data, x-1) + 1/(x + 1) * (data[x] - sampleMeanRecursive(data, x-1))

    return mean

answer = 1.6
data  = [0.4, 0.5, 0.3, 0.6, 0.5, 0.7, 0.5, 0.1, 0.5, 0.9, answer]

print(sampleMeanRecursive(data, len(data) - 1))
print(sampleMean(data))

print ("\nSolution value -> " + str(answer))