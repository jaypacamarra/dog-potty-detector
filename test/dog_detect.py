import cv2

# Load the pre-trained Haarcascade for dog detection
dog_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Detect dogs in an image
#image = cv2.imread('dog_image_2.jpg')
image = cv2.imread('tree.jpg')
image = cv2.resize(image, (800, 600))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
dogs = dog_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

# Draw rectangles around detected dogs
for (x, y, w, h) in dogs:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 0, 255), 2)

# Display the result
while not cv2.waitKey(1) & 0xFF == ord('q'):
    cv2.imshow('Dog Detection', image)
cv2.destroyAllWindows()
