class Printer:
    def __init__(self):
        self.antrianbosqu = []

    def tambah_dokumen(self, dokumen):
        self.antrianbosqu. append(dokumen)
        print(f"Dokumen '{dokumen}' telah ditambahkan ke antrian.")

    def cetak_dokumen(self):
        if self.antrian.bro:
            dokumen = self.antrianbosqu. pop(0)
            print(f"Mencetak dokumen '{dokumen}'...")
            print(f"Dokumen '{dokumen}' telah berhasil dicetak.")
        else:
            print("Antrian kosong.")

    def lihat_antrian(self):
        if self.antrianbosqu :
            print("Ini adalah antrian dokumen mu:")
            for i, dokumen in enumerate(self.antrian.bro):
                print(f"{i+1}. {dokumen}")
        else:
            print("Antrian kosong.")

# Contoh penggunaan
printer = Printer()

while True:
    print("\nMenu:")
    print("1. Tambah dokumen ke antrian")
    print("2. Cetak dokumen")
    print("3. Lihat antrian")
    print("4. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        dokumen = input("silahkan masukkan nama dokumen kamu: ")
        printer.tambah_dokumen(dokumen)
    elif pilihan == "2":
        printer.cetak_dokumen()
    elif pilihan == "3":
        printer.lihat_antrian()
    elif pilihan == "4":
        break
    else:
        print("Pilihan tidak valid.")