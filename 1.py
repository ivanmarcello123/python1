## Mendefinisikan list NamaBuah
NamaBuah = []

# Menambahkan elemen ke dalam list
NamaBuah.append("jeruk")
NamaBuah.append("apel")
NamaBuah.append("salak")
NamaBuah.append("semangka")

# Menampilkan isi list
print("List awal:")
print(NamaBuah)

# Menambahkan elemen dari list Buah_import ke NamaBuah
Buah_import = ["blueberry", "blackcurrent", "persik"]
NamaBuah.extend(Buah_import)
print("\nSetelah extend dengan Buah_import:")
print(NamaBuah)

# Mengganti nilai item di list
print("\nGanti nilai item pertama dengan 'durian':")
NamaBuah[0] = "durian"
print(NamaBuah)

# Menghapus elemen 'durian' dari list
print("\nSetelah remove durian:")
NamaBuah.remove("durian")  # Menghapus 'durian' yang sudah ada
print(NamaBuah)

# Menghapus semua elemen dalam list Buah_import
print("\nSetelah clear Buah_import:")
Buah_import.clear()  # clear() akan menghapus semua elemen dalam list
print(Buah_import)  # Ini akan menampilkan list yang kosong: []

# Menghapus variabel Buah_import
print("\nSetelah del Buah_import:")
del Buah_import  # Menghapus seluruh objek Buah_import
try:
    print(Buah_import)  # Ini akan menyebabkan error karena Buah_import sudah dihapus
except NameError:
    print("Buah_import sudah dihapus.")  # Menangani error jika variabel sudah dihapus
