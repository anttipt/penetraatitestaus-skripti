# 🔍 Nmap Scan Python-skripti

Tämä sovellus ajaa [Nmap](https://nmap.org/) -skannauksen Pythonin kautta ja tallentaa tulokset tiedostoon.  
Sovellus on tarkoitettu penetraatiotestauksen ja kyberpuolustuksen harjoitteluun.

---

## 🚀 Ominaisuudet
- Ajaa Nmapin porttiskannauksen Pythonin `subprocess`-moduulin avulla
- Tukee SYN-skannausta (`-sS`), palveluversioiden tunnistusta (`-sV`) ja käyttöjärjestelmän tunnistusta (`-O`)
- Tallentaa tulokset tiedostoon (`nmap_results.txt`)
- Luo automaattisesti tuloskansion jos sitä ei ole
- Virheenkäsittely: ilmoittaa jos Nmap ei löydy tai skannaus epäonnistuu

---

## 📦 Asennus

1. Asenna [Python 3](https://www.python.org/downloads/)
2. Asenna [Nmap](https://nmap.org/download.html) Windowsille
   - Oletuspolku: `C:\Program Files (x86)\Nmap\`
   - Lisää polku PATH-muuttujaan tai käytä täyttä polkua skriptissä
3. Kloonaa projekti tai kopioi skripti

---

## 🧑‍💻 Käyttö

Aja skripti komentoriviltä:

```bash
python nmap_scan.py
```

Tulokset tallentuvat tiedostoon: 
```
C:\temp\nmap_results.txt
```

## 📄 Koodiesimerkki
```
import subprocess
import os

target_ip = "127.0.0.1"  # kohde-IP
results_dir = r"C:\temp"
os.makedirs(results_dir, exist_ok=True)

output_file = os.path.join(results_dir, "nmap_results.txt")
nmap_path = r"C:\Program Files (x86)\Nmap\nmap.exe"

command = [nmap_path, "-Pn", "-sS", "-sV", "-O", "-p-", "-oN", output_file, target_ip]

print("Ajetaan komento:", " ".join(command))
try:
    subprocess.run(command, check=True)
    print(f"Nmap-skannaus valmis! Tulokset tallennettu: {output_file}")
except FileNotFoundError:
    print("Virhe: Nmapia ei löytynyt annetusta polusta.")
except subprocess.CalledProcessError as e:
    print("Skannaus epäonnistui:", e)
```

## 📊 Esimerkkitulokset

Alla ote nmap_results.txt-tiedostosta, kun kohteena oli 127.0.0.1:
```
# Nmap 7.94 scan initiated Mon Nov 24 15:45:00 2025 as: nmap -Pn -sS -sV -O -p- -oN nmap_results.txt 127.0.0.1
Nmap scan report for localhost (127.0.0.1)
Host is up (0.00012s latency).
Not shown: 65532 closed ports
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 8.9 (protocol 2.0)
80/tcp   open  http    Apache httpd 2.4.54
443/tcp  open  https   OpenSSL 1.1.1
MAC Address: 00:0C:29:AB:CD:EF (VMware)
Device type: general purpose
Running: Linux 5.X
OS details: Linux 5.10 - 5.15
OS detection performed.
# Nmap done at Mon Nov 24 15:45:10 2025 -- 1 IP address (1 host up) scanned in 10.00 seconds
```

## ⚠️ Huomioitavaa

- SYN-skannaus (-sS) ja OS-tunnistus (-O) vaativat usein admin-oikeudet Windowsissa
- Jos kohde ei vastaa pingille, käytä -Pn-optiota
- OneDrive-synkronoidut kansiot voivat estää tulosten tallentumisen → käytä paikallista polkua (esim. C:\temp)


