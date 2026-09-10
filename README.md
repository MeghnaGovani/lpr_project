# Automatic License Plate Recognition (ALPR)

A Python-based computer vision application that detects vehicle license plates in images using **OpenCV** for image processing and contour extraction, and **Tesseract OCR** for character recognition.

---

##  Features

* **Image Preprocessing:** Uses bilateral filtering and Canny edge detection to highlight plate contours while preserving edges.
* **Contour Detection:** Identifies rectangular bounding areas matching standard license plate geometry.
* **Text Extraction:** Utilizes Tesseract OCR to extract optical text from detected license plates.
* **Visual Output:** Highlights detected license plate regions directly on the image with bounding boxes.

---

##  Prerequisites

Before installing the Python dependencies, ensure you have **Tesseract OCR** installed on your system.

### Install Tesseract OCR

* **Windows:**
  1. Download the installer from the [Tesseract at UB Mannheim GitHub page](https://github.com/UB-Mannheim/tesseract/wiki).
  2. Run the installer and copy the installation path (default: `C:\Program Files\Tesseract-OCR\tesseract.exe`).
  
* **macOS:**
  ```bash
  brew install tesseract