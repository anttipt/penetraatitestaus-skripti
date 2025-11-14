import subprocess

output_path = "C:/Users/antti/OneDrive/Työpöytä/anttipt/kyberpuolustus_eettinen_hakkerointi/penetration-testing-script/results/nmap_results.txt"
command = ["nmap", "-sS", "-sV", "-O", "-p-", "-oN", output_path, "192.168.1.180"]

subprocess.run(command)
