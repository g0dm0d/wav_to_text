import speech_recognition as sr
r = sr.Recognizer()
with sr.AudioFile('file.wav') as source:
    audio_data = r.record(source)
text = r.recognize_google(audio_data)
print(text)