import cv2
cascpath = "haarcascade_frontalface_default.xml"

faceCascade = cv2.CascadeClassifier(cascpath)

image = cv2.imread('1.png')
cv2.waitKey(0)
cv2.imshow('image',image)
gray =  cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(

gray,
scaleFactor=1.1,
minNeighbors=11,
minSize=(1,1),
flags = cv2.CASCADE_SCALE_IMAGE
)

print("Detected {0} faces!", format(len(faces)))

# This draws a green rectangle around the faces detected

for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y), (x+w, y+h), (0,255,0),2)

    cv2.imshow('Faces Detected', image)
    cv2.waitKey(0)