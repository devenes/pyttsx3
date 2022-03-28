import pyttsx3


engine = pyttsx3.init()

engine.setProperty("rate", 150)

text = input("Enter the text you want to convert to audio: ")

engine.say(text)

engine.runAndWait()
