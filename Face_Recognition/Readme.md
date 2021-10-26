<h1 align="center"><a name="section_name">Real-time Face Detection using Raspberry Pi</a></h1>

## Introduction

<div align="justify">
Face detection systems has become very popular these days, as it can be very secure compared to fingerprint and typed passwords. This repository presents a Face Recognition system using the OpenCV Library on Raspberry Pi, as it is portable to work as a surveillance system.

It includes two python scripts, of which one is a training program that will analyze the set of photos of a particular person available in the 'Face_Images' directory and create a dataset(YML File) from it. The second program here is the Recognizer program, which detects a face and then uses this YML file to recognize the face to mention the person's name. The programs here, are optimized for Raspberry Pi.
</div>

## About the Module
<div align="justify">
There are plenty of algorithms behind detecting a face from these pixels and further recognize the person in it and trying to explain them is beyond the scope of this tutorial, but since we are using the OpenCV library, which is incredibly simple to perform, face Recognition can be understood without getting deeper into the concepts.

OpenCV is an open-source library for computer vision, machine learning, and image processing. By using this library, one can process images and videos to identify objects. It identifies image patterns and their features, which will be used in vector space to perform mathematical operations.

Dlib is a toolkit for real-world Machine Learning and data analysis applications.

Pillow also called PIL, stands for Python Imaging Library which is known to open, manipulate and save images in an exceedingly different format.

The face_recognition library for python is taken into account to be the only library to acknowledge and manipulate faces. we'll be using this library to coach and recognize faces.
</div>

## Training & Testing
<div align="justify">
Let’s take a glance at the Face_Trainer.py program. The target of the program is to open all the pictures within the Face_Images directory and seek faces.
Once the face is detected, it crops the face and converts it to grayscale, then to a NumPy array. Then, the face_recognition library is used to coach and put it aside as a file called face-trainner.yml. the information during this file can later be accustomed to recognize the faces.

The haarcascade_frontalface_default.xml classifier to detect faces in images. Then, a recognizer variable is used to form a Local Binary Pattern Histogram (LBPH) Face Recognizer.

Once the face has been detected, it is cropped and considered as Region of Interest (ROI). The ROI region is used to train the face recognizer. These ROI values together with the Face ID value to the recognizer is the training data. The information obtained is saved in the face-trainner.yml file.

Within the Face Recognizer program, we'll get a live video feed from a USB webcam then convert it to a picture.

Then the face detection technique detects faces in those photos compares them with all the Face ID that was created earlier. If a match is found, a bounding box for the face is drawn and the name of the person recognized is written over it.
<div>
### Results 

Sample result obtained on Raspberry Pi 4 Model B:

![Output](https://raw.githubusercontent.com/Surveillance-NWB/Smart-Home-Surveillance/main/Face_Recognition/sample_Output.png)

### Reference
https://robu.in/real-time-face-detection-using-raspberry-pi-connections-and-code/
