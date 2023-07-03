import asyncio
import re
from EdgeGPT import Chatbot, ConversationStyle
import pyttsx3
import speech_recognition as sr  
import threading
import cv2

import facerecognizemain as l

# import object_detection as od
# import face_recognition_main as frm

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def listen():
    print("listening...")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        query = query.lower()
        return query
    except Exception as e:
        print(e)
        return listen()

    
async def bing(listener):
# def bing(listener):
    bot=Chatbot(cookiePath='C:/Users/arunp/Documents/project/Bing chatbot/cookies.json')
    
    
    # response = bot.ask(prompt=listener,conversation_style=ConversationStyle.creative)
    response = await bot.ask(prompt=listener,conversation_style=ConversationStyle.creative)
    

    # response = await bot.ask(prompt=input("Type here : "),conversation_style=ConversationStyle.creative)
    # Select only the bot response from response dictionary
    for message in response["item"]["messages"]:
        if message["author"]=="bot":
            bot_response = message["text"]
    #remove [^#^] citations from response
    bot_response = re.sub('\[\^\d+\^\]', '', bot_response)
    print("Bot's response : ",bot_response)
    # speak(bot_response)
    await bot.close()
    # bot.close()
    return bot_response

async def response(listener):
    
    if "detect objects around me" in listener:
        print("detecting objects around you")
        speak("detecting objects around you")
        # objects=list(od.main_object_detection())
        # speak("objects around are ")
        # print(objects)
        # for i in objects:
        #     speak(i)
        
    
    else:    
        result = await bing(listener)
        # result = bing(listener)
        speak(result)
    # speak(listener)
    
    # if listener=="exit":
    #     break



    
async def main():
# def main():
    classNames,encodeListKnown=l.img_list()
    cap = cv2.VideoCapture(0)

    while True:
        
        success, img = cap.read()

        img=l.face_main(success, img ,classNames,encodeListKnown)

        cv2.imshow('Webcam',img)
        

    # while True:
        listener=listen()
        print(listener)
        
        if listener=="exit":
            break

        await response(listener)

        cv2.waitKey(1)

        

    cap.release()
    cv2.destroyAllWindows()
        

        # if "detect objects around me" in listener:
        #     print("detecting objects around you")
        #     speak("detecting objects around you")
        #     # objects=list(od.main_object_detection())
        #     # speak("objects around are ")
        #     # print(objects)
        #     # for i in objects:
        #     #     speak(i)
            
        
        # else:    
        #     result = await bing(listener)
        #     # result = bing(listener)
        #     speak(result)
        # # speak(listener)
        
        # if listener=="exit":
        #     break


if __name__ == '__main__':
    asyncio.run(main())


















# Google Bard ai chatbot 

# from Bard import Chatbot

# token = "WwgsvduAtIsXcTpERM367hvLUGCMlmGsiqUbF2BohWewaV-xwDezkzXmEU0prYeRLTikzA."
# # Initialize Google Bard API
# chatbot = Chatbot(token)

# def prompt_bard(prompt):
#     response = chatbot.ask(prompt)
#     return response['content']

# while True:
#     prompt=input("Please enter your question : ")
#     print("Bard response : " + prompt_bard(prompt))
#     if prompt == "q":
#         break