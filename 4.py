import cv2,sys

s=0
if len(sys.argv)>1:
    s=int(sys.argv[1])

source = cv2.VideoCapture(s)

window_name = 'Video'
cv2.namedWindow(window_name,cv2.WINDOW_NORMAL)
while cv2.waitKey(1)!=27:
    ret,frame = source.read()
    if ret==False:
        break
    cv2.imshow(window_name,frame)

source.release()
cv2.destroyWindow(window_name)
