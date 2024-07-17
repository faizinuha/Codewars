import tkinter as tk
from tkinter import simpledialog, messagebox
from datetime import datetime
import json
import time

# Inisialisasi total uang kas dan daftar masukan
total_kas = 0
masukan_list = []

def save_to_file(data):
    """Menyimpan data ke dalam file robot.txt dengan format yang rapi."""
    with open('robot.txt', 'a') as file:
        file.write(data + '\n' + '-'*40 + '\n')

def load_kas():
    """Memuat total kas dari file robot.json."""
    try:
        with open('robot.json', 'r') as file:
            data = json.load(file)
            return data.get('total_kas', 0)
    except FileNotFoundError:
        return 0

def save_kas(total_kas):
    """Menyimpan total kas ke file robot.json."""
    with open('robot.json', 'w') as file:
        json.dump({'total_kas': total_kas}, file)

def remove_all_masukan():
    """Menghapus semua masukan dari file robot.txt dan reset total kas."""
    global total_kas
    try:
        with open('robot.txt', 'r') as file:
            lines = file.readlines()

        with open('robot.txt', 'w') as file:
            # Menulis ulang file tanpa masukan
            is_masukan_section = False
            for line in lines:
                if line.startswith("Masukan Uang Kas"):
                    is_masukan_section = True
                elif line.startswith("Pengeluaran Kas"):
                    is_masukan_section = False
                if not is_masukan_section:
                    file.write(line)
        total_kas = 0
        save_kas(total_kas)
        messagebox.showinfo("Success", "Semua masukan berhasil dihapus.")
    except FileNotFoundError:
        pass

def check_pin():
    """Fungsi utama untuk memeriksa PIN dan menyimpan data."""
    correct_pin = "1234"  # PIN yang benar
    max_attempts = 5      # Jumlah maksimum percobaan PIN
    wait_time = 10        # Waktu tunggu dalam detik setelah mencapai batas percobaan

    root = tk.Tk()
    root.withdraw()  # Menyembunyikan jendela utama

    while True:
        attempts = 0          # Inisialisasi jumlah percobaan
        canceled = False      # Variabel untuk melacak apakah proses dibatalkan

        while attempts < max_attempts:
            # Meminta PIN dari pengguna
            user_pin = simpledialog.askstring("PIN Required", "Masukkan PIN:", parent=root)

            # Memeriksa apakah pengguna membatalkan dialog
            if user_pin is None:
                canceled = True
                break

            # Memeriksa apakah PIN yang dimasukkan benar
            if user_pin == correct_pin:
                main_menu(root)
                break
            else:
                attempts += 1
                remaining_attempts = max_attempts - attempts
                if remaining_attempts > 0:
                    messagebox.showerror("Access Denied", f"PIN Salah. Percobaan tersisa: {remaining_attempts}")
                else:
                    messagebox.showerror("Access Denied", "PIN Salah. Akses Ditolak. Coba lagi setelah 10 detik.")
                    root.update()  # Memperbarui jendela untuk menampilkan pesan
                    time.sleep(wait_time)  # Menunggu selama waktu tunggu

        if canceled:
            messagebox.showinfo("Operation Cancelled", "Operasi dibatalkan oleh pengguna.")

        # Tanya kepada pengguna apakah ingin melanjutkan atau keluar
        continue_running = messagebox.askyesno("Continue", "Apakah Anda ingin melanjutkan?")
        if not continue_running:
            break

    root.quit()  # Menutup aplikasi setelah pengguna memilih untuk berhenti

def main_menu(root):
    global total_kas
    total_kas = load_kas()  # Memuat total kas dari file

    while True:
        # Menampilkan menu utama
        choice = simpledialog.askstring("Menu Utama", "Pilih opsi:\n1. Masukan Uang Kas\n2. Total Uang Kas\n3. Pengeluaran Kas\n4. Hapus Semua Masukan\n5. Keluar", parent=root)

        if choice == "1":
            masukan_uang_kas(root)
        elif choice == "2":
            total_uang_kas()
        elif choice == "3":
            pengeluaran_kas(root)
        elif choice == "4":
            hapus_semua_masukan()
        elif choice == "5":
            break
        else:
            messagebox.showerror("Invalid Choice", "Opsi tidak valid, silakan coba lagi.")

def masukan_uang_kas(root):
    global total_kas, masukan_list
    try:
        jumlah_uang = float(simpledialog.askstring("Masukan Uang Kas", "Masukkan jumlah uang kas:", parent=root))
        total_kas += jumlah_uang
        today_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data_to_save = (
            f"Masukan Uang Kas\n"
            f"Jumlah Uang: {jumlah_uang}\n"
            f"Tanggal: {today_date}\n"
            f"Total Kas: {total_kas}"
        )
        save_to_file(data_to_save)
        save_kas(total_kas)
        masukan_list.append(data_to_save)
        messagebox.showinfo("Success", "Jumlah uang kas berhasil dimasukkan.")
    except (TypeError, ValueError):
        messagebox.showerror("Invalid Input", "Input tidak valid, silakan masukkan angka.")

def total_uang_kas():
    global total_kas
    messagebox.showinfo("Total Uang Kas", f"Total uang kas saat ini: {total_kas}")

def pengeluaran_kas(root):
    global total_kas, masukan_list
    pengeluaran_total = 0
    data_to_save = "Pengeluaran Kas\n"
    today_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    for i in range(1, 4):  # Memungkinkan memasukkan hingga 3 barang
        try:
            nama_barang = simpledialog.askstring("Pengeluaran Kas", f"Nama Barang {i}:", parent=root)
            if nama_barang is None or nama_barang.strip() == "":
                break  # Keluar dari loop jika pengguna tidak memasukkan nama barang
            jumlah_barang = int(simpledialog.askstring("Pengeluaran Kas", f"Jumlah Barang {i}:", parent=root))
            harga_barang = float(simpledialog.askstring("Pengeluaran Kas", f"Harga Barang {i}:", parent=root))
            total_pengeluaran = jumlah_barang * harga_barang
            pengeluaran_total += total_pengeluaran

            data_to_save += (
                f"Nama Barang: {nama_barang}\n"
                f"Jumlah Barang: {jumlah_barang}\n"
                f"Harga Barang: {harga_barang}\n"
                f"Total Pengeluaran: {total_pengeluaran}\n"
                f"{'-'*40}\n"
            )

        except (TypeError, ValueError):
            messagebox.showerror("Invalid Input", "Input tidak valid, silakan masukkan angka.")
            return  # Keluar dari fungsi jika terjadi kesalahan input

    total_kas -= pengeluaran_total

    # Cek apakah total kas menjadi negatif
    if total_kas < 0:
        messagebox.showerror("Error", "Total kas menjadi negatif, semua masukan dan pengeluaran dibatalkan.")
        total_kas += pengeluaran_total  # Batalkan pengeluaran
        remove_all_masukan()  # Hapus semua masukan dari file
        masukan_list = []  # Kosongkan daftar masukan
    else:
        data_to_save += f"Tanggal: {today_date}\nTotal Pengeluaran: {pengeluaran_total}\nTotal Kas: {total_kas}"
        save_to_file(data_to_save)
        save_kas(total_kas)
        messagebox.showinfo("Success", "Pengeluaran kas berhasil dicatat.")

def hapus_semua_masukan():
    global total_kas, masukan_list
    confirm = messagebox.askyesno("Confirm", "Apakah Anda yakin ingin menghapus semua masukan?")
    if confirm:
        remove_all_masukan()
        masukan_list = []

if __name__ == "__main__":
    check_pin()
