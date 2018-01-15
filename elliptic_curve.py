# Test 1, revision 2
import numpy as np
import matplotlib.pyplot as plt

def main():
    a = -3
    b = 4

    y, x = np.ogrid[-5:5:100j, -5:5:100j]
    plt.contour(x.ravel(), y.ravel(), pow(y, 2) + x*y - pow(x, 3) - x * a - b, [0])
    plt.grid()
    plt.show()

if __name__ == '__main__':
    main()
