import os, cv2
import numpy as np

img = cv2.imread(os.path.join('.','test.jpeg'))


#brightness and darkness

matrix = np.ones(img.shape,dtype='uint8')*50

bright = cv2.add(img,matrix)
dark = cv2.subtract(img,matrix)


#contrast

matrix1 = np.ones(img.shape,dtype='uint8')*0.7
matrix2 = np.ones(img.shape,dtype='uint8')*1.3

contrast1 = np.uint8(cv2.multiply(np.float64(img),matrix1))
contrast2 = np.uint8(np.clip(cv2.multiply(np.float64(img),matrix2),0,255))

#cv2.imshow('contrast1',contrast1)
#cv2.imshow('contrast2',contrast2)

#cv2.imshow('bright',bright)
#cv2.imshow('dark',dark)


#bitwise

circle = cv2.imread(os.path.join('.','circle.jpg'),0)
rectangle = cv2.imread(os.path.join('.','rect.jpg'),0)

rectangle = cv2.resize(rectangle,(circle.shape[1],circle.shape[0]))
#print(circle)
#print(rectangle)
#cv2.imshow('circle',circle)
#cv2.imshow('rectangle',rectangle)
#and_ = cv2.bitwise_and(circle,rectangle,mask=circle)
or_ = cv2.bitwise_or(circle,rectangle)
xor_ = cv2.bitwise_xor(circle,rectangle)
not_ = cv2.bitwise_not(circle)

#print(and_)
#cv2.imshow('and',and_)
#cv2.imshow('or',or_)
cv2.imshow('xor',xor_)
cv2.imshow('not',not_)




#cv2.imshow('image',img)
cv2.waitKey(0)

