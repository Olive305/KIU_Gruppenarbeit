# Installationsanleitung

## Installation von Python und pip

Springen Sie für die Installationsanleitung zu ihrem jeweiligen Betriebssystem.

### Windows

1. Laden Sie den Python Installer von der [offiziellen Website](https://www.python.org/downloads/) herunter.
2. Starten Sie das Installationsprogramm und überprüfen Sie, dass das Kästchen "Add Python to PATH" angeklickt wurde (Ansonsten wird man die Befehle nicht nutzen können).

Um zu testen, ob Python erfolgreich installiert wurde, öffnen Sie die Commandpromt und führen Sie die folgenden Befehle aus:
```sh
python --version
pip --version
```
Dies sollte die jeweiligen Versionen ausgeben.

### Linux

1. Öffnen Sie ein Terminal.
2. Aktualisieren Sie die Paketliste:
```sh
sudo apt update
```
3. Installieren Sie Python und pip:
```sh
sudo apt install python3 python3-pip
```

Um zu testen, ob Python erfolgreich installiert wurde, öffnen Sie das Terminal und führen Sie die folgenden Befehle aus:
```sh
python3 --version
pip3 --version
```
Dies sollte die jeweiligen Versionen ausgeben.

### Mac

1. Laden Sie den Python Installer von der [offiziellen Website](https://www.python.org/downloads/) herunter.
2. Starten Sie das Installationsprogramm und überprüfen Sie, dass das Kästchen "Add Python to PATH" angeklickt wurde (Möglicherweise bei Mac nicht notwendig).
3. Alternativ kann Homebrew verwenden werden, um Python zu installieren:
```sh
brew install python
```

Um zu testen, ob Python erfolgreich installiert wurde, öffnen Sie das Terminal und führen Sie die folgenden Befehle aus:
```sh
python3 --version
pip3 --version
```
Dies sollte die jeweiligen Versionen ausgeben.


## Installation von Abhängigkeiten

1. Navigieren Sie zu dem Ordner mit dem Code:
```sh
cd /path/to/your/project
```
2. Installieren Sie die in `requirements.txt` angegebenen Abhängigkeiten:
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
