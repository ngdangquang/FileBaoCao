import cv2

img_path = "Natural.jpg"
img = cv2.imread(img_path)
cv2.imwrite('Natural_Low_Quality.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 5])
img_low = cv2.imread('Natural_Low_Quality.jpg')

cv2.imshow('Low Quality', img_low)
cv2.imshow('High Quality', img)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()
