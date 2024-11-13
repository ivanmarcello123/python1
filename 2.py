# Daftar buku yang tersedia di perpustakaan
daftar_buku = [
    "Python untuk Pemula",
    "Algoritma dan Struktur Data",
    "Pemrograman Web",
    "Data Science",
    "Kecerdasan Buatan"
]

# Menampilkan daftar buku yang tersedia
print("Daftar Buku yang Tersedia:")
for buku in daftar_buku:
    print(f"- {buku}")

# Menggunakan loop while untuk meminta input buku yang ingin dipinjam
while True:
    # Meminta pengguna untuk memasukkan judul buku yang ingin dipinjam
    judul_buku_pinjam = input("\nMasukkan judul buku yang ingin dipinjam (atau ketik 'keluar' untuk berhenti): ")

    # Jika pengguna mengetik 'keluar', keluar dari loop
    if judul_buku_pinjam.lower() == 'keluar':
        print("\nTerima kasih telah menggunakan layanan perpustakaan.")
        break

    # Mengecek apakah buku yang dimasukkan ada dalam daftar buku
    if judul_buku_pinjam in daftar_buku:
        # Menghapus buku yang dipinjam dari daftar
        daftar_buku.remove(judul_buku_pinjam)
        print(f"\nBuku '{judul_buku_pinjam}' berhasil dipinjam!")
        break  # Keluar dari loop setelah buku berhasil dipinjam
    else:
        print("\nBuku yang Anda cari tidak tersedia. Silakan coba lagi.")

# Menampilkan daftar buku yang masih tersedia setelah peminjaman
print("\nDaftar Buku yang Tersedia Setelah Peminjaman:")
if daftar_buku:
    for buku in daftar_buku:
        print(f"- {buku}")
else:
    print("Tidak ada buku yang tersisa.")
