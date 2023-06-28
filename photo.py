import cv2 as cv
image = cv.imread('1.png')
cv.imshow('myimage',image)
cv.waitKey(0)
print(image.shape) 
size = (1095,1095)
image_resize=image.resize(image,size,cv.INTER_AREA)
cv.inshow('resizeimage',image_resize)

