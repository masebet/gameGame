import cv2

img = cv2.imread("image.jpg")      # load image
cv2.imshow("My Image", img)        # show image
cv2.waitKey(0)                     # wait for key press
cv2.destroyAllWindows()
