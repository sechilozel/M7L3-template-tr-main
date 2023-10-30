import speech_recognition as sr
import random
import time

seviyeler = {

    "easy": ["diary", "mouse", "computer", "past", "guest", "gift"],

    "normal": ["programming", "algorithm", "developer", "present", "exhausted"],

    "hard": ["neural network", "machine learning", "artificial intelligence", "pronounce", "mischievous"]

}

level = random.choice(seviyeler)
def play_game(level):
    word = random.choice(level)
    print("You are playing in", level, "mode. Your word is", word, "now spell it if you can :>")

    def speech():
        mic = sr.Microphone()
        recog = sr.Recognizer()

        with mic as audio_file:
            audio = recog.listen(audio_file)
            print(recog.recognize_google(audio, language= "en-GB")) #en-GB ---> English | tr-TR ---> Turkish
            return recog.recognize_google(audio, language="en-GB")

play_game(level)