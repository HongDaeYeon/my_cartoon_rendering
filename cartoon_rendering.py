import cv2

img = cv2.imread('dog.jpg')

img = cv2.resize(img, (600, 600))

def cartoonize_image(img):
    
    img_color = cv2.pyrMeanShiftFiltering(img, 21, 51)

    img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
    
    img_gray = cv2.medianBlur(img_gray, 5)
    
    edges = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    
    img_cartoon = cv2.bitwise_and(img_color, img_color, mask=edges)
    
    return img_cartoon

cartoon_img = cartoonize_image(img)

cv2.imshow('Cartoonized Image', cartoon_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('cartoon_image.jpg', cartoon_img)