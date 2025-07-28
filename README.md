# Intune CI/CD Template

Automatizované spracovanie aplikácií a politík v Microsoft Intune pomocou Python skriptov a CI/CD pipeline.

## Obsah
- Export a import objektov pomocou Microsoft Graph API
- Git-verziovanie záloh (`.json`)
- Dynamická konfigurácia cez `config.json`
- Azure DevOps pipeline (`azure-pipelines.yml`)

## Nastavenie
1. Vytvor Azure App Registration s potrebnými oprávneniami
2. Uprav `config.json` podľa tvojho tenanta
3. Spusti pipeline cez DevOps alebo manuálne