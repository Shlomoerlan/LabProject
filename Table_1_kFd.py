import numpy as np
import pandas as pd

# Constants
v_F = 1e6  # Fermi velocity in graphene in m/s
hbar = 6.582e-16  # Reduced Planck's constant in eV·s


# Function to calculate all parameters based on input d
def calculate_parameters(d, kFd_ratio=1.54):
    # Convert d to meters
    d_m = d * 1e-9  # nm to meters

    # Calculate kF from the given condition kF * d ≈ 1.54
    kF = kFd_ratio / d_m  # in m^-1

    # Calculate n from kF: n = kF^2 / pi
    n = (kF ** 2) / np.pi * 1e-4  # Convert to cm^-2

    # Calculate lambda_F (Fermi wavelength)
    lambda_F = 2 * np.pi / kF * 1e9  # Convert to nm

    # Calculate EF (Fermi energy): EF = ħ * v_F * kF
    EF = hbar * v_F * kF * 1e3  # Convert to meV

    # Return all parameters in a dictionary
    return {
        "d (nm)": d,
        "kF (nm^-1)": kF * 1e-9,  # Convert to nm^-1
        "n (cm^-2)": "{:.2e}".format(n),  # Scientific notation
        "λ_F (nm)": lambda_F,
        "EF (meV)": EF
    }


# Example input values for d (nm)
d_values = [50, 100, 150, 250, 500, 1000]

# Calculate for each d value and store in a list
results1 = [calculate_parameters(d, kFd_ratio=1.54) for d in d_values]
results2 = [calculate_parameters(d, kFd_ratio=6.16) for d in d_values]
# Convert the list of results to a DataFrame for display
df1 = pd.DataFrame(results1)
df2 = pd.DataFrame(results2)

# Display the DataFrame
print('for kFd=1.54 : ')
print(df1)
print('for kFd=6.16 : ')
print(df2)
