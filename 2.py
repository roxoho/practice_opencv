import os,cv2
import matplotlib.pyplot as plt

img = cv2.imread(os.path.join('.','test.jpg'),0)

#print(img.shape)
#print(img[0,0],img[0,174])

img_copy=img.copy()

img_copy[100:355,400:500]=55

#plt.imshow(img_copy,cmap='gray')
#plt.show()

resize=cv2.resize(img_copy,(200,200),fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)


#resizing mantaining aspect ratio

desired_width=100
aspect_ratio=desired_width/img.shape[1]
desired_height=int(img.shape[0]*aspect_ratio)
dim=(desired_width,desired_height)

resized=cv2.resize(img_copy,dim,interpolation=cv2.INTER_AREA)


#flip
flipped=cv2.flip(img_copy,-1)

#rotate
rotated=cv2.rotate(img_copy,cv2.ROTATE_90_CLOCKWISE)

cv2.imshow('rotate',rotated)

cv2.imshow('flip',flipped)

cv2.imshow('resize',resized)

cv2.imshow('image',img_copy)
cv2.waitKey(0)
