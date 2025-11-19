import sys
import time
import os
from colorama import Fore, init

init(autoreset=True)

# lirik gabut
lirik = [
    "jangan lagi lagi",
    "kamu cari cari",
    "cucucukup aku saja",
    "",
    "engga engga engga dulu",
    "kalo bukan kamu",
    "sabab kamu bintang",
    "bawa cinta datang",
    "",
    "engga engga engga dulu",
    "pokoknya harus kamu",
    "satu yang kumau",
    "cuma harus kamu",
]

# warna teks
warna_teks = [Fore.BLUE, Fore.LIGHTGREEN_EX, Fore.CYAN, Fore.MAGENTA]

# DELAY antara baris
delay_baris = [1, 1, 1, 0.1, 1, 1.1, 1.2, 1.2, 0.28, 1, 1.1, 1, 1.2]

# TEKS TENGAH
try:
    cols = os.get_terminal_size().columns
except:
    cols = default = 80

# GASSKEUUNN...
for i, ganz in enumerate(lirik):
    teks = ""
    warna = warna_teks[i % len(warna_teks)]
    for char in ganz:
        teks += char
        lirik_ditengah = teks.center(cols)
        print(warna + lirik_ditengah, end="\r")
        sys.stdout.flush()
        time.sleep(0.04)
    lirik_ditengah = ganz.center(cols)

    print(warna + lirik_ditengah)
    sys.stdout.flush()
    time.sleep(delay_baris[i])
print(Fore.LIGHTRED_EX + "=> By_Ganz | Thanks <=".center(cols))
