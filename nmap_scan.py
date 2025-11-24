import subprocess
import os

# Kohde-IP
target_ip = "192.168.1.130"

# Tulosten tallennuskansio
results_dir = output_file = r"C:\temp\nmap_results.txt"
os.makedirs(results_dir, exist_ok=True)

# Tulostiedoston polku
output_file = os.path.join(results_dir, "nmap_results.txt")

# Nmap-komento (käytä 'nmap' jos PATHissa, muuten täysi polku esim. r"C:\Program Files (x86)\Nmap\nmap.exe")
command = ["nmap", "-sS", "-sV", "-O", "-p-", "-oN", output_file, target_ip]

try:
    subprocess.run(command, check=True)
    print(f"Nmap-skannaus valmis! Tulokset tallennettu: {output_file}")
except FileNotFoundError:
    print("Virhe: Nmapia ei löytynyt. Varmista että se on asennettu ja PATHissa.")
except subprocess.CalledProcessError as e:
    print("Skannaus epäonnistui:", e)