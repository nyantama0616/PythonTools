from turtle import position
import cv2
from cvzone.PoseModule import PoseDetector

cap = cv2.VideoCapture("./assets/dance.mov")
detector = PoseDetector()
posList = []

while True:
    success, img = cap.read()
    if img is None:
        print("write")
        with open("./output/Animation.txt", "w") as f:
            f.writelines(["%s\n" % item for item in posList])
        break

    img = detector.findPose(img)
    lmList, bboxInfo = detector.findPosition(img)

    if bboxInfo:
        lmString = ""
        for lm in lmList:
            lmString += f"{lm[1]},{img.shape[0] - lm[2]},{lm[3]},"
        posList.append(lmString)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)
    # if key == ord("s"):
    #     print("write")
    #     with open("./output/Animation.txt", "w") as f:
    #         f.writelines(["%s\n" % item for item in posList])
