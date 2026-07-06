import requests
from datetime import datetime
from pathlib import Path

FGT_IP = "192.168.184.139"
API_TOKEN = "70H0d5Gzxfqn1bHsksjfHfGkd7mf3f"

url = f"https://{FGT_IP}/api/v2/monitor/system/config/backup"

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

params = {
    "scope": "global"
}

# Backup directory
backup_dir = Path("/home/Firewall/backups")
backup_dir.mkdir(parents=True, exist_ok=True)

response = requests.get(
    url,
    headers=headers,
    params=params,
    verify=False
)

if response.status_code == 200:
    filename = backup_dir / f"FortiGate_{datetime.now().strftime('%Y%m%d_%H%M%S')}.conf"

    with open(filename, "wb") as file:
        file.write(response.content)

    print(f"Backup saved as {filename}")
else:
    print(f"HTTP {response.status_code}")
    print(response.text)
