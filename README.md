# Installationsanleitung

## Installation von Python und pip

Beachten Sie die Installationseinleitung von Ihrem Betriebssystem.

### Windows

1. Herunterladen von Python von der [offiziellen Website](https://www.python.org/downloads/).
2. Führen sie die heruntergeladene Installationsdatei aus und stellen Sie sicher, dass das Kästchen "Add Python to PATH" angeclickt ist

Um zu testen, ob Python erfolgreich installiert führt man die folgenden Befehle in der Kommandozeile aus:
```sh
python --version
pip --version
```
Dies sollte die jeweiligen Versionen ausgeben.

### Linux

1. Öffnen eines Terminals.
2. Aktualisierung der Paketliste:
```sh
sudo apt update
```
3. Installation von Python und pip:
```sh
sudo apt install python3 python3-pip
```

Um zu testen, ob Python erfolgreich installiert führt man die folgenden Befehle in der Konsole aus:
```sh
python3 --version
pip3 --version
```
Dies sollte die jeweiligen Versionen ausgeben.

### Mac

1. Herunterladen von Python von der [offiziellen Website](https://www.python.org/downloads/).
2. Führen sie die heruntergeladene Installationsdatei aus und stellen Sie sicher, dass das Kästchen "Add Python to PATH" angeclickt ist (Möglicherweise bei Mac nicht nötig).
3. Alternativ kann Homebrew verwenden werden, um Python zu installieren:
```sh
brew install python
```

Um zu testen, ob Python erfolgreich installiert führt man die folgenden Befehle in der Konsole aus:
```sh
python3 --version
pip3 --version
```
Dies sollte die jeweiligen Versionen ausgeben.


## Installation von Abhängigkeiten

1. Navigigation zu dem Ordner mit dem Code:
```sh
cd /path/to/your/project
```
2. Installation der in `requirements.txt` angegebenen Abhängigkeiten:
```sh
pip install -r requirements.txt
```

## Ausführen des Codes

Um den Code zu starten, führen Sie die main.py Datei aus:
```sh
python3 app/main.py
```
oder bei Windows:
```sh
python app/main.py
```
Die Datei `main.py` befindet sich im Ordner `app` und muss von dort aus ausgeführt werden.
