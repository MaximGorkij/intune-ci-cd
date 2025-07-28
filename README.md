# Intune Deployer Web

Webová aplikácia na správu aplikácií v Microsoft Intune. Umožňuje export, import a porovnanie konfigurácií aplikácií cez Graph API.

## Funkcie

- GUI výber aplikácií na import
- Vizualizácia zmien
- Docker podpora

## Spustenie

```bash
docker build -t intune-deployer .
docker run -p 5000:5000 intune-deployer