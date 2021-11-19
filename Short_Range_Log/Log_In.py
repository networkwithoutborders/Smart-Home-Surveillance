import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
import pickle

def markAttendance(name):
    with open('Log.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            if entry[0]=='':
                continue
            else:
                nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')

def take_photo():
    file_name=input("Enter your name : ")
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        cv2.imshow('webcam feed' , frame)
        key = cv2.waitKey(1) & 0xFF
        if key == ord("c"):
            cv2.imwrite("Training Images/"+str(file_name)+".png",frame)
            cv2.destroyAllWindows()
            break


    cap.release()

def findEncodings(images):
    encodeList = []


    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        print(img)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def training():
    take_photo()
    path = 'Training Images'
    images = []
    classNames = []
    myList = os.listdir(path)
    print(myList)
    for cl in myList:
        curImg = cv2.imread(f'{path}/{cl}')
        images.append(curImg)
        classNames.append(os.path.splitext(cl)[0])
    encodeListKnown = findEncodings(images)
    with open('encodeListKnown.ob', 'wb') as fp:
        pickle.dump(encodeListKnown, fp)
    with open('classNames.ob', 'wb') as fp:
        pickle.dump(classNames, fp)
    print('Encoding Complete')

op=input("New entry(Yes/No)  : ")
if op=='Yes' or op=='yes':
    training()
    with open('encodeListKnown.ob', 'rb') as fp:
        encodeListKnown = pickle.load(fp)
    with open('classNames.ob', 'rb') as fp:
        classNames = pickle.load(fp)
else:
    with open('encodeListKnown.ob', 'rb') as fp:
        encodeListKnown = pickle.load(fp)
    with open('classNames.ob', 'rb') as fp:
        classNames = pickle.load(fp)

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
# img = captureScreen()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
# print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
# print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name)
    cv2.imshow('Preview',img) #Display the Video
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()