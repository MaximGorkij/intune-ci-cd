import os, json, requests

def get_apps(config, token):
    url = "https://graph.microsoft.com/v1.0/deviceAppManagement/mobileApps"
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers).json()
    return response.get("value", [])

def run(config):
    token = get_token(config)
    apps = get_apps(config, token)
    os.makedirs(config["backupPath"], exist_ok=True)
    for app in apps:
        with open(os.path.join(config["backupPath"], f"{app['id']}.json"), "w") as f:
            json.dump(app, f, indent=4)