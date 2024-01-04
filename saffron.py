import cv2
import numpy as np

def analyze_saffron(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image to the HSV color space
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Define color ranges for saffron in HSV
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])

    lower_white = np.array([0, 0, 200])
    upper_white = np.array([180, 30, 255])

    # Threshold the image to get saffron color regions
    mask_red = cv2.inRange(hsv_image, lower_red, upper_red)
    mask_yellow = cv2.inRange(hsv_image, lower_yellow, upper_yellow)
    mask_white = cv2.inRange(hsv_image, lower_white, upper_white)

    # Extract saffron features based on color regions
    color = "red" if cv2.countNonZero(mask_red) > 0 else "yellow" if cv2.countNonZero(mask_yellow) > 0 else "white"

    # Analyze size based on contour detection
    contours, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    area = sum(cv2.contourArea(cnt) for cnt in contours)
    size = "big" if area > 1000 else "medium" if area > 500 else "small"

    # Analyze shape based on contour detection
    contours, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    shape = "straight" if len(contours) == 1 else "curved" if len(contours) > 1 else "broken"

    # Analyze thickness based on color
    thickness = "thick" if color == "red" else "medium" if color == "yellow" else "thin"

    return color, size, shape, thickness

def map_to_grade(color, size, shape, thickness):
    # Count the number of matching elements
    match_count = sum(
        elem == "red" or elem == "big" or elem == "straight" or elem == "thick"
        for elem in [color, size, shape, thickness]
    )

    # Assign grade based on matching elements
    if match_count >= 3:
        if "red" in [color, size, shape, thickness]:
            return "High"
        elif "yellow" in [color, size, shape, thickness]:
            return "Medium"
        elif "white" in [color, size, shape, thickness]:
            return "Low"
    else:
        return "Unknown"

# Example usage:
image_path = "saffron.jpg"
color, size, shape, thickness = analyze_saffron(image_path)
grade = map_to_grade(color, size, shape, thickness)

# Print the analysis results
print(f"Saffron Color: {color}, Size: {size}, Shape: {shape}, Thickness: {thickness}, Grade: {grade}")
