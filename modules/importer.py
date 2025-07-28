import os, json

def run(config):
    for app_id in config["selectedApps"]:
        file_path = os.path.join(config["backupPath"], f"{app_id}.json")
        if os.path.exists(file_path):
            with open(file_path) as f:
                app = json.load(f)
            print(f"Importujem: {app['displayName']}")
            # POST / PUT cez Graph API – voliteľne