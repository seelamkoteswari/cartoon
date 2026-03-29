import cv2

def cartoon(img):
    return cv2.stylization(img, sigma_s=60, sigma_r=0.5)

def pencil(img):
    _, sketch = cv2.pencilSketch(img)
    return sketch

def detail(img):
    return cv2.detailEnhance(img)

def edge(img):
    return cv2.Canny(img, 100, 200)