import numpy as np
import matplotlib.pyplot as plt

# Constants
h = 6.626e-34  # Planck constant, J·s
c = 3.0e8      # Speed of light, m/s
k_B = 1.381e-23 # Boltzmann constant, J/K
sum_temp = 5778

cls_len = np.array([410, 475, 685])  # violet, blue, red wavelengths

def blackbody_radiation_intensity(T, wavelength):
    """
    Calculate blackbody radiation intensity for a given temperature T and wavelength.
    T: Temperature in Kelvin
    wavelength: Wavelength in nanometers
    """
    wavelength = wavelength * 1e-9  # Convert wavelength to meters
    term1 = (2 * h * c**2) / (wavelength**5)
    term2 = 1 / (np.exp((h * c) / (wavelength * k_B * T)) - 1)
    intensity = term1 * term2
    return intensity

def plot_blackbody_spectrum(T):
    wavelengths = np.linspace(100, 3000, 1000)  # Wavelengths in nanometers
    intensities = blackbody_radiation_intensity(T, wavelengths)
    cls_intensities = blackbody_radiation_intensity(T, cls_len)

    plt.figure(figsize=(8, 6))
    plt.plot(wavelengths, intensities, color='blue')
    plt.scatter(cls_len, cls_intensities, color='red')

    # Add vertical lines for visible light range (400 nm to 700 nm)
    plt.axvline(x=380, color='green', linestyle='--', label="Visible light range")
    plt.axvline(x=780, color='green', linestyle='--')

    plt.title(f"Blackbody Radiation Spectrum at T = {T} K")
    plt.xlabel("Wavelength (nm)")
    plt.ylabel("Radiation Intensity (W/m^2·nm)")
    plt.grid(True)
    plt.legend()
    plt.show()

if __name__ == "__main__":
    plot_blackbody_spectrum(sum_temp)
