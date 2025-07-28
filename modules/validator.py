import jsonschema

def validate_config(config):
    schema = {
        "type": "object",
        "properties": {
            "backupPath": {"type": "string"},
            "selectedApps": {"type": "array"},
            "auth": {
                "type": "object",
                "properties": {
                    "tenantId": {"type": "string"},
                    "clientId": {"type": "string"},
                    "clientSecret": {"type": "string"},
                    "scope": {"type": "string"}
                },
                "required": ["tenantId", "clientId", "clientSecret", "scope"]
            }
        },
        "required": ["backupPath", "selectedApps", "auth"]
    }
    jsonschema.validate(instance=config, schema=schema)