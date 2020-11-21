from account import Account
from random import randint
from datetime import datetime

trial = 0


def printReceipt():
    noRecord = randint(100000, 1000000)
    time = datetime.now()

    print("""
Resi tercetak otomatis saat anda keluar.
Harap simpan tanda terima ini
sebagai bukti transaksi anda.

No. Rekord : %s
Tanggal : %s
Saldo akhir : %d
Terima kasih telah menggunakan ATM Progate!
""" % (noRecord, time, atm.getBalance()))


def printMainMenu():
    print("""
1 - Cek Saldo
2 - Ambil Saldo
3 - Tambah Saldo
4 - Ubah Pin
5 - Keluar
    """)


def mainProgram():
    print("Selamat datang di ATM Progate..")
    printMainMenu()

    while True:
        inputUser = int(input("Silakan pilih menu : "))

        if inputUser == 1:
            balance = atm.getBalance()
            print("Saldo anda sekarang: Rp.", balance)
            printMainMenu()
        elif inputUser == 2:
            balance = atm.getBalance()

            amount = int(input("Masukkan nominal saldo : "))

            if amount < 1:
                print("Jumlah yang diambil tidak boleh kurang dari 1")
                printMainMenu()
            else:
                verifyWithdraw = input(
                    "Konfirmasi: Anda akan melakukan debet dengan nominal berikut ? y/n %d " % amount)

                if verifyWithdraw == "y":
                    print("Saldo awal anda adalah : Rp.", balance)
                else:
                    break

                if balance < amount:
                    print("Maaf. Saldo anda tidak cukup untuk melakukan debet!")
                    print("Silakan lakukan penambahan nominal saldo")
                    printMainMenu()
                else:
                    atm.withdraw(amount)
                    balance = atm.getBalance()
                    print("Transaksi debet berhasil!")
                    print("Saldo sisa sekarang: Rp.", balance)
                    printMainMenu()

        elif inputUser == 3:
            amount = int(input("Masukkan nominal saldo: "))

            if amount < 1:
                print("Jumlah yang akan ditambahkan tidak boleh kurang dari 1")
                printMainMenu()
            else:
                verifyDeposit = input("Konfirmasi: Anda akan melakukan penyimpanan dengan nominal berikut ? y/n %d " % amount)

                if verifyDeposit == "y":
                    atm.topup(amount)
                    balance = atm.getBalance()
                    print("Saldo anda sekarang adalah: Rp.", balance)
                    printMainMenu()
                else:
                    break

        elif inputUser == 4:
            while True:
                oldPin = input("Masukkan PIN anda : ")

                if atm.checkPin(oldPin):
                    newPin = input("silakan masukkan pin baru: ")
                    atm.changePin(newPin)
                    print("pin anda berhasil diganti!")
                    verifyNewPin = input("coba masukkan pin baru:")
                    if atm.checkPin(verifyNewPin):
                        print("pin baru anda sukses!")
                    else:
                        print("maaf, pin anda salah! ")
                    printMainMenu()
                    break
                else:
                    print("pin anda salah, silakan masukkan pin:")

        elif inputUser == 5:
            printReceipt()
            exit()
        else:
            print("Error. Maaf, menu tidak tersedia")
            printMainMenu()


while trial < 3:
    if trial > 0:
        pin = input("Pin anda salah. Silakan Masukkan lagi: ")
    else:
        pin = input("Masukkan PIN anda : ")

    atm = Account()

    if atm.checkPin(pin):
        mainProgram()
        exit()
    else:
        if trial == 2:
            print("Error. Silahkan ambil kartu dan coba lagi")

        trial += 1
