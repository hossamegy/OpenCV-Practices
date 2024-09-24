# OpenCV Practice Project - README.md

## Overview
This repository serves as a collection of Python scripts developed as part of my journey to learn and practice various functionalities of the OpenCV library. OpenCV, an open-source computer vision and machine learning framework, is widely used for tasks involving image and video processing. Through these scripts, I have explored fundamental concepts such as image and video manipulation, rescaling, drawing shapes, geometric transformations, filtering techniques, and working with contours and color spaces.

Each script in this repository is dedicated to a specific OpenCV technique, providing hands-on experience and a deeper understanding of core operations essential for building sophisticated computer vision applications.

## Installation Instructions
Before running the code, ensure you have Python installed, along with the necessary libraries:

1. **Install Python**: If you haven't installed Python yet, you can download it from the [official website](https://www.python.org/downloads/).
2. **Install OpenCV**: To install the required OpenCV library, run the following command:

    ```bash
    pip install opencv-python
    ```

3. **Ensure NumPy is Installed**: Some scripts also use NumPy for array manipulations. Install it using:

    ```bash
    pip install numpy
    ```

## Scripts Overview

### 1. `img_read.py`
- **Functionality**: Reads and displays an image using OpenCV.
- **Key Concepts**:
  - Reading images with `cv2.imread()`.
  - Displaying images with `cv2.imshow()`.
  - Accessing image properties like dimensions using `.shape`.

### 2. `read_video.py`
- **Functionality**: Reads and displays video frames.
- **Key Concepts**:
  - Reading videos frame by frame using `cv2.VideoCapture()`.
  - Displaying video frames in a window.
  - Loop control using keyboard input to break from the video feed (`waitKey()`).

### 3. `rescale_image.py`
- **Functionality**: Rescales an image to a specific factor.
- **Key Concepts**:
  - Rescaling images using `cv2.resize()`.
  - Custom rescale function to reduce or increase image size by a given factor.

### 4. `rescale_video.py`
- **Functionality**: Rescales a video in real-time.
- **Key Concepts**:
  - Video frame resizing using the custom rescale function.
  - Displaying the rescaled video with a dynamic scaling factor applied to each frame.

### 5. `draw.py`
- **Functionality**: Demonstrates basic drawing functionalities in OpenCV (lines, rectangles, circles, and text).
- **Key Concepts**:
  - Creating blank images with `numpy.zeros()`.
  - Drawing shapes such as rectangles, circles, and lines.
  - Adding text overlays with `cv2.putText()`.

### 6. `transformations.py`
- **Functionality**: Performs geometric transformations like translation, rotation, and flipping.
- **Key Concepts**:
  - Image translation using affine transformation matrices.
  - Rotation around a specified point.
  - Flipping images horizontally, vertically, or both.

### 7. `basics.py`
- **Functionality**: Covers fundamental image processing techniques such as color conversion, blurring, edge detection, and resizing.
- **Key Concepts**:
  - Color conversion (RGB to Grayscale).
  - Applying Gaussian blur.
  - Edge detection using the Canny edge detector.
  - Dilation and resizing of images.

### 8. `contours.py`
- **Functionality**: Detects and draws contours around objects in an image.
- **Key Concepts**:
  - Edge detection with Canny.
  - Finding contours in binary images using `cv2.findContours()`.
  - Drawing contours over blank images for visualization.

### 9. `color_spaces.py`
- **Functionality**: Explores different color spaces such as Grayscale, HSV, and LAB.
- **Key Concepts**:
  - Converting between color spaces using `cv2.cvtColor()`.
  - Displaying images in multiple color representations.

### 10. `split_merge.py`
- **Functionality**: Splits and merges the channels of an image (Red, Green, Blue channels).
- **Key Concepts**:
  - Splitting an image into its constituent color channels using `cv2.split()`.
  - Merging color channels back into an image using `cv2.merge()`.
  - Creating custom color images by merging a single channel with two empty ones.

### 11. `smothing.py`
- **Functionality**: Applies different types of blurring techniques to images.
- **Key Concepts**:
  - Averaging blur, Gaussian blur, Median blur, and Bilateral blur.
  - Understanding how different filters affect image sharpness and noise.

### 12. `bitwise.py`
- **Functionality**: Demonstrates bitwise operations on shapes (rectangle and circle).
- **Key Concepts**:
  - Creating blank images using `numpy.zeros()`.
  - Drawing shapes like rectangles and circles.
  - Applying bitwise operations (`AND`, `OR`, `XOR`, `NOT`) to the shapes.

### 13. `mask.py`
- **Functionality**: Demonstrates masking of images using shapes.
- **Key Concepts**:
  - Creating masks with shapes like rectangles and circles using `numpy` functions.
  - Applying the masks to images using `cv2.bitwise_and()` to isolate specific regions of an image.

### 14. `histogram.py`
- **Functionality**: Plots histograms for grayscale and color images.
- **Key Concepts**:
  - Calculating and plotting histograms for both grayscale and color images.
  - Masking specific regions of an image and plotting the histogram for only that region.
  - Using `matplotlib` for histogram visualization.

### 15. `thresh.py`
- **Functionality**: Applies different types of thresholding techniques to an image.
- **Key Concepts**:
  - Simple thresholding using `cv2.threshold()`.
  - Inverse thresholding and adaptive thresholding for better edge detection and segmentation.
  - Working with grayscale images and their binary transformations.

### 16. `gradient.py`
- **Functionality**: Computes gradients using various operators.
- **Key Concepts**:
  - Applying the Laplacian and Sobel operators to detect edges and compute gradients in images.
  - Combining gradient results from different axes (x, y) using bitwise operations.


## Usage
Each script can be run independently. For example, to run the `img_read.py` file, use the following command in your terminal:

```bash
python img_read.py
```
Ensure that the images and video files referenced in each script are correctly placed in the `assets/` folder.

## Assets
Make sure the images and videos that are required for the scripts are available in the `assets/` directory.
## Conclusion
This repository reflects my learning journey with OpenCV and provides a practical resource for anyone looking to get hands-on with the basics of computer vision. By exploring these scripts, you will gain a solid understanding of essential image and video processing techniques. This foundational knowledge can be further expanded upon to tackle more advanced projects and challenges in the field of computer vision.
