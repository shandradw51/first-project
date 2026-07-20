import matplotlib.pyplot as plt

# Data bulan dan biomassa serasah per stasiun
bulan = ['January', 'February', 'March', 'April', 'August', 'September', 'October', 'November']
biomassa_stasiun = {
    'Station 1': [2.825, 2.628, 2.177, 3.669, 4.213, 4.198, 4.303, 3.758],
    'Station 2': [2.635, 3.105, 2.326, 3.611, 4.647, 4.210, 4.139, 3.968],
    'Station 3': [2.987, 2.826, 2.400, 3.429, 3.978, 4.634, 4.002, 3.737],
    'Station 4': [2.650, 2.801, 2.550, 2.295, 4.173, 3.968, 3.774, 3.270]
}

plt.figure(figsize=(10,6))

# Plot setiap stasiun dengan gaya berbeda
for stasiun, data in biomassa_stasiun.items():
    plt.plot(bulan, data, marker='o', linestyle='-', label=stasiun)

plt.title("Mangrove litter Biomass", fontsize=14, fontweight='bold')
plt.xlabel("Month", fontsize=12)
plt.ylabel("Litter Biomass (gr/day)", fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

import matplotlib.pyplot as plt

# Data bulan dan biomassa serasah per stasiun
bulan_awal = ['January', 'February', 'March', 'April']
bulan_akhir = ['August', 'September', 'October', 'November']

biomassa_stasiun = {
    'Station 1': [2.825, 2.628, 2.177, 3.669, 4.213, 4.198, 4.303, 3.758],
    'Station 2': [2.635, 3.105, 2.326, 3.611, 4.647, 4.210, 4.139, 3.968],
    'Station 3': [2.987, 2.826, 2.400, 3.429, 3.978, 4.634, 4.002, 3.737],
    'Station 4': [2.650, 2.801, 2.550, 2.295, 4.173, 3.968, 3.774, 3.270]
}

plt.figure(figsize=(10,6))

# Plot setiap stasiun dengan warna berbeda untuk dua periode
colors = ['b', 'g', 'r', 'c']  # Warna untuk tiap stasiun
for i, (stasiun, data) in enumerate(biomassa_stasiun.items()):
    plt.plot(bulan_awal, data[:4], marker='o', linestyle='-', color=colors[i], label=f"{stasiun} (Jan-Apr)")
    plt.plot(bulan_akhir, data[4:], marker='o', linestyle='--', color=colors[i], label=f"{stasiun} (Agu-Nov)")

plt.title("Rata-rata Biomassa Serasah Perbulan", fontsize=14, fontweight='bold')
plt.xlabel("Bulan", fontsize=12)
plt.ylabel("Biomassa Serasah (Ton/Ha)", fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

import matplotlib.pyplot as plt

# Data bulan dan karbon serasah per stasiun
bulan = ['January', 'February', 'March', 'April', 'August', 'September', 'October', 'November']
karbon_stasiun = {
    'Station 1': [1.328, 1.235, 1.023, 1.724, 1.980, 1.973, 2.022, 1.766],
    'Station 2': [1.238, 1.460, 1.093, 1.697, 2.184, 1.979, 1.945, 1.865],
    'Station 3': [1.404, 1.328, 1.128, 1.612, 1.870, 2.178, 1.881, 1.757],
    'Station 4': [1.245, 1.316, 1.198, 1.079, 1.961, 1.865, 1.774, 1.537]
}

plt.figure(figsize=(10,6))

# Plot setiap stasiun dengan gaya berbeda
for stasiun, data in karbon_stasiun.items():
    plt.plot(bulan, data, marker='o', linestyle='-', label=stasiun)

plt.title("Carbon C", fontsize=14, fontweight='bold')
plt.xlabel("Month", fontsize=12)
plt.ylabel("Litter Carbon (gr/day)", fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# Data bulan dan karbon serasah per stasiun
bulan = ['January', 'February', 'March', 'April', 'August', 'September', 'October', 'November']
karbon_stasiun = {
    'Station 1': [1.328, 1.235, 1.023, 1.724, 1.980, 1.973, 2.022, 1.766],
    'Station 2': [1.238, 1.460, 1.093, 1.697, 2.184, 1.979, 1.945, 1.865],
    'Station 3': [1.404, 1.328, 1.128, 1.612, 1.870, 2.178, 1.881, 1.757],
    'Station 4': [1.245, 1.316, 1.198, 1.079, 1.961, 1.865, 1.774, 1.537]
}

# Standar error untuk masing-masing data (misalnya nilai acak sebagai contoh)
std_error = {
    'Station 1': [0.1, 0.12, 0.08, 0.15, 0.11, 0.09, 0.13, 0.10],
    'Station 2': [0.09, 0.11, 0.10, 0.14, 0.12, 0.10, 0.11, 0.09],
    'Station 3': [0.12, 0.10, 0.09, 0.13, 0.10, 0.12, 0.08, 0.11],
    'Station 4': [0.11, 0.09, 0.12, 0.10, 0.13, 0.11, 0.09, 0.10]
}

plt.figure(figsize=(10,6))

# Plot setiap stasiun dengan gaya berbeda dan error bar
for stasiun, data in karbon_stasiun.items():
    plt.errorbar(bulan, data, yerr=std_error[stasiun], marker='o', linestyle='-', label=stasiun, capsize=5)

plt.title("Rata-rata Karbon Serasah Mangrove", fontsize=14, fontweight='bold')
plt.xlabel("Bulan", fontsize=12)
plt.ylabel("Karbon Serasah (Gram/Hari)", fontsize=12)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()


