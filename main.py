#Importing Libraries
import speech_recognition as sr
import os

#Main Function
def voice_recorder():
#enable user microphone
    recorder = sr.Recognizer()

#using microphone recordings
    with sr.Microphone() as source:
        recorder.adjust_for_ambient_noise(source)
        audio = recorder.listen(source)
        
    try:
        speech = recorder.recognize_google(audio, language='pt-BR')

        if ('Abra' in speech and ('ópera' in speech) or 'Google' in speech):
            os.system("start opera.exe")
        
        if 'Abra' in speech and 'calculadora' in speech:
            os.system('start calc.exe')

#returns the pronounced sentence
        print('Você disse: '+ speech)
    
    except sr.UnknownValueError:
#Indicates that the speech recognizer did not understand what was said
        print("Desculpe eu não entendi oque você disse!")
    
    return speech

voice_recorder()
