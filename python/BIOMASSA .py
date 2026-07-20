# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 14:23:52 2026

@author: ASUS
"""

import matplotlib.pyplot as plt

# Data bulan dan biomassa serasah per stasiun
bulan = ['January', 'February', 'March', 'April', 'August', 'September', 'October', 'November']
biomassa_stasiun = {
    'Station 1': [0.188, 0.175, 0.145, 0.281, 0.281, 0.280, 0.287, 0.251],
    'Station 2': [0.176, 0.207, 0.155, 0.241, 0.310, 0.281, 0.276, 0.256],
    'Station 3': [0.199, 0.188, 0.160, 0.229, 0.265, 0.309, 0.267, 0.249],
    'Station 4': [0.177, 0.187, 0.170, 0.153, 0.278, 0.265, 0.252, 0.218]
}

plt.figure(figsize=(10,6))

# Plot setiap stasiun
for stasiun, data in biomassa_stasiun.items():
    plt.plot(bulan, data, marker='o', linestyle='-', label=stasiun)

ax = plt.gca()

# Membuat garis sumbu X dan Y samar
ax.spines['bottom'].set_color('lightgray')
ax.spines['left'].set_color('lightgray')
ax.spines['bottom'].set_linewidth(0.8)
ax.spines['left'].set_linewidth(0.8)

# Hilangkan garis atas dan kanan
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

# Label sumbu tetap ada
plt.xlabel("Month", fontsize=12)
plt.ylabel("Litter Biomass (g/day)", fontsize=12)

# Legend tetap ada
plt.legend()

plt.show()