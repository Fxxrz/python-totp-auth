# Python TOTP 2FA Tool

Dies ist ein einfaches Python-Tool zur Generierung und Überprüfung von TOTP-basierten Zwei-Faktor-Authentifizierungscodes (2FA) mit der Bibliothek `pyotp`.

Mit diesem Tool können Sie:
- Einen neuen Shared Secret (16 Zeichen) generieren
- Den aktuellen 6-stelligen TOTP-Code anzeigen
- Einen eingegebenen 2FA-Code gegen einen vorhandenen Secret überprüfen

## Funktionen

Zufällige Generierung eines Shared Secret  
TOTP-Code-Erzeugung (6-stelliger PIN)  
Überprüfung eines Benutzereingabecodes auf Gültigkeit  

## Voraussetzungen

- Python 3.6 oder höher  
- Das Python-Paket `pyotp`

Installieren Sie die Abhängigkeiten mit:

```bash
pip install -r requirements.txt
```

## Verwendung

Führen Sie das Skript aus:

```bash
python your_script_name.py
```

Sie werden dann aufgefordert:

1. **Einen neuen Shared Secret zu generieren** (der aktuelle TOTP-Code wird sofort angezeigt)  
2. **Einen bestehenden Secret zu testen**, indem Sie ihn manuell eingeben und einen TOTP-Code zur Prüfung angeben

## Beispiel

```
Möchten Sie einen neuen Shared Secret generieren oder einen bestehenden testen? (1 = generieren, 2 = testen): 1
Zufällig generierter Shared Secret (16 Zeichen): Xk8T2...
Ihr aktueller TOTP-Code lautet: 123456
```

## Hinweise

- TOTP-Codes ändern sich alle 30 Sekunden.
- Für den produktiven Einsatz empfiehlt es sich, Secrets sicher zu speichern und optional einen QR-Code für die Nutzung mit Authenticator-Apps (z. B. Google Authenticator, Authy) anzuzeigen.

## Lizenz

MIT – Nutzung und Anpassung sind frei erlaubt.