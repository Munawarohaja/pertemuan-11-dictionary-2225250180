def cari_mahasiswa(data, nim):
    return data.get(nim)

def rata_rata_nilai(data):
    if len(data) == 0:
        return 0
    total = 0
    for info in data.values():
        total += info["nilai"]
    return total / len(data)
data_mahasiswa = {
    "A001": {"nama": "Ayu", "kelas": "A", "nilai": 85},
    "A002": {"nama": "Budi", "kelas": "A", "nilai": 78},
    "A003": {"nama": "Citra", "kelas": "B", "nilai": 92},
    "A004": {"nama": "Deni", "kelas": "B", "nilai": 74},
    "A005": {"nama": "Eka", "kelas": "A", "nilai": 88}
}
print("--- UJI PENCARIAN ---")
nim_cari = "A003"
hasil = cari_mahasiswa(data_mahasiswa, nim_cari)
if hasil is not None:
    print(f"Data {nim_cari}: {hasil}")
else:
    print("Data tidak ditemukan")
nim_invalid = "A999"
if cari_mahasiswa(data_mahasiswa, nim_invalid) is None:
    print(f"NIM {nim_invalid}: Data tidak ditemukan")
data_mahasiswa["A006"] = {
    "nama": "Fajar",
    "kelas": "B",
    "nilai": 80
}
print("\nMahasiswa A006 berhasil ditambahkan.")
data_mahasiswa["A002"]["nilai"] = 82
print("Nilai A002 telah diperbarui menjadi 82.")
print("\n--- REKAP SELURUH MAHASISWA ---")
for nim, info in data_mahasiswa.items():
    print(f"NIM: {nim} | Nama: {info['nama']} | Kelas: {info['kelas']} | Nilai: {info['nilai']}")
rata = rata_rata_nilai(data_mahasiswa)
print("-" * 35)
print(f"Rata-rata nilai kelas = {rata:.2f}")