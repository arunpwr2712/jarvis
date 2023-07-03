
import cv2
from cvzone.HandTrackingModule import HandDetector

# cap =cv2.VideoCapture(0)
detector=HandDetector(maxHands=1)

def handsdetect(img):
    offset=75
# while True:
    # success,img=cap.read()
    hands,img=detector.findHands(img)
    try:
        if hands:
            hand=hands[0]
            x,y,w,h=hand['bbox']
            imgcrop=img[y-offset:y+h+offset,x-offset:x+w+offset]
            # if imgcrop.shape[0]>400 and imgcrop.shape[1]>400:
            cv2.imshow("imagecrop",imgcrop)
            # print(imgcrop.shape)
            # if imgcrop.shape[0]>400 and imgcrop.shape[1]>400:
                
            #     cv2.imshow("imagecrop",imgcrop)
            #     print(imgcrop.shape)

            return imgcrop
    except Exception:
        pass

    return img

    


    # cv2.imshow("image",img)
    # cv2.waitKey(1)






























# import cv2
# from cvzone.HandTrackingModule import HandDetector

# cap =cv2.VideoCapture(0)
# detector=HandDetector(maxHands=1)

# offset=100
# while True:
#     success,img=cap.read()
#     hands,img=detector.findHands(img)
#     try:
#         if hands:
#             hand=hands[0]
#             x,y,w,h=hand['bbox']
#             imgcrop=img[y-offset:y+h+offset,x-offset:x+w+offset]
#             # if imgcrop.shape[0]>400 and imgcrop.shape[1]>400:
                
#             cv2.imshow("imagecrop",imgcrop)
#             print(imgcrop.shape)
#             # if imgcrop.shape[0]>400 and imgcrop.shape[1]>400:
                
#             #     cv2.imshow("imagecrop",imgcrop)
#             #     print(imgcrop.shape)
#     except Exception:
#         pass


#     cv2.imshow("image",img)
#     cv2.waitKey(1)