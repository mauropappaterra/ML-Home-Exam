# Home Exam Machine Learning
# classRule.py
# Created by Mauro J. Pappaterra on 14 of May 2019.
import sonarmini as data

def classRule (dataset):
    """Given a dataset, returns number of correct/incorrect classification"""
    correct = 0
    incorrect = 0

    for data in dataset:
        newclass = 0
        console = "> Input: " + str(data) + "\n"

        if (data[1] < 0.05):
            newclass = 1

        console += "  New Classification -> " + str(newclass)

        if (data[2] == newclass):
            console += "\n  Correct Classification!\n"
            correct += 1
        else:
            console += "\n  Incorrect Classification!\n"
            incorrect += 1

        print(console)

    print ("\nCORRECT CLASSIFICATIONS: " + str(correct))
    print("INCORRECT CLASSIFICATIONS: " + str(incorrect))

classRule(data.sonarmini_class)