## PY-SPEECH

A python program uses the [pyttsx3](https://pyttsx3.readthedocs.io/en/latest/engine.html#examples) package for speech-to-text. 

### Dependencies
- pyttsx3
- Speech-to-text synthesizer (you may have to install one)
    - pyttsx3 includes drivers for:
        - SAPI5 (Windows)
        - NSSpeechSynthesizer (MacOS)
        - espeak (Linux)

### Steps to run the project

1. Clone the repository

2. From inside of the project directory, create a virtual environment:
```shell
python -m venv ./venv
```

3. Activate the virtual environment:
```shell
source venv/bin/activate
```

4. Install pyttsx3:
```shell
python -m pip install pyttsx3
```

5. Run the program:
```shell
python main.py
```