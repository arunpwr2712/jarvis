import threading
import cv2
import pyttsx3
import speech_recognition as sr  
import face_recognition

import img as d
import facerecognizemain as l
import hand as h


# Function for video capture
def video_capture():
    classNames,encodeListKnown=l.img_list()
    # Open video capture
    cap = cv2.VideoCapture(0)

    while True:
        # Read frame from video capture
        success,img = cap.read()

        imgS = cv2.resize(img,(0,0),None,0.25,0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(imgS)
        names,img=l.face_main(success, img ,classNames,encodeListKnown)
        objlist,img=d.detect(img)

        # Process the frame (e.g., display, save, etc.)
        cv2.imshow('Video', img)

        # Exit loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release video capture and close windows
    cap.release()
    cv2.destroyAllWindows()

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
        # print("Failed to recognize", e)
        return ""

# Function for voice input and speak
def voice_input_and_speak():
    # Initialize text-to-speech engine
    engine = pyttsx3.init()

    while True:
        # Get voice input
        voice_input =listen() # input("Enter your command: ")

        # Process voice input (e.g., perform actions based on the command)

        # Speak the response
        if len(voice_input)>0:
            engine.say("You said: " + voice_input)
            engine.runAndWait()

# Create threads for video capture and voice input/speak
video_thread = threading.Thread(target=video_capture)
voice_thread = threading.Thread(target=voice_input_and_speak)

# Start the threads
video_thread.start()
voice_thread.start()
