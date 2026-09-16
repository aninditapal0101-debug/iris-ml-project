import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread("sample.jpg")

# Check if image is loaded
if image is None:
    print("Error: Image not found!")
    exit()

# Convert BGR to RGB (OpenCV uses BGR by default)
rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert to Grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Resize the image
resized_image = cv2.resize(rgb_image, (300, 300))

# Display images
plt.figure(figsize=(10, 4))

plt.subplot(1, 3, 1)
plt.imshow(rgb_image)
plt.title("Original")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(gray_image, cmap="gray")
plt.title("Grayscale")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(resized_image)
plt.title("Resized")
plt.axis("off")

plt.show()

# Save grayscale image
cv2.imwrite("gray_output.jpg", gray_image)

print("Image processing completed successfully!")