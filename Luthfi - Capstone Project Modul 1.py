
from prettytable import PrettyTable


# DATA PASIEN
data_pasien = {
    "P0001": {"nama": "Budi Santoso", "umur": 35, "jenis_kelamin": "L", "diagnosa": "Tifus"},
    "P0002": {"nama": "Siti Rahma", "umur": 30, "jenis_kelamin": "P", "diagnosa": "Diabetes Tipe 1"},
    "P0003": {"nama": "Adi Wijaya", "umur": 40, "jenis_kelamin": "L", "diagnosa": "Stroke"},
    "P0004": {"nama": "Rizky Wijaya", "umur": 17, "jenis_kelamin": "L", "diagnosa": "Patah Tulang"},
    "P0005": {"nama": "Dewi Lestari", "umur": 30, "jenis_kelamin": "P", "diagnosa": "Ibu Hamil"},
    "P0006": {"nama": "Farhan Ramadhan", "umur": 35, "jenis_kelamin": "L", "diagnosa": "Diabetes Tipe 2"}
}


# Function Menampilkan Tabel
def tampilkan_tabel(data):  
    table = PrettyTable()
    table.field_names = ["ID Pasien", "Nama", "Umur", "Jenis Kelamin", "Diagnosa"]
    table.align = "c"   

    for id_pasien, detail in data.items():
        table.add_row([
            id_pasien,
            detail["nama"],
            detail["umur"],
            detail["jenis_kelamin"],
            detail["diagnosa"]
        ])
    print("\n", table)


# VALIDASI INPUT Y/N
def input_yn(pesan):
    while True:
        pilihan = input(pesan).strip().lower()
        if pilihan in ["y", "n"]:
            return pilihan
        else:
            print("Input hanya boleh 'y' atau 'n'!")

def ulang_proses(pesan):  
    return input_yn(pesan) == "y"


# Function Read
def read_pasien():
    while True:
        print("\n=== Menu Cari Data Pasien ===")
        print("1. Tampilkan Semua Data Pasien")
        print("2. Cari Data Pasien")
        print("3. Kembali ke Menu Utama")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            if len(data_pasien) == 0:
                print("Data kosong!")
            else:
                tampilkan_tabel(data_pasien)

        elif pilihan == "2":
            print("\nCari berdasarkan: ID, Nama, Umur, Jenis Kelamin atau Diagnosa")
            kata_cari = input("Masukkan kata kunci pencarian: ").strip()

            if kata_cari == "":
                print("Kata kunci tidak boleh kosong!")
                continue

            hasil = {}
            kata_cari_lower = kata_cari.lower()
            kata_cari_upper = kata_cari.upper()
            kata_cari_words = kata_cari_lower.split()

            for id_pasien, detail in data_pasien.items():
                nama_lower = detail["nama"].lower()
                diagnosa_lower = detail["diagnosa"].lower()
                nama_match = all(word in nama_lower for word in kata_cari_words)
                diagnosa_match = all(word in diagnosa_lower for word in kata_cari_words)

                if (
                    kata_cari_lower in id_pasien.lower() or
                    nama_match or
                    kata_cari in str(detail["umur"]) or 
                    kata_cari_upper == detail["jenis_kelamin"] or
                    diagnosa_match
                ):
                    hasil[id_pasien] = detail

            if len(hasil) > 0:
                tampilkan_tabel(hasil)
            else:
                print("Pasien tidak ditemukan!")

        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid!")


# Function Create
def create_pasien():
    while True:
        print("\n=== Menu Tambah Data Pasien ===")
        if len(data_pasien) > 0:
            tampilkan_tabel(data_pasien)   
        else:
            print("Belum ada data pasien.")

        id_pasien = input("\nMasukkan ID Pasien Baru: ")
        if not id_pasien.startswith("P"):
            print("ID harus diawali huruf P!")
            if not ulang_proses("Ingin mengulang proses tambah pasien? (y/n): "):
                break
            continue

        angka = id_pasien[1:]
        if not angka.isdigit() or len(angka) > 6:
            print("Setelah P harus diikuti dengan Angka!")
            if not ulang_proses("Ingin mengulang proses tambah pasien? (y/n): "):
                break
            continue

        if id_pasien in data_pasien:
            print("ID sudah terdaftar!")
            if not ulang_proses("Ingin mengulang proses tambah pasien? (y/n): "):
                break
            continue

        nama = input("Masukkan Nama: ")
        if not nama.replace(" ", "").isalpha():   
            print("Nama hanya boleh huruf dan spasi!")
            if not ulang_proses("Ingin mengulang proses tambah pasien? (y/n): "):
                break
            continue

        umur_input = input("Masukkan Umur: ")
        if not umur_input.isdigit() or int(umur_input) <= 0:
            print("Umur harus angka > 0!")
            if not ulang_proses("Ingin mengulang proses tambah pasien? (y/n): "):
                break
            continue
        umur = int(umur_input)

        jenis_kelamin = input("Masukkan Jenis Kelamin (L/P): ").upper()
        if jenis_kelamin not in ["L", "P"]:
            print("Jenis kelamin harus L atau P!")
            if not ulang_proses("Ingin mengulang proses tambah pasien? (y/n): "):
                break
            continue

        diagnosa = input("Masukkan Diagnosa: ")
        if diagnosa.strip() == "":
            print("Diagnosa tidak boleh kosong!")
            if not ulang_proses("Ingin mengulang proses tambah pasien? (y/n): "):
                break
            continue

        print("\nData yang akan ditambahkan:")
        tampilkan_tabel({
            id_pasien: {
                "nama": nama,
                "umur": umur,
                "jenis_kelamin": jenis_kelamin,
                "diagnosa": diagnosa
            }
        })

        if input_yn("Simpan Data Pasien Baru? (y/n): ") == "y":
            data_pasien[id_pasien] = {
                "nama": nama,
                "umur": umur,
                "jenis_kelamin": jenis_kelamin,
                "diagnosa": diagnosa
            }
            print("Data berhasil disimpan!")

        if not ulang_proses("Tambah Data Pasien lagi? (y/n): "):
            break


# Function Update
def update_pasien():
    while True:
        print("\n=== Menu Perbarui Data Pasien ===")
        if len(data_pasien) == 0:
            print("Belum ada data pasien!")
            break

        tampilkan_tabel(data_pasien)
        id_pasien = input("Masukkan ID Pasien yang ingin diperbarui: ")

        if id_pasien in data_pasien:
            nama = input("Masukkan Nama baru: ")
            if not nama.replace(" ", "").isalpha():   
                print("Nama hanya boleh huruf dan spasi!")
                if not ulang_proses("Ulangi Pembaruan Data Pasien? (y/n): "):
                    break
                continue

            umur_input = input("Masukkan Umur baru: ")
            if not umur_input.isdigit() or int(umur_input) <= 0:
                print("Umur harus angka > 0!")
                if not ulang_proses("Ulangi Pembaruan Data Pasien? (y/n): "):
                    break
                continue

            jenis_kelamin = input("Masukkan Jenis Kelamin baru (L/P): ").upper()
            if jenis_kelamin not in ["L", "P"]:
                print("Jenis kelamin harus L atau P!")
                if not ulang_proses("Ulangi Pembaruan Data Pasien? (y/n): "):
                    break
                continue

            diagnosa = input("Masukkan Diagnosa baru: ")
            if diagnosa.strip() == "":
                print("Diagnosa tidak boleh kosong!")
                if not ulang_proses("Ulangi Pembaruan Data Pasien? (y/n): "):
                    break
                continue
            
            data_pasien[id_pasien] = {
                "nama": nama,
                "umur": int(umur_input),
                "jenis_kelamin": jenis_kelamin,
                "diagnosa": diagnosa
            }
            print("Data berhasil diperbarui!")
        else:
            print("ID tidak ditemukan!")

        if not ulang_proses("Ingin Memperbarui Data Pasien Lagi? (y/n): "):
            break


# Function Delete
def delete_pasien():
    while True:
        print("\n=== Hapus Data Pasien ===")
        if len(data_pasien) == 0:
            print("Belum ada data pasien!")
            break

        tampilkan_tabel(data_pasien)
        id_pasien = input("Masukkan ID Pasien yang ingin dihapus: ")

        if id_pasien in data_pasien:
            if input_yn("Yakin ingin menghapus? (y/n): ") == "y":
                del data_pasien[id_pasien]
                print("Data berhasil dihapus!")
        else:
            print("ID tidak ditemukan!")

        if not ulang_proses("Ingin Menghapus Data Pasien lagi? (y/n): "):
            break


# LOGIN
username_benar = "Rsadmin"
password_benar = "Admin123"
percobaan = 0
login_berhasil = False

while percobaan < 3:
    username = input("Masukkan username: ").strip()
    password = input("Masukkan password: ").strip()

    if username == username_benar and password == password_benar:
        print("Login berhasil!")
        login_berhasil = True
        break
    else:
        percobaan += 1
        if username != username_benar and password != password_benar:
            print(f"Login gagal ke-{percobaan}: Username dan Password salah!")
        elif username != username_benar:
            print(f"Login gagal ke-{percobaan}: Username salah!")
        elif password != password_benar:
            print(f"Login gagal ke-{percobaan}: Password salah!")

if not login_berhasil:
    print("Gagal login 3x. Anda telah keluar dari Sistem.")
    exit()


# MENU CRUD SETELAH LOGIN
def main_menu():
    while True:
        print("\n===== Data Pasien Rumah Sakit ABC =====")
        print("1. Cari Data Pasien")
        print("2. Tambah Data Pasien")
        print("3. Perbarui Data Pasien")
        print("4. Hapus Data Pasien")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            read_pasien()
        elif pilihan == "2":
            create_pasien()
        elif pilihan == "3":
            update_pasien()
        elif pilihan == "4":
            delete_pasien()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan sistem.")
            break
        else:
            print("Pilihan tidak valid!")

main_menu()