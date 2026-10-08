import socket
from colorama import Fore, Back, Style
import os
import requests

banner = r"""
__________               __            
\______   \ ____ ___.__.|  | _______   
 |    |  _//  _ <   |  ||  |/ /\__  \  
 |    |   (  <_> )___  ||    <  / __ \_
 |______  /\____// ____||__|_ \(____  /
        \/       \/          \/     \/ 
            Coded By 4B2A             
"""


def scan(ip, port):
    try:
        s = socket.socket()
        s.settimeout(2.0)
        s.connect((ip, port))

        s.send(b"\r\n")
        cevap = s.recv(1024).decode().strip()

        s.close()
        # Eğer port açıksa ama servis konuşmadıysa boş kalmasın diye varsayılan yazı veriyoruz
        return cevap if cevap else "Unknown Service (No Banner)"
    except:
        # Port kapalıysa None dönecek
        return None


def check_vulnerability(service_name):
    # Eğer servis ismi bilinmiyorsa API'yi boşa yormamak için kontrol ediyoruz
    if "Unknown Service" in service_name or not service_name:
        return None

    try:
        # Önce boşluklara göre ayırıp ilk kelimeyi alıyoruz (Örn: "OpenSSH_8.2" -> "OpenSSH_8.2")
        ilk_parca = service_name.split()[0]
        # Sonra alt tireye göre ayırıp ana ismi temizliyoruz (Örn: "OpenSSH_8.2" -> "OpenSSH")
        keyword = ilk_parca.split("_")[0].strip()

        # CIRCL güncel arama altyapısı API Endpoint'i
        # Yazım hatası düzeltildi ve API arama yolu güncel hale getirildi
        url = f"https://circl.lu{keyword}"

        response = requests.get(url, timeout=4)
        if response.status_code == 200:
            data = response.json()

            # API'den gelen veride zafiyet listesi varsa ilk 2 tanesini seçiyoruz
            if isinstance(data, list) and len(data) > 0:
                vulns = []
                for item in data[:2]:
                    cve_id = item.get("id", "N/A")
                    summary = item.get("summary", "No summary available.")
                    vulns.append(f"{cve_id}: {summary[:70]}...")
                return vulns
    except:
        pass
    return None


def boyka_menu():
    # 1. KURAL: Önce ekranı temizle
    os.system("cls" if os.name == "nt" else "clear")

    # 2. KURAL: Her şeyi temizlenmiş ekrana fonksiyonun içinde yazdır
    print(Fore.CYAN + Style.BRIGHT + banner)
    print(
        Fore.YELLOW
        + Style.BRIGHT
        + "=================================================="
    )
    print(Fore.WHITE + " [1] Start Network Vulnerability Scanner")
    print(Fore.WHITE + " [2] Help")
    print(Fore.WHITE + " [3] Exit")
    print(
        Fore.YELLOW
        + Style.BRIGHT
        + "=================================================="
    )


def main():
    while True:
        boyka_menu()
        secim = input(Fore.GREEN + "\nChoose an option: " + Fore.WHITE)

        if secim == "1":
            print(Fore.YELLOW + "\n[*] Scanning mode selected...")
            hedef_ip = input(
                Fore.GREEN + "🎯 Enter the target IP address: " + Fore.WHITE
            )
            print(Fore.BLUE + f"\n[*] Target IP address entered: {hedef_ip}")

            # Genişletilmiş kritik port listesi
            test_portlari = [
                21,
                22,
                23,
                25,
                53,
                80,
                110,
                139,
                443,
                445,
                3306,
                3389,
                8080,
            ]
            print(Fore.YELLOW + "[*] Scanning ports and checking database safely...\n")

            acik_portlar_verisi = {}
            zafiyetli_portlar = {}

            # Portları tarıyoruz ve versiyonları topluyoruz
            for port in test_portlari:
                servis_bilgisi = scan(hedef_ip, port)

                if servis_bilgisi is not None:
                    acik_portlar_verisi[port] = servis_bilgisi
                    cve_list = check_vulnerability(servis_bilgisi)
                    if cve_list:
                        zafiyetli_portlar[port] = cve_list

            # AKILLI RAPORLAMA SİSTEMİ
            print(
                Fore.YELLOW
                + "\n=================== BOYKA SCAN REPORT ==================="
            )

            if not acik_portlar_verisi:
                print(Fore.WHITE + "[-] Target seems offline or no open ports found.")

            elif not zafiyetli_portlar:
                print(
                    Fore.GREEN
                    + "[+] Scan complete. No known vulnerabilities found via API."
                )
                print(Fore.YELLOW + "\n[ Open Ports & Versions ]")
                for port, version in acik_portlar_verisi.items():
                    print(Fore.GREEN + f"  • Port {port}: {version}")

            else:
                print(
                    Fore.RED + "[!] CRITICAL: Vulnerabilities detected on the target!"
                )
                print(Fore.YELLOW + "\n[ Open Ports & Versions ]")
                for port, version in acik_portlar_verisi.items():
                    print(Fore.GREEN + f"  • Port {port}: {version}")

                print(Fore.RED + "\n[ Vulnerability Details ]")
                for port, cves in zafiyetli_portlar.items():
                    print(
                        Fore.RED
                        + Style.BRIGHT
                        + f"\n Port {port} ({acik_portlar_verisi[port]}) is VULNERABLE!"
                    )
                    for cve in cves:
                        print(Fore.WHITE + f"   - {cve}")

            print(
                Fore.YELLOW
                + "========================================================="
            )
            input(Fore.WHITE + "\nPress Enter to return to main menu...")

        elif secim == "2":
            print(
                Fore.CYAN
                + "\n[ HELP ] Boyka Scanner checks open ports and pulls service versions."
            )
            print(
                Fore.CYAN
                + "Then it checks the CVE database using APIs for security issues."
            )
            input(Fore.WHITE + "\nPress Enter to return to main menu...")

        elif secim == "3":
            print(Fore.RED + "\n[*] Exiting Boyka Scanner... Stay safe!")
            break
        else:
            print(Fore.RED + "\n[*] Invalid option...")
            input(Fore.WHITE + "\nPress Enter to try again...")


if __name__ == "__main__":
    main()
