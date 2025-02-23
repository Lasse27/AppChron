# AppChron

## Kurzbeschreibung
AppChron ist eine Python-Anwendung, die die aktuell aktive Anwendung auf deinem PC überwacht und die Wechselereignisse in einer SQLite-Datenbank protokolliert. Mit diesem Tool lassen sich Nutzungszeiten auswerten, beispielsweise um die Gesamtanwendungszeit eines Monats zu berechnen.

## Projektübersicht
Das Projekt besteht aus zwei Hauptkomponenten:

- **watcher.py**  
  Dieses Modul ist verantwortlich für:
  - Das Erfassen des aktuell aktiven Fensters (mithilfe von Windows-spezifischen APIs wie pywin32 oder pywinauto).
  - Das Überwachen von Fensterwechseln in regelmäßigen Intervallen oder per Event-Callback.
  - Das Auslösen von Ereignissen, sobald sich die aktive Anwendung ändert.

- **db_handler.py**  
  Dieses Modul kümmert sich um:
  - Die Initialisierung und Verwaltung der SQLite-Datenbank.
  - Das Erstellen der notwendigen Tabellen (z. B. eine Tabelle „app_logs“).
  - Das Einfügen der Log-Daten (App-Name, Fenstertitel und Zeitstempel).
  - Die Durchführung von Abfragen, um unter anderem die gesamte Anwendungszeit auszuwerten.

## Installation & Setup

1. **Repository klonen:**

   ```bash
   git clone https://github.com/lasse27/appchron.git
   cd active-app-logger
   ```

2. **Virtuelle Umgebung erstellen (optional):**

   ```bash
   python -m venv venv
   source venv/bin/activate    # Unter Windows: venv\Scripts\activate
   ```

3. **Abhängigkeiten installieren:**

   Erstelle eine requirements.txt (z.B. mit pywin32 oder pywinauto) und führe dann aus:

   ```bash
   pip install -r requirements.txt
   ```

4. **Skript starten:**

   ```bash
   python app.py
   ```

## Weiterentwicklung
- Erweiterung der Datenbankstruktur, um explizit Start- und Endzeiten zu speichern.
- Implementierung eines Dashboards zur Visualisierung der Nutzungszeiten.
- Verbesserte Fehlerbehandlung und Logging-Mechanismen.

## Lizenz
Dieses Projekt ist unter der MIT-Lizenz veröffentlicht. Details findest du in der Datei LICENSE.

## Kontakt
Bei Fragen oder Verbesserungsvorschlägen kannst du dich gerne unter lassehillen@gmx.de oder über GitHub an mich wenden.
