# Fungsi untuk menghitung nilai akhir
def hitung_nilai_akhir(tugas, uts, uas):
    return (tugas * 0.2) + (uts * 0.4) + (uas * 0.4)

# Daftar untuk menyimpan data mahasiswa
mahasiswa = []

# Input data mahasiswa
jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))

for i in range(jumlah_mahasiswa):
    print(f"\nInput data mahasiswa ke-{i + 1}:")
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    tugas = float(input("Masukkan Nilai Tugas: "))
    uts = float(input("Masukkan Nilai UTS: "))
    uas = float(input("Masukkan Nilai UAS: "))

    # Menghitung nilai akhir
    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)

    # Menyimpan data mahasiswa dalam dictionary
    data_mahasiswa = {
        "nim": nim,
        "nama": nama,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "nilai_akhir": nilai_akhir
    }

    # Menambahkan data mahasiswa ke dalam list mahasiswa
    mahasiswa.append(data_mahasiswa)

# Menampilkan hasil data mahasiswa
print("\nData Mahasiswa:")
for mhs in mahasiswa:
    print(f"\nNIM: {mhs['nim']}")
    print(f"Nama: {mhs['nama']}")
    print(f"Nilai Tugas: {mhs['tugas']}")
    print(f"Nilai UTS: {mhs['uts']}")
    print(f"Nilai UAS: {mhs['uas']}")
    print(f"Nilai Akhir: {mhs['nilai_akhir']:.2f}")
