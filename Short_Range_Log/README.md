<h1 align="center">Short Range Person Logger</h1>

## Description:
In this module , the algorithm uses a face recognition system to recognize familiar faces and then logs when they are detected. This is a short range application of the same.

## Table of contents
* [About the Modules](#About-the-Modules)
* [Surveillence Usecase](#Surveillence-Usecase)
* [Setup](#Setup)
* [Demo](#Demo)


## About the Modules:
The Modules used here mainly are:
<ul>
<liOpencv</li>
<li>face_recognition(wrapped around dlib module)</li>
<li>Pickle</li>
</ul>
We make use of face_recogntion module as the main algorithm for face recogntion. it can Recognize and manipulate faces from Python or from the command line with. the world's simplest face recognition library. Built using dlib's state-of-the-art face recognition. built with deep learning.
We also use opencv as a way of capturing video from the web cam and processing it into the code. Also we pickle the encoding using Pickle module and store the trained models and encodings so that they dont need to be trained againa nd can incraese the speed od detection.

## Surveillence Usecase:
In a Surveillence it is important to keep note of who enters and when he or she enters the room or whereever we want to put up a Surveillence camera . This is a short range implementation of the idea. It helps the ownwer keep an track of the people entering the room which can help him kknow if any mishap happen in the room.Thus , this is an import application

## Setup
To run this project locally:
Go to the directory where the project is present

Write this in your Command prompt
```
$pip -r requirements.txt

```

Then after this in the command prompt and use this command
```
$ python Log_IN.py

```

## Demo

#### Training
![gif](https://github.com/adityamukherjee42/Short_Rangel_Log/blob/main/training.gif)

#### Testing
![gif](https://github.com/adityamukherjee42/Short_Rangel_Log/blob/main/identification.gif)

