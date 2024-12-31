# Installationsanleitung

## Installation von Python und pip

### Windows

1. Laden Sie das Python-Installationsprogramm von der [offiziellen Website](https://www.python.org/downloads/) herunter.
2. Führen Sie das Installationsprogramm aus und stellen Sie sicher, dass das Kästchen "Add Python to PATH" aktiviert ist.
3. Folgen Sie den Installationsschritten.

Um die Installation zu überprüfen, öffnen Sie die Eingabeaufforderung und führen Sie aus:
```sh
python --version
pip --version
```

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

Um die Installation zu überprüfen, führen Sie aus:
```sh
python3 --version
pip3 --version
```

### Mac

1. Laden Sie das Python-Installationsprogramm von der [offiziellen Website](https://www.python.org/downloads/) herunter.
2. Führen Sie das Installationsprogramm aus und folgen Sie den Installationsschritten.
3. Alternativ können Sie Homebrew verwenden, um Python zu installieren:
```sh
brew install python
```

Um die Installation zu überprüfen, öffnen Sie das Terminal und führen Sie aus:
```sh
python3 --version
pip3 --version
```

## Installation von Abhängigkeiten

1. Navigieren Sie zu Ihrem Projektverzeichnis:
```sh
cd /path/to/your/project
```
2. Installieren Sie die in `requirements.txt` aufgeführten Abhängigkeiten:
```sh
pip install -r requirements.txt
```

## Ausführen des Codes

Um den Code auszuführen, führen Sie das Hauptskript aus:
```sh
python app/main.py
```
oder:
```sh
python3 app/main.py
```
Die Datei `main.py` befindet sich im Ordner `app` und muss von dort aus ausgeführt werden.
