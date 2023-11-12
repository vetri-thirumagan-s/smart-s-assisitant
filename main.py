import pyttsx3 as tts
import speech_recognition as sr
import gpt
import pywhatkit as pt


def starts():



    engine=tts.init()

    rate=engine.getProperty('rate')
    engine.setProperty('rate',120) 

    voice=engine.getProperty('voices')
    engine.setProperty('voice',voice[1].id)


    def speak(output_text):
        engine.say(output_text)
        engine.runAndWait()

    r=sr.Recognizer()

    while True:

        with sr.Microphone() as scr:

            r.energy_threshold=10000
            r.adjust_for_ambient_noise(scr,1.2)

            print("listening to you...")

            try:    
                audio_input=r.listen(scr)
            
                text_from_audio=r.recognize_google(audio_input)
                print(text_from_audio)
                
                
                if "play" and "video" and "song" in text_from_audio:
                    pt.playonyt(text_from_audio)

                else: 
                    output_text=gpt.palm_output(text_from_audio)
                    print(output_text)
                    speak(output_text)

            except Exception or RuntimeError:
                speak("BYE")
                print("BYE")
                break

