#how Convert the image to gray by python => pillow
# install: pip install Pillow
# from PIL import Image

from PIL import Image

image = input("Enter The Image : ")

# Open The Image
image = Image.open(image)

# show The old Image
image.show()

image = image.convert("LA")

# Save Image
image.save('result.png')

# show The new Image
image.show()