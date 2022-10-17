import easyocr
import cv2


image = 'Test-files/test.png'

reader = easyocr.Reader(['en'], gpu=False)
result = reader.readtext(image)

img = cv2.imread(image)
for detection in result:
    text = detection[1]
    print(text)
    top_left = tuple([int(val) for val in detection[0][0]])
    bottom_right = tuple([int(val) for val in detection[0][2]])
    cv2.rectangle(img, top_left, bottom_right, (0,255,0), 2)
    cv2.putText(img, text, top_left, cv2.FONT_HERSHEY_PLAIN, .5, (255,255,255), cv2.LINE_AA)

cv2.imshow('Img', img)
cv2.waitKey(0)
