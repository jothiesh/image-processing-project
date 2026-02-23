import cv2

img = cv2.imread("girlfriend.jpeg")

# Smooth the image while keeping edges sharp
color = cv2.bilateralFilter(img, 9, 300, 300)

# Detect edges
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 7)
edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                               cv2.THRESH_BINARY, blockSize=9, C=2)

# Combine edges with color
cartoon = cv2.bitwise_and(color, color, mask=edges)

cv2.imwrite("cartoon_output.jpg", cartoon)