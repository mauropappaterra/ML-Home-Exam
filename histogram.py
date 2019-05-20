# Python
# histogram.py
# Created by Mauro J. Pappaterra on 14 of May 2019.
import matplotlib.pyplot as plt
import sonarmini as data
import numpy as np

def histogram_x1 (data):
    bin_1 = 0
    bin_2 = 0
    bin_3 = 0

    for entry in data:
        #print(str(entry))
        if (entry[0] <= 0.05000 ):
            bin_1 += 1
            continue
        if (entry[0] <= 0.10000):
            bin_2 += 1
            continue
        if (entry[0] <= 0.15000):
            bin_3 += 1
            continue

    # PRINT HISTOGRAM
    print ("\nHISTOGRAM X1")
    print("0.00000 to 0.05000 " + "|" * bin_1)
    print("0.05001 to 0.10000 " + "|" * bin_2)
    print("0.10001 to 0.15000 " + "|" * bin_3)

    return np.array([bin_1, bin_2, bin_3])

def histogram_x2 (data):
    bin_1 = 0
    bin_2 = 0
    bin_3 = 0

    for entry in data:
        #print(str(entry))
        if (entry[1] <= 0.08000 ):
            bin_1 += 1
            continue
        if (entry[1] <= 0.16000):
            bin_2 += 1
            continue
        if (entry[1] <= 0.24000):
            bin_3 += 1
            continue

    # PRINT HISTOGRAM
    print ("\nHISTOGRAM X2")
    print("0.00000 to 0.08000 -" + "|" * bin_1)
    print("0.08001 to 0.16000 -" + "|" * bin_2)
    print("0.16001 to 0.24000 -" + "|" * bin_3)

    return np.array([bin_1, bin_2, bin_3])

x1 = histogram_x1(data.sonarmini_x_y)
x2 = histogram_x2(data.sonarmini_x_y)

plt.hist2d(x1, x2, bins=3)
plt.show()