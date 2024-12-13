import csv
import math
import matplotlib.pyplot as plt

# Constants
a11 = -50.0
a21 = -19000.0
a22 = -21.5
ein = 1.5
k1 = 0.008
k2 = 0.002

def func1(v10):
    return a11 * v10 - a11 * ein

def func2(v10, v20):
    return a21 * v10 + a22 * v20 - a21 * ein

def chem1(c1, c2, c3, t):
    return c1 + (k2 * c3 - k1 * c1 * c2) * t

def chem2(c1, c2, c3, t):
    return c2 + (k2 * c3 - k1 * c1 * c2) * t

def chem3(c1, c2, c3, t):
    return c3 + (2 * k1 * c1 * c2 - 2 * k2 * c3) * t

def main():
    # For the first simulation
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

    # Plot the first results
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

    # For the second simulation
    c1 = 25
    c2 = 50
    c3 = 0
    t = 0

    t_values_chem = []
    c1_values = []
    c2_values = []
    c3_values = []

    with open("lab1.csv", "w", newline="") as fp:
        writer = csv.writer(fp, delimiter='\t')

        while t < 10:
            temp_c1 = chem1(c1, c2, c3, 0.25)
            temp_c2 = chem2(c1, c2, c3, 0.25)
            temp_c3 = chem3(c1, c2, c3, 0.25)

            # Write to file
            writer.writerow([t, temp_c1, temp_c2, temp_c3])

            # Update values
            c1 = temp_c1
            c2 = temp_c2
            c3 = temp_c3
            t += 0.25

            t_values_chem.append(t)
            c1_values.append(c1)
            c2_values.append(c2)
            c3_values.append(c3)

    # Plot the second results
    plt.figure(figsize=(10, 6))
    plt.plot(t_values_chem, c1_values, label="c1", color="blue")
    plt.plot(t_values_chem, c2_values, label="c2", color="green")
    plt.plot(t_values_chem, c3_values, label="c3", color="red")
    plt.xlabel("Time (t)")
    plt.ylabel("Concentration")
    plt.title("Chemical Simulation Results")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    main()
