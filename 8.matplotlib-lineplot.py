import matplotlib.pyplot as plt
import numpy as np

 
# data harga cabai dalam bentuk list
bulan = [1,2,3,4,5,6,7,8,9,10,11,12]
harga_cabai = [4677, 4900, 4800, 5100, 4950, 5400, 5250, 5700, 5550, 6000, 5850, 6300]

# mengatur konfigurasi default dari matplotlib
plt.rcParams['font.size'] = 14
plt.rcParams['font.family'] = 'serif'
plt.rcParams['figure.figsize'] = (10, 5)

# mengubah ukuran plot
plt.figure(figsize=(10, 5))

plt.plot(bulan, harga_cabai, label="Harga Cabai", color="red", marker="o", linestyle="dashed",
         markeredgecolor="blue",
         markersize="10",
         alpha=0.7)

plt.title("Harga Cabai Per-kg")
plt.xlabel("Bulan")
plt.ylabel("Harga Cabai")
plt.legend(loc="lower left")
plt.grid(True, linestyle="--", color="green")
plt.show()

