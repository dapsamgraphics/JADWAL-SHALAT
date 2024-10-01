import requests
from colorama import init, Fore
import pyfiglet


# Inisialisasi colorama
init(autoreset=True)

# Kode ANSI untuk warna
warna_putih = '\033[37m'  # Kode untuk teks putih
reset = '\033[0m'         # Kode untuk reset warna
bg_black = '\033[40m'

# Fungsi untuk menampilkan jadwal sholat dalam format tabel yang menyerupai masjid
def tampilkan_jadwal(jadwal):
    print(f"{Fore.WHITE}#################%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*+++*++=++-==")
    print(f"{Fore.WHITE}###################%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%#%%%%%%%%%#*+*****++++++")
    print(f"{Fore.WHITE}#######%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%*#%%%%%%%#*+=++=====----")
    print(f"{Fore.WHITE}#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@#%%%%%%%%%%%%%%%%+#%%%%%%%#**=-======+--=")
    print(f"{Fore.WHITE}@@@@@%%%%%%%%%%%@@@@@@@@@@@@@@@@@@@@@=%@#%%%@%%%%@@@@%+#%%%%%%%#*#*==++==++=-+")
    print(f"{Fore.WHITE}@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=@@%@@@@@@@@@@@@@%#@@%%%%%%##%##**#*#****")
    print(f"{Fore.WHITE}@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@-@@%@@@@@@@@@@@@@##@@@@@@@@%%%###*+******")
    print(f"{Fore.WHITE}%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%=-:#%%@@@@@@@@@@@@##@@@@@@@@@%%###****+***")
    print(f"{Fore.WHITE}%%%@%@@@@@@@@@@@@@@@@@@@@@@@@@@@@#=+-=+++*@@@@@@@@@@@@%*@@@@@@@@@@@###***==***")
    print(f"{Fore.WHITE}%%%%%@@@@@@@@@@@@@@@@@@@@@@@@@%***#*******++#@@@@@@@@%*+#@@@@@@@@%%###**+**#*+")
    print(f"{Fore.WHITE}%%%%%%@@@@@@@@@@@@@@@@@@@@@@**+*+++++=======+++#@@@@@%#+#%@@@@@@%@%###**+*#***")
    print(f"{Fore.WHITE}%%%%%%%%%%@@@@@@@@@@@@@@@%*+*=+++=====----------=*@@%##**#@@@@@@%@%*****=++***")
    print(f"{Fore.WHITE}%%%%%%%%%%%%@@@@@@@@@@@@**++==+===-=------::::-----%@%#*+%@@@@%%%%@*###*++:*#*")
    print(f"{Fore.WHITE}%%%%%%%%%%%%%@@@@@@@@@@**+++-===----:::::::::::::---%##++@@@%%%%%@@*###*+-.=#*")
    print(f"{Fore.WHITE}%%%%%%%%%%%%%%%%@@@@@@*++++=------:::::::::::::::::-=##*+@@@%%%%%@@*###+*++**+")
    print(f"{Fore.WHITE}%%%%%%%%%%%%%%%@@@@@@%+++=====--===-------:-:::::::::*###@@@%%%@%*%**#*******+")
    print(f"{Fore.WHITE}%%%%%%%%%%%%%%@@@@@@@#**+=+-=-------::--:::::::::-::=-%##*%@@%%%##@**#**+====+")
    print(f"{Fore.WHITE}%%%%%%%%%%%%%%%%@@@@#+=-=++=-==-=-==++=-==----::::::::-%##@@@@%%##@***#**==-=+")
    print(f"{Fore.WHITE}%%%%%%%%%%%%%%%@@@@@#++=++----=-.::.:--..:.::::.:::::--***@@@@%%%#%**###%**+**")
    print(f"{Fore.WHITE}%%%%%%%%%%%%%@@@@@@@=+-.==::-==-::-----:::::::::..:...:=+#@@@%%%%@@#####+*####")
    print(f"{Fore.WHITE}%%%%%%%%%%%%@@@@@@@%=+++---:-==-:-:----::::::::::::::::=*#@@@%%%%@@####%%#:###")
    print(f"{Fore.WHITE}%%%%%%%%%%%@@@@@@@%*==++--:--==::::::--:::::::::.:..::::-#@@@@%%%@@######+:###")
    print(f"{Fore.WHITE}%%%%%%%%%%%@@@@@@@#*===-====+******#####******+=-:::::::-*@@@@%%%@@###%@####%#")
    print(f"{Fore.WHITE}%%%%%%%%%%%@@@@@###%@#*#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%*=#*+%@%%%%%#***%=====##")
    print(f"{Fore.WHITE}%%%%%@@@%%%%@%%@%@@@%#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%@#%@%%%%%%%#++*=#*:.::==")
    print(f"{Fore.WHITE}++#*+#++**++*++#**%#+*#+*##*#%**@%#%@*#%**##**##*#%**%#***+**++**+##*=*#:..:--")
    print(f"{Fore.WHITE}============+++++++++++++++*********##*****************+*+++++++++***=*#===---")
    print(f"{Fore.WHITE}++++++++++++++++++++++++++********#####*######**#****************+++*=*#-----")
    print(f"{Fore.WHITE}.%%%%%%...%%%%...%%%%%...%%...%%...%%%%...%%.......%%%%...%%..%%...%%%%...%%.......%%%%...%%%%%%.")
    print(f"{Fore.WHITE}.....%%..%%..%%..%%..%%..%%...%%..%%..%%..%%......%%......%%..%%..%%..%%..%%......%%..%%....%%...")
    print(f"{Fore.WHITE}.....%%..%%%%%%..%%..%%..%%.%.%%..%%%%%%..%%.......%%%%...%%%%%%..%%%%%%..%%......%%%%%%....%%...")
    print(f"{Fore.WHITE}.%%..%%..%%..%%..%%..%%..%%%%%%%..%%..%%..%%..........%%..%%..%%..%%..%%..%%......%%..%%....%%...")
    print(f"{Fore.WHITE}..%%%%...%%..%%..%%%%%....%%.%%...%%..%%..%%%%%%...%%%%...%%..%%..%%..%%..%%%%%%..%%..%%....%%...")
    # Mencetak jadwal sholat dengan tabel yang lebih rapi
    print(f"{bg_black}{warna_putih}-----------------------------------------------------{reset}")
    print(f"{bg_black}{warna_putih}   |    Waktu    |         Jadwal                   |{reset}")
    print(f"{bg_black}{warna_putih}----------------------------------------------------{reset}")
    print(f"{bg_black}{warna_putih}   |    Subuh    |          {jadwal['subuh']}                   |{reset}")
    print(f"{bg_black}{warna_putih}   |    Dzuhur   |          {jadwal['dzuhur']}                   |{reset}")
    print(f"{bg_black}{warna_putih}   |    Ashar    |          {jadwal['ashar']}                   |{reset}")
    print(f"{bg_black}{warna_putih}   |    Maghrib  |          {jadwal['maghrib']}                   |{reset}")
    print(f"{bg_black}{warna_putih}   |    Isya     |          {jadwal['isya']}                   |{reset}")
    print(f"{bg_black}{warna_putih}-----------------------------------------------------{reset}")
    banner = pyfiglet.figlet_format("Cypher",font="banner3-D")

# Fungsi untuk mendapatkan ID kota
def get_kota_id(nama_kota):
    response = requests.get(f'https://api.myquran.com/v2/sholat/kota/cari/{nama_kota}')
    data = response.json()
    return data['data'][0]['id'] if data['data'] else None

# Fungsi untuk mendapatkan jadwal sholat
def get_jadwal_sholat(kota_id):
    response = requests.get(f'https://api.myquran.com/v2/sholat/jadwal/{kota_id}/2024/10/01')
    data = response.json()
    return data['data']['jadwal']  # Pastikan mengakses data jadwal dengan benar

# Fungsi utama
def main():
    nama_kota = input('Masukkan nama kota: ')
    kota_id = get_kota_id(nama_kota)
    if kota_id:
        print(f'ID Kota: {kota_id}')
        jadwal = get_jadwal_sholat(kota_id)
        tampilkan_jadwal(jadwal)
    else:
        print('Kota tidak ditemukan.')

if __name__ == '__main__':
    main()
