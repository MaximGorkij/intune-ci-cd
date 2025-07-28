import json, os, requests
from auth import get_token

with open("config.json", "r") as f:
    config = json.load(f)

token = get_token(config)
headers = {"Authorization": f"Bearer {token}"}
backup_path = config["backupPath"]

def export_apps():
    url = "https://graph.microsoft.com/v1.0/deviceAppManagement/mobileApps"
    apps = requests.get(url, headers=headers).json()["value"]
    for app in apps:
        path = os.path.join(backup_path, f"{app['id']}.json")
        with open(path, "w") as f:
            json.dump(app, f, indent=4)

def export_policies():
    pass  # voliteľne doplniť export compliance/configuration policies

export_apps()
export_policies()