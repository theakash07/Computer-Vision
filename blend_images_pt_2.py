
import cv2
import numpy as np

# Step 1: Read images and resize them
img1 = cv2.imread('Snapchat-135456721.jpg')
img2 = cv2.imread('img_6.png')

# Resize both images to the same dimensions
imgr1 = cv2.resize(img1, (512, 512))
imgr2 = cv2.resize(img2, (512, 512))

# Ensure both images have the same size
if imgr1.shape != imgr2.shape:
    raise ValueError("Images must have the same dimensions for blending")

# Blend the images horizontally
bothimage = np.hstack((imgr1[:, :256], imgr2[:, 256:]))

# Print the dimensions of the images
print(imgr1.shape)
print(imgr2.shape)

# Step 3: Generate Gaussian and Laplacian pyramids for blending
# Generate Gaussian pyramid for img1
imgr1_copy = imgr1.copy()
gp_imgr1 = [imgr1_copy]
for i in range(6):
    imgr1_copy = cv2.pyrDown(imgr1_copy)
    gp_imgr1.append(imgr1_copy)

# Generate Gaussian pyramid for img2
imgr2_copy = imgr2.copy()
gp_imgr2 = [imgr2_copy]
for i in range(6):
    imgr2_copy = cv2.pyrDown(imgr2_copy)
    gp_imgr2.append(imgr2_copy)

# Generate Laplacian pyramid for img1
imgr1_copy = gp_imgr1[5]
lp_imgr1 = [imgr1_copy]
for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp_imgr1[i])
    laplacian = cv2.subtract(gp_imgr1[i - 1], gaussian_extended)
    lp_imgr1.append(laplacian)

# Generate Laplacian pyramid for img2
imgr2_copy = gp_imgr2[5]
lp_imgr2 = [imgr2_copy]
for i in range(5, 0, -1):
    gaussian_extended = cv2.pyrUp(gp_imgr2[i])
    laplacian = cv2.subtract(gp_imgr2[i - 1], gaussian_extended)
    lp_imgr2.append(laplacian)

# Combine left half of img1 and right half of img2 in each level
img1_img2_pyramid = []
for img1_lap, img2_lap in zip(lp_imgr1, lp_imgr2):
    cols, rows, ch = img1_lap.shape
    laplacian = np.hstack((img1_lap[:, :int(cols/2)], img2_lap[:, int(cols/2):]))
    img1_img2_pyramid.append(laplacian)

# Reconstruct the blended image
img1_img2_reconstruct = img1_img2_pyramid[0]
for i in range(1, 6):
    img1_img2_reconstruct = cv2.pyrUp(img1_img2_reconstruct)
    img1_img2_reconstruct = cv2.add(img1_img2_pyramid[i], img1_img2_reconstruct)

# Display the images
cv2.imshow('img1', imgr1)
cv2.imshow('img2', imgr2)
cv2.imshow('bothimage', bothimage)
cv2.imshow('reconstruct', img1_img2_reconstruct)

cv2.waitKey(0)
cv2.destroyAllWindows()
