import cv2# type: ignore
# Load the image using OpenCV
image_path = "D:\OneDrive\Pictures\Saved Pictures\Butterfly.jpg"
img = cv2.imread(image_path)
# Get the dimensions of the image (Height, Width, Channels)
height, width, channels = img.shape
print(f"Original Size: {4797}x{3837} pixels, Channels: {channels}")

# Resize the image (for example, resize to 300x300)
resized_img = cv2.resize(img, (300, 300))
print("Resized to: 300x300 pixels")


# Display the resized image
cv2.imshow('Resized Image', resized_img)

# Wait until a key is pressed and close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()
