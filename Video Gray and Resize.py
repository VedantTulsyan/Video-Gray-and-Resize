import cv2 as cv

path=input("Give video path : ")

new_size=int(input("Enter the size to be reduced (in percentage): "))
new_size= new_size/100

capture = cv.VideoCapture(path)

def Resize(frame, size):
    
    width=int(frame.shape[1]*size)
    height=int(frame.shape[0]*size)

    dimentions=(width,height)

    return cv.resize(frame, dimentions,interpolation=cv.INTER_AREA)

while True:
    isTrue, vid = capture.read()

    # Read video
    cv.imshow('Real Video',vid)

    #grayscaling
    gray = cv.cvtColor(vid, cv.COLOR_BGR2GRAY)

    #Resizing
    newvid = Resize(gray,new_size)
    
    cv.imshow('New Video',newvid)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break
capture.release()

cv.destroyAllWindows()
