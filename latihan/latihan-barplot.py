import matplotlib.pyplot as plt

# Data harga beras per kg di tahun 2023 dalam bentuk list (sumber BPS)
bulan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
harga_beras = [11647, 11990, 12041, 12092, 12102, 12115, 12141, 12265, 13036, 13315, 13380, 13458]
suhu = [25,28.7,28,24,22,23,24,25,27,28,30,29]

# Ketikan kode anda disini:
plt.bar(bulan, harga_beras, color='orange')

rerata = sum(harga_beras) / len(harga_beras)
plt.axhline(y=rerata, color='green', linestyle='--', label='Rata-rata Tahunan Harga Beras')

plt.text(1, rerata+100, f"Rerata= Rp. {round(rerata)}")

for i, harga in enumerate(harga_beras, start=1):
  plt.text(i, harga+50, str(harga), color='black', fontsize=7, ha='center')

plt.ylim(11000, 14000)
plt.title("Harga Beras PerKG Tahun 2023")
plt.xlabel("Bulan")
plt.ylabel("Harga Beras (Rp)")
plt.grid(axis='y')
plt.legend()
plt.show()