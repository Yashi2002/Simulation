import math

# Constants
a = 5
b = 3
m = 16

# Initialize variables
frequencies = [0] * 16
r0 = 45
chi_sptab = 24.96

def calculate_chi_square(frequencies, expected):
    chi_sq = 0
    for observed in frequencies:
        chi_sq += (observed - expected) ** 2 / expected
    return chi_sq

# Generate random numbers and count frequencies
for _ in range(100):
    rn = (a * r0 + b) % m
    r0 = rn
    frequencies[rn] += 1

# Print frequencies
print("The frequencies are:")
for i, freq in enumerate(frequencies):
    print(f"{i}: {freq}")

# Calculate Chi-Square value
expected_frequency = 100.0 / 16.0
chi_sq = calculate_chi_square(frequencies, expected_frequency)

print(f"\nThe calculated value of Chi-Square is {chi_sq:.2f}")

# Hypothesis testing
if chi_sptab > chi_sq:
    print("\nH0 is not rejected.")
else:
    print("\nH0 is rejected.")
