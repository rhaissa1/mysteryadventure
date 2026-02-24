import time

def dram_print(text):
    print(text)
    time.sleep(0.5)

def game_utama():
    dram_print("--- MEMULAI PETUALANGAN DIGITAL ---")
    nama = input("Siapa namamu? ")

    nyawa = 100
    progress = 0
    dram_print(f"Halo, {nama}. Kamu memasuki sebuah lorong misterius. Jangan langsung menang/kalah—jelajahi dulu.")

    # Game loop: pemain harus membuat beberapa keputusan baik untuk keluar
    while nyawa > 0 and progress < 3:
        dram_print("Kamu berada di persimpangan. Dua jalur tampak menyala: 'left' atau 'right'.")
        choice = input("Pilih jalur (left/right): ").strip().lower()

        if choice == 'left' or choice == 'l':
            dram_print("Kamu berjalan ke lorong beraroma manis—'ice cream corridor'.")
            dram_print("Di ujung ada dua opsi: 'follow music' atau 'inspect bench'.")
            sub = input("Pilih tindakan (music/bench): ").strip().lower()
            if sub == 'music' or sub == 'follow music':
                dram_print("Suara musik membawa kamu ke sebuah ruang tenang. Kamu menemukan jalan rahasia.")
                progress += 1
            elif sub == 'bench' or sub == 'inspect bench':
                nyawa -= 20
                dram_print("Bangku tersebut rapuh dan menjatuhkanmu ke lubang kecil. Nyawa -20.")
                dram_print(f"Sisa nyawa: {nyawa}")
            else:
                dram_print("Tindakan tidak dimengerti; tidak ada akibat besar, lanjutkan.")

        elif choice == 'right' or choice == 'r':
            dram_print("Kamu melangkah ke lorong hangat—'chocolate lava corridor'.")
            dram_print("Ada 'careful path' dan 'rush forward'.")
            sub = input("Pilih tindakan (careful/rush): ").strip().lower()
            if sub == 'careful' or sub == 'careful path':
                dram_print("Kamu berhati-hati dan menemukan batu dingin untuk diinjak—jalan lanjut terbuka.")
                progress += 1
            elif sub == 'rush' or sub == 'rush forward':
                nyawa -= 20
                dram_print("Kamu tergelincir dekat lava cokelat; terbakar sedikit. Nyawa -20.")
                dram_print(f"Sisa nyawa: {nyawa}")
            else:
                dram_print("Pilihan tak dimengerti; lorong bergetar tapi kamu tetap aman.")

        else:
            dram_print("Pilihan tidak jelas. Coba ketik 'left' atau 'right'.")

        # memberi kesempatan pemain untuk istirahat kecil
        if nyawa > 0:
            dram_print("Kamu bisa melanjutkan atau mengetik 'status' untuk melihat keadaanmu.")
            extra = input("Lanjutkan atau status? (enter/status): ").strip().lower()
            if extra == 'status':
                dram_print(f"Nama: {nama} | Nyawa: {nyawa} | Kemajuan: {progress}/3")

    if nyawa <= 0:
        dram_print("Nyawamu habis. Petualangan berakhir.")
    else:
        dram_print("Setelah beberapa langkah hati-hati, kamu menemukan sebuah pintu keluar tersembunyi.")
        dram_print("Kamu selamat kali ini — tapi petualangan belum berakhir. Terima kasih telah bermain.")

if __name__ == "__main__":
    game_utama()

