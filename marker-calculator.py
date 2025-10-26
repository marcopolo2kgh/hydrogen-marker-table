import pandas as pd

# wczytaj fragment bazy NIST
data = pd.read_csv("nist-sample.csv")

def find_wavelength(upper, lower):
    transition = f"{upper}->{lower}"
    row = data[data["Transition"] == transition]
    if not row.empty:
        return float(row["Wavelength (nm)"].values[0])
    return None

def marker(upper, lower, wavelength):
    # tu możesz wstawić własny algorytm Marker calculus
    # na razie tylko różnica orbit jako przykład
    return upper - lower

# przykład użycia
upper = 18
lower = 9
wavelength = find_wavelength(upper, lower)
print("λ =", wavelength, "nm")
print("Marker =", marker(upper, lower, wavelength))
