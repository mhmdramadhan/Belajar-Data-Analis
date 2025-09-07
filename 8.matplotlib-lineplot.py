import matplotlib.pyplot as plt
import numpy as np

 
# data harga cabai dalam bentuk list
bulan = [1,2,3,4,5,6,7,8,9,10,11,12]
harga_cabai = [4677, 4800, 4950, 5100, 5250, 5400, 5550, 5700, 5850, 6000, 6150, 6300]

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
