# AppChron

AppChron – Eine Python-Anwendung, die die aktive App auf deinem PC überwacht und die Nutzung in einer SQLite-Datenbank protokolliert. Ideal, um Nutzungszeiten auszuwerten und Anwendungsgewohnheiten zu analysieren. 

## Inhaltsverzeichnis

- [Installation](#installation)
- [Verwendung](#verwendung)
- [Ordnerstruktur](#ordnerstruktur)
- [Lizenz](#lizenz)
- [Mitwirken](#mitwirken)

## Installation

1. **Repository klonen:**

   ```bash
   git clone https://github.com/dein-benutzername/dein-projekt.git
   cd dein-projekt
   ```

2. **Virtuelle Umgebung erstellen (optional, aber empfohlen):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. **Abhängigkeiten installieren:**

   ```bash
   pip install -r requirements.txt
   ```

## Verwendung

Starte die Anwendung über das Hauptskript (z.B. `main.py` oder ein anderes Startskript):

```bash
python main.py
```

Die Anwendung nutzt Flask als Backend und FlaskWebGUI, um eine benutzerfreundliche grafische Oberfläche bereitzustellen.

Weitere Details und Konfigurationsoptionen findest du im `appchron`-Ordner.

## Ordnerstruktur

Ein Überblick über die wichtigsten Dateien und Ordner:

```
.
├── appchron           # Enthält alle wichtigen Projektdaten und Dokumente
├── requirements.txt   # Python-Abhängigkeiten
├── main.py            # Hauptanwendung (Beispielname)
└── README.md          # Dieses Dokument
```

## Lizenz

Dieses Projekt wird unter der **MIT Lizenz** veröffentlicht. Details findest du in der [LICENSE](LICENSE)-Datei.

## Mitwirken

Beiträge sind willkommen! Falls du Fehler findest oder neue Features vorschlagen möchtest, erstelle bitte ein Issue oder einen Pull Request.

---

*Hinweis: Passe die Dateinamen und Pfade ggf. an dein Projekt an.*
```

Du kannst diese README.md nach Belieben erweitern oder anpassen. Viel Erfolg mit deinem Projekt!
