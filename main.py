import os, cv2


img = cv2.imread(os.path.join('.','test.jpg'))
img_2 = cv2.imread(os.path.join('.','test2.jpg'),1)

b,g,r = cv2.split(img_2)
#print(img.shape)
#print(img.dtype)
converted = cv2.cvtColor(img_2, cv2.COLOR_BGR2HSV)

h,s,v = cv2.split(converted)

h=h+50
converted = cv2.merge([h,s,v])
converted = cv2.cvtColor(converted, cv2.COLOR_HSV2BGR)
#cv2.imshow('h',h)
#cv2.imshow('s',s)
#cv2.imshow('v',v)
cv2.imshow('converted',converted)

#cv2.imshow('b',b)
#cv2.imshow('g',g)
#cv2.imshow('r',r)
#cv2.imshow('image',img_2)
cv2.waitKey(0)


