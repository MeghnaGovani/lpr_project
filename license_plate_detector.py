import cv2
import pytesseract

# Set Tesseract executable path if on Windows (e.g., r'C:\Program Files\Tesseract-OCR\tesseract.exe')
# pytesseract.pytesseract.tesseract_cmd = r'<PATH_TO_TESSERACT_EXE>'

def detect_license_plate(image_path):
    # 1. Load the image
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # 2. Apply bilateral filter to reduce noise while keeping edges sharp
    gray = cv2.bilateralFilter(gray, 11, 17, 17)

    # 3. Find edges in the image
    edged = cv2.Canny(gray, 30, 200)

    # 4. Find contours in the edged image
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours = sorted(contours, key=cv2.contourArea, reverse=True)[:10]

    screen_cnt = None
    for c in contours:
        # Approximate the contour shape
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.018 * peri, True)

        # A license plate is typically rectangular (4 corners)
        if len(approx) == 4:
            screen_cnt = approx
            break

    if screen_cnt is None:
        print("No license plate contour detected.")
        return

    # 5. Extract text using Tesseract OCR
    x, y, w, h = cv2.boundingRect(screen_cnt)
    plate_crop = gray[y:y + h, x:x + w]
    text = pytesseract.image_to_string(plate_crop, config='--psm 8')

    print(f"Detected License Plate Text: {text.strip()}")

    # 6. Draw contour and display result
    cv2.drawContours(img, [screen_cnt], -1, (0, 255, 0), 3)
    cv2.imshow("License Plate Detector", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Replace 'car.jpg' with your target image file
    detect_license_plate("car.jpg")