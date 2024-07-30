import cv2
import time
import autopy
import HandDetector as hd

from VirtualMouseClass import VirtualMouse
from VirtualKeyboardClass import VirtualKeyboard


wCam, hCam = 1280, 720
# wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'))
cap.set(cv2.CAP_PROP_FPS, 60)

detector = hd.HandDetector(maxHands=2)
myMouse = VirtualMouse(detector)
myKbd = VirtualKeyboard(detector)
pTime = 0

def isKbdOrMouse(kbd, mouse):
    fingers = detector.fingersUp()
    # print("fingers: ", fingers)
    if fingers[4] == 1 and fingers.count(0) >= 3: # kbd
        autopy.mouse.move(38, 610)
        autopy.mouse.click()
        return True, False
    if fingers.count(1) == 5: # mouse 
        return False, True
    return kbd, mouse


iskeyboardActive, isMouseActive = False, False

try:
    while True:
        success, img = cap.read()
        img = cv2.flip(img, 1)
        img = detector.findHands(img)

        lmList, bboxInfo =  detector.findPosition(img)
        lmList2, bboxInfo2 =detector.findPosition(img, 1)
        
        if len(lmList) != 0:
            iskeyboardActive, isMouseActive = isKbdOrMouse(iskeyboardActive, isMouseActive)
            if iskeyboardActive:
                
                # cv2.putText(
                # img,
                # 'Q',
                # (50 + 20, 50 + 65),
                # cv2.FONT_HERSHEY_PLAIN,
                # 4,
                # (255, 255, 255),
                # 4,
                # )
                myKbd.drawAll(img)
                myKbd.trackClick(img, lmList, lmList2)
                # print('KBD')
            elif isMouseActive:
                # img = cv2.flip(img, 1)
                myMouse.trackFingertip(img, lmList)
                # print('mouse')
        
        
        
        
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(
            img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 255), 3
        )

        cv2.imshow("Image", img)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
finally:
        cap.release()
        cv2.destroyAllWindows()