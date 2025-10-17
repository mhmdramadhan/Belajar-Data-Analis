import matplotlib.pyplot as plt

# Data harga beras per kg di tahun 2023 dalam bentuk list (sumber BPS)
bulan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
harga_beras = [11647, 11990, 12041, 12092, 12102, 12115, 12141, 12265, 13036, 13315, 13380, 13458]

plt.plot(bulan, harga_beras,
         marker='o',
         color='green',
         linestyle='--',
         label= 'Harga Beras'
         )


plt.title("Harga Beras PerKG Tahun 2023")
plt.xlabel("Bulan")
plt.ylabel("Rupiah")
plt.legend()
plt.grid(True)
plt.show()