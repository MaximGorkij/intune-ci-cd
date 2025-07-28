import os, json

def compare_apps(apps, config):
    statuses = {}
    for app in apps:
        app_id = app["id"]
        file_path = os.path.join(config["backupPath"], f"{app_id}.json")
        if not os.path.exists(file_path):
            statuses[app_id] = "new"
        else:
            with open(file_path) as f:
                backup = json.load(f)
            statuses[app_id] = "changed" if app != backup else "unchanged"
    return statuses