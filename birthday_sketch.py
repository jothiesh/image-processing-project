# 3) Strong pencil sketch (more drawing-like, with paper texture)

# smooth while keeping edges
img_small = cv2.bilateralFilter(img, d=9, sigmaColor=75, sigmaSpace=75)

gray = cv2.cvtColor(img_small, cv2.COLOR_BGR2GRAY)

# strong edges for pencil lines
edges = cv2.Canny(gray, 40, 120)
edges = cv2.GaussianBlur(edges, (3, 3), 0)

# tone using dodge blend
inv = 255 - gray
blur = cv2.GaussianBlur(inv, (25, 25), 0)
blend = 255 - blur
blend[blend == 0] = 1
tone = (gray * 255 / blend)
tone = np.clip(tone, 0, 255).astype("uint8")

# combine tone + edges
sketch = cv2.subtract(tone, edges // 2)
sketch = np.clip(sketch, 0, 255).astype("uint8")

# add "paper" texture so it feels like real drawing
H, W = sketch.shape[:2]
paper = np.random.normal(235, 10, (H, W)).astype("uint8")  # light paper with grain
sketch = cv2.multiply(sketch, paper, scale=1 / 255.0)

# back to BGR so we can draw colored text on it
sketch_bgr = cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)