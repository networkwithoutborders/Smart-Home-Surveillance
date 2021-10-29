<h1 align="center">Person Counter</h1>

## Description:
It is a very quick implementation of counteing number of people in a room using Mobilenet SSD detector.This can help in the Surveillance and especially in covid time where there should not be more than certain amount of people in the room.

## Table of contents
* [About the Modules](#About-the-Modules)
* [Surveillence Usecase](#Surveillence-Usecase)
* [Setup](#Setup)
* [Demo](#Demo)


## About the Modules:
The Modules used here mainly are:
<ul>
<liOpencv</li>
<li>imutills</li>
<li>Numpy</li>
</ul>
We make the use of single shot detection algorithim for detection of humans that are present in the room .Single Shot detector like YOLO takes only one shot to detect multiple objects present in an image using multibox.It is significantly faster in speed and high-accuracy object detection algorithm. SSD also fits our requiremnts of high fps and light weight python program 

## Surveillence Usecase:
During these times of Covid,it is a must to follow the SOP and curb the chain of transmission. In this one of the main Protocols to be followed is Social distancing and not overcrowding any rooms . The Person Counting code  will help us in the Surveillance of weather the room is overcrowded or not and thus keep an eye weather the SOPS are being followed and then curb the spread of COIVD  

## Setup
To run this project locally:
Go to the directory where the project is present

Write this in your Command prompt
```
$pip -r rquirements.txt

```

Then after this in the command prompt and use this command
```
$ python Person_Counter.py

```

## Demo
![gif](https://github.com/adityamukherjee42/OPENCV-PEOPLE_COUNTER/blob/main/video.gif)


## Contributors
<table>
<tr align="center">


<td>
Aditya Mukherjee

<p align="center">
<img src = "https://avatars.githubusercontent.com/adityamukherjee42"  height="120" alt="Aditya Mukherjee">
</p>
<p align="center">
<a href = "https://github.com/adityamukherjee42"><img src = "http://www.iconninja.com/files/241/825/211/round-collaboration-social-github-code-circle-network-icon.svg" width="36" height = "36"/></a>
<a href = "https://www.linkedin.com/in/aditya-mukherjee-817a17190/">
<img src = "http://www.iconninja.com/files/863/607/751/network-linkedin-social-connection-circular-circle-media-icon.svg" width="36" height="36"/>
</a>
</p>
</td>
</table>
</tr>
