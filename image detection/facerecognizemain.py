import cv2
import numpy as np
import face_recognition
import os
import shutil
from datetime import datetime
import datetime


def get_time_of_day():
    current_hour = datetime.datetime.now().hour

    if current_hour < 12:
        time_of_day = "Morning"
    elif current_hour < 17:
        time_of_day = "Afternoon"
    else:
        time_of_day = "Evening"

    return time_of_day

def greet_person(name):
    time_of_day = get_time_of_day()
    greeting = f"Good {time_of_day}, {name}!"

    return greeting


def rename_file(file_path, new_name):
    # Get the directory and current name of the file
    directory = os.path.dirname(file_path)
    current_name = os.path.basename(file_path)
    # Construct the new file path with the new name
    new_file_path = os.path.join(directory, new_name)
    try:
        # Rename the file
        os.rename(file_path, new_file_path)
        print("File renamed successfully!")
    except OSError as e:
        print(f"Error occurred while renaming the file: {e}")

# # Example usage
# file_path = 'jeffandelon.jpg'
# new_name = 'jande.jpg'

# # Rename the file
# rename_file(file_path, new_name)


def move_file_to_folder(file_path, destination_folder):
    # Specify the destination path for the file
    destination_path = os.path.join(destination_folder, os.path.basename(file_path))

    # Move the file to the destination folder
    shutil.move(file_path, destination_path)

    print("file moved to destination")
# Example usage
# file_path = 'arun.jpg'
# destination_folder = 'images'

# Move the file to the destination folder
# move_file_to_folder(file_path, destination_folder)


def capture_and_save_image(image_name,img,success):
    if success:
        # Save the image with the custom name
        cv2.imwrite(image_name, img)
        print("new face saved successfully!")
    else:
        print("Failed to capture image from webcam")

# # Example usage
# image_name = '1.jpg'

# # Capture and save the image with the custom name
# capture_and_save_image(image_name)


def findEncodings(images):
    try:
        encodeList = []
        for img in images:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            encode = face_recognition.face_encodings(img)[0]
            encodeList.append(encode)
        return encodeList
    except Exception:
        pass


def img_list():
    path = 'images'
    images = []
    classNames = []
    myList = os.listdir(path)
    print(myList)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    print(classNames)

    encodeListKnown = findEncodings(images)
    print('Encoding Complete')

    return classNames,encodeListKnown


def f_recognize(img,imgS,encodeListKnown,classNames,recognized_faces=[]):
    recognized_faces=set(recognized_faces)

    # encodeListKnown = findEncodings(images)
    # print('Encoding Complete')
    

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)

    for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        #print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            #print(name)

            recognized_faces.add(name) #add the recognized faces to the set


            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            # markAttendance(name)
    
    return list(recognized_faces)


def capture_new_face(img,success,counter,name):
    #take image of new unknown faces
    capture_and_save_image(f'{counter}.jpg',img,success)

    # move the image to the correct place i.e images folder
    move_file_to_folder(f'{counter}.jpg', 'images')

    # r=input("do you want to rename the new face\n press y for Yes\n press n for NO")

    #rename the numbered image with the new name
    # if r.lower()=='y':
        # name=input("Enter new face's name")
    rename_file('images/'+f'{counter}.jpg',f'{name}.jpg')
    
    # encode the new face
    classNames,encodeListKnown=img_list()
        
    counter+=1

    return classNames,encodeListKnown




# def face_main():
def face_main(success, img, classNames, encodeListKnown):
    # classNames,encodeListKnown=img_list()

    # cap = cv2.VideoCapture(0)

    # while True:
        
    #     success, img = cap.read()


        # img = captureScreen()

    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)


    # Detect faces in the frame
    face_locations = face_recognition.face_locations(imgS)

    # if len(face_locations)==0:
    #     print("No faces detected")
    # else:
    #     print("Detecting faces",face_locations)

    result=[]
    if f_recognize(img,imgS,encodeListKnown,classNames)!=None:
        result=f_recognize(img,imgS,encodeListKnown,classNames)
        # print("result",result)


    


        
        
        
        # cv2.imshow('Webcam',img)
        # cv2.waitKey(1)

    return result,img

        # print(result)


























# def face_main():
#     classNames,encodeListKnown=img_list()

#     cap = cv2.VideoCapture(0)

#     counter=1
#     while True:
        
#         success, img = cap.read()
#         #img = captureScreen()
#         imgS = cv2.resize(img,(0,0),None,0.25,0.25)
#         imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)


#         # Detect faces in the frame
#         face_locations = face_recognition.face_locations(imgS)

#         # if len(face_locations)==0:
#         #     print("No faces detected")
#         # else:
#         #     print("Detecting faces",face_locations)

#         result=[]
#         if fr.f_recognize(img,imgS,encodeListKnown,classNames)!=None:
#             result=fr.f_recognize(img,imgS,encodeListKnown,classNames)
#             # print("result",result)


#         #save the image of unknown faces with number as  image name
#         if len(face_locations)>len(result):

#             #take image of new unknown faces
#             capture_and_save_image(f'{counter}.jpg',img,success)

#             # move the image to the correct place i.e images folder
#             move_file_to_folder(f'{counter}.jpg', 'images')

#             r=input("do you want to rename the new face\n press y for Yes\n press n for NO")

#             #rename the numbered image with the new name
#             if r.lower()=='y':
#                 name=input("Enter new face's name")
#                 rename_file('images/'+f'{counter}.jpg',f'{name}.jpg')
            
#             # encode the new face
#             classNames,encodeListKnown=img_list()
                
#             counter+=1

        
            
            
            
#         cv2.imshow('Webcam',img)
#         cv2.waitKey(1)

#         # print(result)
