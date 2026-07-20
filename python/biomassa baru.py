# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 14:23:52 2026

@author: ASUS
"""

import matplotlib.pyplot as plt

# Data bulan dan biomassa serasah per stasiun
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Agustus', 'September', 'Oktober', 'November']
biomassa_stasiun = {
    'Stasiun 1': [0.063, 0.058, 0.048, 0.082, 0.094, 0.093, 0.096, 0.084],
    'Stasiun 2': [0.059, 0.069, 0.052, 0.080, 0.103, 0.094, 0.092, 0.088],
    'Stasiun 3': [0.066, 0.063, 0.053, 0.076, 0.088, 0.103, 0.089, 0.083],
    'Stasiun 4': [0.059, 0.062, 0.057, 0.051, 0.093, 0.088, 0.084, 0.073]
}

plt.figure(figsize=(10,6))

# Plot setiap stasiun
for stasiun, data in biomassa_stasiun.items():
    plt.plot(bulan, data, marker='o', linestyle='-', label=stasiun)

ax = plt.gca()

# Hilangkan hanya garis sumbu
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

# Label sumbu tetap ada
plt.xlabel("Bulan", fontsize=12)
plt.ylabel("Biomassa Serasah (gr/day)", fontsize=12)

# Legend tetap ada
plt.legend()

plt.show()