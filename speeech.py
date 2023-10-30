import speech_recognition as sr

def speeech():
    mic = sr.Microphone()
    recog = sr.Recognizer()

    with mic as audio_file:
        audio = recog.listen(audio_file)
        #print(recog.recognize_google(audio, language= "tr-TR")) #en-GB ---> English | tr-TR ---> Turkish
        return recog.recognize_google(audio, language="tr-TR")

print(speeech())