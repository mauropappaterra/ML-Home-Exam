# Home Exam Machine Learning
# gradientDescent.py
# Created by Mauro J. Pappaterra on 19 of May 2019.

def gradDesc_x4 (x, step):
    """Gradient Descent for f(x) = x**4 with derivative df(x) = x*4"""
    gradient_value = x - step * (x * 4)
    return round(gradient_value,5)

x = 2 # initial value
step = 0.1 # step size
updates = 10 # number of iterations

i = 1
while (updates > 0):
    x = gradDesc_x4(x, step)
    print("Ite. " + str (i)+ " -> " + str(x))
    updates -= 1
    i+= 1