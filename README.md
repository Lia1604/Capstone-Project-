# Capstone-Project-
Capstone Project Modul 1

Nama     : Luthfi
Program  : Data Science Online Batch - (JCDSAH-025)

Deskripsi Program
Program aplikasi menggunakan Python dengan fitur Utama CRUD (Create, Read, Update, dan Delete). Case study dalam program ini ialah Data Pasien Rumah Sakit.

Fitur Program
  1. Menu login dimana user harus menginmput username dan password dengan benar. Jika melakukan salah in 


Cara Menggunakan Progam 
  1. Login:  Gunakan username Rsadmin dan Password Admin123. Jika ada kesalahan dalam memasukan inputan akan muncul notifikasi bahwa inputan salah, Jika melakukan 3 kali salah input program akan berhenti. Jika berhasil akan masuk ke program.
  2. Read : Pilih 1 untuk menampilkan data pasien, akan ada pilihan ingin menampilkan keseluruhan data pasien atau dicari berdasarkan input key yang diinginkan. Pencarian data pasien dapat berupa huruf maupun angka. pencarian dengan huruf akan mencari berdasarkan ID pasien, nama, jenis kelamin dan diagnosa, jika memasukan angka akan dicari berdasarkan umur. Setelah itu akan memunculkan data pasien berdasarkan key input.
  3. Create : Pilih 2 untuk menambahkan data pasien. Disini ada beberapa validasi seperti ID pasien harus diawali dengan huruf P agar sama dengan ID pasien lain, lalu setelah huruf P harus diikuti dengan angka dan tidak boleh lebih dari enam angka. Validasi lain ialah nama hanya boleh huruf, umur hanya boleh angka dan lebih besar dari 0, jenis kelamin hanya boleh "L" atau "P", dan diagnosa tidak boleh kosong. Setelah itu akan menampilkan konfirmasi ingin menambahkan data pasien, jika iya data pasien baru akan tersimpan.
  4. Update : Pilih 3 untuk memperbarui data pasien. Disini akan diminta memasukkan ID Pasien untuk mewakili data mana yang akan diubah. Setelah itu masukkan input nama, umur, jenis kelamin dan diagnosa. Disini juga akan ada beberapa validasi seperti ketika menambahkan data pasien.
  5. Delete : Pilih 4 untuk menghapus data pasien. pilih ID pasien yang ingin dihapus lalu hapus data pasien tersebut. Validasi yang digunakan disini ialah inputan search tidak boleh kosong.
  6. Exit Program : Pilih 5 untuk keluar dari program.

Info Login
Username = Rsadmin
Password = Admin123

Cara Menjalankan Aplikasi
  Sebelum di-run, pastikan untuk install library tambahan yang digunakan:
  pip install prettytable
  
  lalu jalankan filenya: Luthfi - Capstone Project Modul 1.py
