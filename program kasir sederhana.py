# Data barang
barang = [
    {"no": 1, "kode": "001", "nama": "air narmada", "stok": 10},
    {"no": 2, "kode": "002", "nama": "indomi goreng", "stok": 50},
    {"no": 3, "kode": "003", "nama": "buku imformatika", "stok": 20},
    {"no": 4, "kode": "004", "nama": "lasegar cap badak", "stok": 30},
]

# Data kasir
kasir = [
    {"kode": "001", "nama": "mamat"},
    {"kode": "002", "nama": "budi "},
    {"kode": "003", "nama": "wawan "},
]

# Fungsi untuk menampilkan barang
def tampilkan_barang():
    print("          TOKO ABADI SEJAHTERA           ")
    print("="*48)
    print("no | kode barang | nama barang | jumlah stok |")
    print("=" * 48)
    for item in barang:
        print(f"{item['no']}   {item['kode']}            {item['nama']}      {item['stok']}          ")
    print("=" * 48)

# Fungsi untuk menambah barang
def tambah_barang():
    no = len(barang) + 1
    kode = input("Masukkan kode barang: ")
    nama = input("Masukkan nama barang: ")
    stok = int(input("Masukkan jumlah stok: "))
    
    barang.append({"no": no, "kode": kode, "nama": nama, "stok": stok})
    print("Barang berhasil ditambahkan!")

# Fungsi untuk menghapus barang
def hapus_barang():
    tampilkan_barang()
    no_hapus = int(input("Masukkan nomor barang yang ingin dihapus: "))
    
    for item in barang:
        if item["no"] == no_hapus:
            barang.remove(item)
            print("Barang berhasil dihapus!")
            return
    
    print("Nomor barang tidak ditemukan.")

# Fungsi untuk update nama barang
def update_nama_barang():
    tampilkan_barang()
    no_update = int(input("Masukkan nomor barang yang ingin diupdate: "))
    
    for item in barang:
        if item["no"] == no_update:
            nama_baru = input("Masukkan nama barang baru: ")
            item["nama"] = nama_baru
            print("Nama barang berhasil diupdate!")
            return
    
    print("Nomor barang tidak ditemukan.")

# Fungsi untuk update stok barang
def update_stok_barang():
    tampilkan_barang()
    no_update = int(input("Masukkan nomor barang yang ingin diupdate: "))
    
    for item in barang:
        if item["no"] == no_update:
            stok_baru = int(input("Masukkan jumlah stok baru: "))
            item["stok"] = stok_baru
            print("Stok barang berhasil diupdate!")
            return
    
    print("Nomor barang tidak ditemukan.")

# Fungsi untuk menampilkan data kasir
def tampilkan_kasir():
    print("           KASIR        ")
    print("="*40)
    print("kode |         nama kasir           |")
    print("=" * 40)
    for item in kasir:
        print(f"{item['kode']}  | {item['nama']}        ")
    print("=" * 40)

# Fungsi untuk menambah kasir
def tambah_kasir():
    kode = input("Masukkan kode kasir: ")
    nama = input("Masukkan nama kasir: ")
    
    kasir.append({"kode": kode, "nama": nama})
    print("Kasir berhasil ditambahkan!")

# Fungsi untuk menghapus kasir
def hapus_kasir():
    tampilkan_kasir()
    kode_hapus = input("Masukkan kode kasir yang ingin dihapus: ")
    
    for item in kasir:
        if item["kode"] == kode_hapus:
            kasir.remove(item)
            print("Kasir berhasil dihapus!")
            return
    
    print("Kode kasir tidak ditemukan.")

# Fungsi untuk update kasir
def update_kasir():
    tampilkan_kasir()
    kode_update = input("Masukkan kode kasir yang ingin diupdate: ")
    
    for item in kasir:
        if item["kode"] == kode_update:
            nama_baru = input("Masukkan nama kasir baru: ")
            item["nama"] = nama_baru
            print("Nama kasir berhasil diupdate!")
            return
    
    print("Kode kasir tidak ditemukan.")

# Program utama
while True:
    print("\n   MENU  ")
    print("="*30)
    print("1. Tampilkan Barang")
    print("2. Tambah Barang")
    print("3. Hapus Barang")
    print("4. Update Nama Barang")
    print("5. Update Stok Barang")
    print("6. Tampilkan Kasir")
    print("7. Tambah Kasir")
    print("8. Hapus Kasir") 
    print("9. Update Kasir")
    print("0. Keluar")
    

    pilihan = input("Pilih menu satu sampai sembilan -_- ")
    print("="*30)

    if pilihan == "1":
        tampilkan_barang()
    elif pilihan == "2":
        tambah_barang()
    elif pilihan == "3":
        hapus_barang()
    elif pilihan == "4":
        update_nama_barang()
    elif pilihan == "5":
        update_stok_barang()
    elif pilihan == "6":
        tampilkan_kasir()
    elif pilihan == "7":
        tambah_kasir()
    elif pilihan == "8":
        hapus_kasir()
    elif pilihan == "9":
        update_kasir()
    elif pilihan == "0":
        print("Program selesai. Sampai jumpa!")
        break
    else:
        print("Pilihan tidak valid. Silakan pilih menu 0-9.")
