# barplot adalah diagram batang
# scatter plot adalah diagram titik
import matplotlib.pyplot as plt
plt.style.use('tableau-colorblind10')

# Data harga beras per kg di tahun 2023 dalam bentuk list (sumber BPS)
bulan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
harga_beras = [11647, 11990, 12041, 12092, 12102, 12115, 12141, 12265, 13036, 13315, 13380, 13458]

plt.bar(bulan, harga_beras)
# buat batasan y axis
plt.ylim(11000, 14000)
# batasi x axis
# plt.xlim(1, 12)

# atur x ticks
plt.xticks(bulan)
# atur y ticks
plt.yticks([11000, 11500, 12000, 12500, 13000, 13500, 14000])

plt.title("Harga Beras PerKG Tahun 2023")
plt.xlabel("Bulan")
plt.ylabel("Rupiah")
plt.show()


