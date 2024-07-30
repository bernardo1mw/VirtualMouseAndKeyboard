import cv2
from time import sleep
import cvzone
from pynput.keyboard import Controller
import math

class Button:
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.text = text
        self.size = size


class VirtualKeyboard:
    def __init__(self, detector):
        self.textArea = 0
        self.keys = [
        ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "spc"],
        ]
        self.finalText = ""
        self.detector = detector
        self.keyboard = Controller()
        self.buttonList = []
        for i in range(len(self.keys)):
            for j, key in enumerate(self.keys[i]):
                self.buttonList.append(Button([100 * j + 100, 100 * i + 200], key))

    
    def drawAll(self, img):
        for button in self.buttonList:
            x, y = button.pos
            w, h = button.size
            cvzone.cornerRect(
                img,
                (button.pos[0], button.pos[1], button.size[0], button.size[1]),
                20,
                rt=0,
            )
            cv2.rectangle(img, button.pos, (x + w, y + h), (255, 0, 255), cv2.FILLED)
            cv2.putText(
                img,
                button.text,
                (x + 20, y + 65),
                cv2.FONT_HERSHEY_PLAIN,
                4,
                (255, 255, 255),
                4,
            )
            
        # return img

    def trackClick(self, img, lmList, lmList2):
        
        if lmList: ## Try to find the position using module
            for button in self.buttonList:
                x, y = button.pos
                w, h = button.size

                if x < lmList[8][1] < x + w and y < lmList[8][2] < y + h:
                    cv2.rectangle(
                        img,
                        (x - 5, y - 5),
                        (x + w + 5, y + h + 5),
                        (175, 0, 175),
                        cv2.FILLED,
                    )
                    cv2.putText(
                        img,
                        button.text,
                        (x + 20, y + 65),
                        # (x + 5, y+ 45),
                        cv2.FONT_HERSHEY_PLAIN,
                        4,
                        (255, 255, 255),
                        4,
                    )
                    l, _, _ = self.detector.findDistance(8, 4, img, draw=False)
                    # print(l)

                    ## when clicked
                    if l < 30:
                        # self.keyboard.press(button.text)
                        cv2.rectangle(
                            img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED
                        )
                        cv2.putText(
                            img,
                            button.text,
                            (x + 20, y + 65),
                            cv2.FONT_HERSHEY_PLAIN,
                            4,
                            (255, 255, 255),
                            4,
                        )
                        if button.text == 'spc':
                            self.finalText += " "
                        else:
                            self.finalText += button.text
                        sleep(0.5)


        if lmList2:
            for button in self.buttonList:
                x, y = button.pos
                w, h = button.size

                if x < lmList2[8][1] < x + w and y < lmList2[8][2] < y + h:
                    cv2.rectangle(
                        img,
                        (x - 5, y - 5),
                        (x + w + 5, y + h + 5),
                        (175, 0, 175),
                        cv2.FILLED,
                    )
                    cv2.putText(
                        img,
                        button.text,
                        (x + 20, y + 65),
                        cv2.FONT_HERSHEY_PLAIN,
                        4,
                        (255, 255, 255),
                        4,
                    )
                    l1, _, _ = self.detector.findDistance(8, 4, img, draw=False)
                    # print(l1)

                    ## when clicked
                    if l1 < 30:
                        # self.keyboard.press(button.text)
                        cv2.rectangle(
                            img, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED
                        )
                        cv2.putText(
                            img,
                            button.text,
                            (x + 20, y + 65),
                            cv2.FONT_HERSHEY_PLAIN,
                            4,
                            (255, 255, 255),
                            4,
                        )
                        self.finalText += button.text
                        sleep(0.5)


        for i in range(0, len(self.finalText), 12):
            j = int(i/12)
            cv2.rectangle(img, (100, 500 + (100*j)), (800, 600 + (100*j)), (175, 0, 175), cv2.FILLED)
            # cv2.rectangle(img, (50, 350 + (100*1)), (700, 450 + (100*1)), (175, 0, 175), cv2.FILLED)
            cv2.putText(
                img, self.finalText[i: i+12], (110, 580 + 100*j), cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5
            )
        


