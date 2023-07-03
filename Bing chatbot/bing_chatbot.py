import asyncio
import re
from EdgeGPT import Chatbot, ConversationStyle
import pyttsx3
import speech_recognition as sr  
import cv2
import face_recognition

import handdetect as h
import objectdetection as d
import facerecognize as l
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
    bot=Chatbot(cookiePath='C:/Users/arunp/Documents/project/Bing chatbot/cookies.json')
    
    
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

async def face_response():
    classNames,encodeListKnown=l.img_list()
    cap = cv2.VideoCapture(0)
    print("capturing")
    wish=0
    counter=1
    
    while True:
        success, img = cap.read()            
        imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        # Detect faces in the frame
        face_locations = face_recognition.face_locations(imgS)
        names,img=l.face_main(success, img ,classNames,encodeListKnown)
        # img=h.handsdetect(img)
        # labels=d.detect(img)
        # print(labels)
        cv2.imshow('Webcam',img)

        print(face_locations)
        print(names)

        if len(face_locations)>len(names):
            print("New faces detected, do you want to save it? say yes nor no")
            speak("New faces detected, do you want to save it? say yes nor no")
            
            listener=listen()
            if listener=="yes" or "s":
                print("say the name of new face")
                speak("say the name of new face")
                listener=listen()
                classNames,encodeListKnown=l.capture_new_face(img,success,counter,listener)
                counter+=1
            else:
                print(" ok")
                speak(" ok")
                
        
        # if len(face_locations)>0 and wish==0:
        #     for name in names:
        #         print(l.greet_person(name))
        #         speak(l.greet_person(name))
        #     wish+=1

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break

    
async def main():
    while True:
        listener=listen()
        print(listener)

        if listener=="exit":
            break
        if listener=="open":
            await face_response()
        else:
            await response(listener)



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