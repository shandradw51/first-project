import matplotlib.pyplot as plt

# Data bulan dan karbon serasah per stasiun
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Agustus', 'September', 'Oktober', 'November']
karbon_stasiun = {
    'Stasiun 1': [1.328, 1.235, 1.023, 1.724, 1.980, 1.973, 2.022, 1.766],
    'Stasiun 2': [1.238, 1.460, 1.093, 1.697, 2.184, 1.979, 1.945, 1.865],
    'Stasiun 3': [1.404, 1.328, 1.128, 1.612, 1.870, 2.178, 1.881, 1.757],
    'Stasiun 4': [1.245, 1.316, 1.198, 1.079, 1.961, 1.865, 1.774, 1.537]
}

plt.figure(figsize=(10,6))

# Plot setiap stasiun dengan gaya berbeda
for stasiun, data in karbon_stasiun.items():
    plt.plot(bulan, data, marker='o', linestyle='-', label=stasiun)

plt.title("Rata-rata Karbon C Serasah Mangrove", fontsize=14, fontweight='bold')
plt.xlabel("Bulan", fontsize=12)
plt.ylabel("Karbon Serasah (Gram/Hari)", fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Data stasiun dan karbon serasah di musim hujan dan kemarau
stasiun = ['Stasiun 1', 'Stasiun 2', 'Stasiun 3', 'Stasiun 4']
hujan = [0.64, 0.66, 0.68, 0.63]
kemarau = [0.98, 1.01, 1.02, 0.91]
std_error_hujan = [0.06, 0.05, 0.06, 0.06]
std_error_kemarau = [0.02, 0.03, 0.11, 0.03]

fig, ax = plt.subplots(figsize=(8, 6))

# Plot garis dengan error bar
ax.errorbar(stasiun, hujan, yerr=std_error_hujan, fmt='-o', label='Musim Hujan', color='blue', capsize=5)
ax.errorbar(stasiun, kemarau, yerr=std_error_kemarau, fmt='-s', label='Musim Kemarau', color='orange', capsize=5)

ax.set_ylabel("Karbon Serasah (Gram/Hari)")
ax.set_title("Rata-rata Karbon Serasah Mangrove di Musim Hujan dan Kemarau", fontsize=14, fontweight='bold')
ax.legend()
ax.grid(True, linestyle='--', alpha=0.6)

plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Data
stasiun = ['Stasiun 1', 'Stasiun 2', 'Stasiun 3', 'Stasiun 4']
mean_hujan = [1.3729, 1.4071, 1.45, 1.3386]
std_hujan = [0.33950, 0.30489, 0.34909, 0.36034]
mean_kemarau = [2.0857, 2.1429, 2.1657, 1.9314]
std_kemarau = [0.11118, 0.16132, 0.59852, 0.15942]

# Plot data dengan error bars
plt.figure(figsize=(8, 5))
plt.errorbar(stasiun, mean_hujan, yerr=std_hujan, marker='o', linestyle='-', color='b', label='Hujan', capsize=5)
plt.errorbar(stasiun, mean_kemarau, yerr=std_kemarau, marker='s', linestyle='--', color='r', label='Kemarau', capsize=5)

# Label dan judul
plt.xlabel("Stasiun")
plt.ylabel("Biomassa Serasah (Gram/Hari)")
plt.title("Rata-rata Biomassa Serasah Mangrove di Musim Hujan dan Kemarau")
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

# Tampilkan grafik
plt.show()


