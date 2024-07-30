import cv2
import numpy as np
import autopy


class VirtualMouse:
    def __init__(self, detector):
        self.detector = detector
        self.wScr, self.hScr = autopy.screen.size()
        self.wCam, self.hCam = 1280, 720
        self.frameR = 200
        self.smoothening = 5
        self.plocX, self.plocY = 0, 0
        self.clocX, self.clocY = 0, 0

    def activate():
        pass

    def trackFingertip(self, img, lmList):
        # lmList, bbox = self.detector.findPosition(img)
        # if len(lmList) != 0:
        cv2.rectangle(
            img,
            (self.frameR, self.frameR),
            (self.wCam - self.frameR, self.hCam - self.frameR),
            (255, 0, 255),
            2,
        )
        x1, y1 = lmList[8][1:]
        fingers = self.detector.fingersUp()
        if fingers[1] == 1 and fingers[2] == 0:
            x3 = np.interp(
                x1, (self.frameR, self.wCam - self.frameR), (0, self.wScr)
            )  # (100, 540) -> (0, 1280)
            y3 = np.interp(
                y1, (self.frameR, self.hCam - self.frameR), (0, self.hScr)
            )  # (100, 380) - > (0, 920)

            self.clocX = self.plocX + (x3 - self.plocX) / self.smoothening
            self.clocY = self.plocY + (y3 - self.plocY) / self.smoothening

            # moveX = self.wScr - self.clocX  -- use for non flipped image
            moveX = self.clocX
            moveY = self.clocY

            moveX = (self.wScr - 1) if moveX > self.wScr else moveX
            moveX = 0 if moveX < 0 else moveX
            moveY = (self.hScr - 1) if moveY > self.hScr else moveY
            moveY = 0 if moveY < 0 else moveY

            # print(moveX,moveY)

            autopy.mouse.move(moveX, moveY)
            
            cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
            self.plocX, self.plocY = self.clocX, self.clocY
        self.trackClick(img, fingers)

    def trackClick(self, img, fingers):

        if fingers[1] == 1 and fingers[2] == 1:
            length, img, lineInfo = self.detector.findDistance(8, 12, img)
            if length < 40:
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 15, (0, 255, 0), cv2.FILLED)
                autopy.mouse.click()
