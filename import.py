import json, os, requests
from auth import get_token

with open("config.json", "r") as f:
    config = json.load(f)

token = get_token(config)
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}
backup_path = config["backupPath"]

def import_apps():
    for app_id in config["selectedApps"]:
        path = os.path.join(backup_path, f"{app_id}.json")
        with open(path, "r") as f:
            app = json.load(f)
        print(f"Importujem: {app['displayName']}")
        # Voliteľne POST/PUT na Graph API

import_apps()