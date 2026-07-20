import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

# Data Musim Kemarau
stasiun = ['Stasiun 1', 'Stasiun 2', 'Stasiun 3', 'Stasiun 4']
variabel = ['Salinitas', 'Suhu', 'pH Tanah', 'BOT Tanah', 'Biomassa', 'Karbon']

data = np.array([
    [31.48, 31.00, 6.56, 9.36, 14.57, 6.85],
    [31.29, 30.86, 6.73, 11.03, 15.00, 7.05],
    [31.19, 30.90, 6.58, 12.29, 14.52, 6.83],
    [32.10, 31.14, 6.50, 18.91, 15.81, 7.43]
])

# Standarisasi data
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# PCA
pca = PCA(n_components=2)
principal_components = pca.fit_transform(data_scaled)
loadings = pca.components_.T
explained_variance = pca.explained_variance_ratio_ * 100
eigenvalues = pca.explained_variance_

# Tampilkan hasil numerik
print("Eigenvalues:")
print(eigenvalues)

print("\nExplained Variance Ratio (%):")
print(explained_variance)

pc_scores = pd.DataFrame(principal_components, columns=['PC1', 'PC2'], index=stasiun)
print("\nSkor PCA untuk tiap stasiun:")
print(pc_scores)

loadings_df = pd.DataFrame(loadings, columns=['PC1', 'PC2'], index=variabel)
print("\nLoadings (kontribusi variabel):")
print(loadings_df)

# Biplot
fig, ax = plt.subplots(figsize=(8, 6))
ax.axhline(0, color='black', linewidth=1, linestyle='--')
ax.axvline(0, color='black', linewidth=1, linestyle='--')

# Scatter stasiun
ax.scatter(principal_components[:, 0], principal_components[:, 1], color='blue', label='Stasiun')
for i, txt in enumerate(stasiun):
    ax.annotate(txt, (principal_components[i, 0], principal_components[i, 1]))

# Vektor variabel
for i, var in enumerate(variabel):
    ax.arrow(0, 0, loadings[i, 0], loadings[i, 1],
             color='red', alpha=0.7, head_width=0.05)
    ax.text(loadings[i, 0]*1.2, loadings[i, 1]*1.2, var,
            color='red', fontsize=10)

ax.set_xlabel(f"PC1 ({explained_variance[0]:.2f}%)")
ax.set_ylabel(f"PC2 ({explained_variance[1]:.2f}%)")
ax.set_title(f"Biplot PCA Musim Kemarau (Total Var: {sum(explained_variance):.2f}%)",
             fontsize=14, fontweight='bold')
ax.legend()
ax.grid(True, linestyle='--', alpha=0.6)

plt.show()

