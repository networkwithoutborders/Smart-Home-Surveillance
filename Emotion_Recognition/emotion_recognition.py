from deepface import DeepFace
import cv2
import matplotlib.pyplot as plt

src=cv2.imread('happy.png')
plt.imshow(src[:,:,::-1])
plt.show()

result = DeepFace.analyze(src, actions= ['emotion'])
print(result)