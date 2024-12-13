import csv
import math
import matplotlib.pyplot as plt

# Constants
a11 = -50.0
a21 = -19000.0
a22 = -21.5
ein = 1.5

def func1(v10):
    return a11 * v10 - a11 * ein

def func2(v10, v20):
    return a21 * v10 + a22 * v20 - a21 * ein

def main():
    h = 0.0002
    v10 = 0.0
    v20 = 0.0

    t_values = []
    v10_values = []
    v20_values = []

    with open("lab11.txt", "w") as ptrf1, open("lab12.txt", "w") as ptrf2:
        for i in range(1, 800):
            m11 = func1(v10)
            m12 = func1(v10 + m11 * h / 2)
            m13 = func1(v10 + m12 * h / 2)
            m14 = func1(v10 + m13 * h)
            v11 = v10 + ((m11 + 2 * m12 + 2 * m13 + m14) / 6) * h

            m21 = func2(v10, v20)
            m22 = func2(v10 + h / 2, v20 + m21 * h / 2)
            m23 = func2(v10 + h / 2, v20 + m22 * h / 2)
            m24 = func2(v10 + h, v20 + m23 * h)
            v21 = v20 + ((m21 + 2 * m22 + 2 * m23 + m24) / 6) * h

            v10 = v11
            v20 = v21
            t = h * i

            t_values.append(t)
            v10_values.append(v10)
            v20_values.append(v20)

            print(f"{v10}\t{v20}")
            ptrf1.write(f"\n{t}\t{v10}")
            ptrf2.write(f"\n{t}\t{v20}")

    # Plot the results
    plt.figure(figsize=(10, 6))

    # Plot for v10
    plt.subplot(2, 1, 1)
    plt.plot(t_values, v10_values, label="v10", color="blue")
    plt.xlabel("Time (t)")
    plt.ylabel("v10")
    plt.title("Runge-Kutta Simulation Results for v10")
    plt.grid()

    # Plot for v20
    plt.subplot(2, 1, 2)
    plt.plot(t_values, v20_values, label="v20", color="red")
    plt.xlabel("Time (t)")
    plt.ylabel("v20")
    plt.title("Runge-Kutta Simulation Results for v20")
    plt.grid()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
