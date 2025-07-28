from flask import Flask, render_template, request
import json
from modules import auth, exporter, importer, diff, validator

app = Flask(__name__)

def get_config():
    with open("config.json") as f:
        return json.load(f)

@app.route("/", methods=["GET"])
def index():
    config = get_config()
    validator.validate_config(config)
    token = auth.get_token(config)
    apps = exporter.get_apps(config, token)
    statuses = diff.compare_apps(apps, config)
    return render_template("index.html", apps=apps, statuses=statuses)

@app.route("/import", methods=["POST"])
def import_selected():
    selected = request.form.getlist("selected")
    config = get_config()
    config["selectedApps"] = selected
    importer.run(config)
    return render_template("result.html", result=f"Import hotový pre {len(selected)} aplikácií.")