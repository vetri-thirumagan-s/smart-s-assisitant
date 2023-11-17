import streamlit as st
import main
import pyttsx3 as tts
import speech_recognition as sr


st.set_page_config("Voice Assistant","🎙️")



engine=tts.init()
engine.setProperty("rate",120)
voice=engine.getProperty('voices')
engine.setProperty("voice",voice[1].id)


r=sr.Recognizer()


    
with sr.Microphone() as scr:

    r.energy_threshold=10000
    r.adjust_for_ambient_noise(scr,1.2)

    print("listening to you...")

    audio_input=r.listen(scr)
    text_from_audio=r.recognize_google(audio_input)
    print(text_from_audio)
    my_name="hey smart"
    if my_name==text_from_audio.lower():
        main.starts()