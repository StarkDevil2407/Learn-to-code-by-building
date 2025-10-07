import subprocess

def show_wifi_passwords():
    try:
        data = subprocess.check_output("netsh wlan show profiles", shell=True).decode()
        profiles = [line.split(":")[1].strip() for line in data.split("\n") if "All User Profile" in line]
        for profile in profiles:
            result = subprocess.check_output(f'netsh wlan show profile "{profile}" key=clear', shell=True).decode()
            for line in result.split("\n"):
                if "Key Content" in line:
                    password = line.split(":")[1].strip()
                    print(f"{profile}: {password}")
    except Exception as e:
        print("❌ Error:", e)

if __name__ == "__main__":
    show_wifi_passwords()
