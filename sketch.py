import cv2

# 1. Load her photo
img = cv2.imread("girlfriend.jpeg")

# 2. Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3. Invert the grayscale image
inverted = cv2.bitwise_not(gray)

# 4. Apply Gaussian Blur (this creates the sketch feel)
blurred = cv2.GaussianBlur(inverted, (111, 111), sigmaX=0, sigmaY=0)

# 5. Blend gray with blurred to get pencil sketch
sketch = cv2.divide(gray, cv2.bitwise_not(blurred), scale=256.0)

# 6. Save the sketch
cv2.imwrite("sketch_output.jpg", sketch)