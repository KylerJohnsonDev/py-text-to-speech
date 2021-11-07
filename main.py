import pyttsx3

def main():
    with open('./file_to_read.txt', 'r') as f:
        file_contents = f.read()
        engine = pyttsx3.init()
        engine.setProperty('rate', 200)
        engine.setProperty('voice', 'english-us')
        engine.say(file_contents)
        engine.runAndWait()
        f.close()

if __name__ == '__main__':
    main()