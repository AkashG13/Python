#import pyttsx3
#engine = pyttsx3.init()
#engine.say("aah just a second sir")
#engine.runAndWait()
import cv2 as cv
#imgg=cv.imread("IMG20190405014014.jpg",1)
#img=cv.resize(img,(600,600))
#cv.imshow("hiii",img)
first_frame=None
video=cv.VideoCapture(0)
a=1
while True:
    a=a+1
    check,frame=video.read()
    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
    #gray=cv.GaussainBlur(gray,(21,21),0) 
    cv.imshow('capture',frame) #if type gray video will be converted to gray
    key=cv.waitKey(1)
    if key==ord('q'):
        break
print(a)
video.release()
#cv.waitKey(0)
cv.destroyAllWindows()
