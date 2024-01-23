import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")

david = voices[0].id
zira = voices[1].id

engine.setProperty("voice", david)


def getVoice(msg):
    # engine.say(msg)
    engine.save_to_file(msg, "promo.wav")
    engine.runAndWait()