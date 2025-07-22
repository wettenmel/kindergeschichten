
# Kindergeschichten-Backend

## Webhook Endpoint:
POST /webhook

## Beschreibung:
Dieses Backend empfängt den Typeform-Webhook, generiert die Geschichte und Bildbeschreibungen mit GPT, ersetzt die Platzhalter, formatiert das Ergebnis in 17 <<<BLOCKEND>>>-Blöcke und gibt den Text zurück – bereit für Zapier.

## Datei-Struktur:
- `main.py`: FastAPI App
- `utils.py`: Logik zur Generierung und Ersetzung
- `prompts.py`: Templates für Geschichte und Bildbeschreibungen
- `README.md`: Diese Anleitung

## Konfiguration:
- GPT-Schlüssel und echte API-Aufrufe bitte ergänzen
- Prompt-Template in `prompts.py` anpassen

## Ergebnis:
1 Textblock → 17 sauber getrennte Blöcke via `<<<BLOCKEND>>>`
