import cv2
import numpy as np

# Read the images
img = cv2.imread('img_6.png')
img1 = cv2.imread('img_5.png')

# Check if images loaded successfully
if img is None or img1 is None:
    print("Error: Could not read images!")
    exit()

# Resize the images
resized_img = cv2.resize(img.copy(), (512, 512))  # Use copy to avoid modification
resized_img1 = cv2.resize(img1.copy(), (512, 512))

# Print the shapes of the original images
print("Original image shape:", img.shape)
print("Original image 1 shape:", img1.shape)

# Function to create Gaussian pyramid (avoiding modification of original image)
def create_gaussian_pyramid(image):
    pyramid = [image.copy()]
    for _ in range(6):
        image = cv2.pyrDown(image)
        pyramid.append(image)
    return pyramid

# Create Gaussian pyramids for both images
gp_img = create_gaussian_pyramid(resized_img)
gp_img1 = create_gaussian_pyramid(resized_img1)

# Function to create Laplacian pyramid (considering channels)
def create_laplacian_pyramid(pyramid):
    laplacian_pyramid = []
    for i in range(5, 0, -1):
        guassian_extended = cv2.pyrUp(pyramid[i])
        laplacian = cv2.subtract(pyramid[i - 1], guassian_extended)
        laplacian_pyramid.append(laplacian)
    return laplacian_pyramid

# Create Laplacian pyramids for both images (handling channels)
lp_img = create_laplacian_pyramid(gp_img)
lp_img1 = create_laplacian_pyramid(gp_img1)

# Combine Laplacian pyramid levels (consider handling channels if needed)
both_image_pyramid = []
for img_lap, img1_lap in zip(lp_img, lp_img1):
    cols, rows, channels = img_lap.shape  # Consider channels
    laplacian = np.hstack((img_lap[:, 0:int(cols / 2)], img1_lap[:, int(cols / 2):]))
    both_image_pyramid.append(laplacian)

# Reconstruct the image
reconstructed_image = both_image_pyramid[0]
for i in range(6):
    reconstructed_image = cv2.pyrUp(reconstructed_image)
    reconstructed_image = cv2.add(both_image_pyramid[i], reconstructed_image)

# Display the images
cv2.imshow('Resized image 1', resized_img)
cv2.imshow('Resized image 2', resized_img1)
cv2.imshow('Reconstructed Image', reconstructed_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
