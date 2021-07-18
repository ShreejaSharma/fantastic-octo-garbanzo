import speech_recognition as sr
import webbrowser

r1=sr.Recognizer()
r2=sr.Recognizer()
r3=sr.Recognizer()

with sr.Microphone() as source:
    print("Speak Anything :")
    audio = r3.listen(source)
    try:
        text = r2.recognize_google(audio)
        print("You said : {}".format(text))
    except:
        print("Sorry could not recognize your voice")
    
