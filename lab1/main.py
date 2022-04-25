from PIL import Image, ImageEnhance
from skimage import io

# reading image
postmark_image = Image.open("./images/postmark.png", mode="r")
#postmark_image.show()

# croping an image
dim = (50,50, 200, 200)
cropped_image = postmark_image.crop(dim)

# writing or saving image
cropped_image.save("./images/cropped_postmark.png")

# changing between color spaces
coordinates = (50, 50)
print(f"RGB pixel {coordinates} coordinate value : {postmark_image.getpixel(coordinates)}")
print(f"grey scale pixel {coordinates} coordinate value : {postmark_image.convert('L').getpixel(coordinates)}")

# visualize the different channels of an RGB image
R, G, B = postmark_image.split()
R.save("./images/R.png")
G.save("./images/G.png")
B.save("./images/B.png")

# convert to gray
grey_postmark_image = postmark_image.convert("L")
grey_postmark_image.save("./images/grey_postmark_image.png")

# resize image
resize_dim = (480, 410)
resized_postmark_image = postmark_image.resize(resize_dim)
resized_postmark_image.save("./images/resized_postmark_image.png")

# rotate image
angle = 90
rotated_postmark_image = postmark_image.rotate(angle)
rotated_postmark_image.save("./images/rotated_postmark_image.png")

# image enhancement
# brightness
enhancer = ImageEnhance.Brightness(postmark_image)
enhancer.enhance(2).save("./images/brightness.png")

# contrast
enhancer = ImageEnhance.Contrast(postmark_image)
enhancer.enhance(2).save("./images/contrast.png")

# accessing pixels of an image
updated_pixel = (11, 112, 200)
print(f"RGB pixel {coordinates} coordinate value : {postmark_image.getpixel(coordinates)}")
print(f"RGB pixel {coordinates} coordinate value is set to {updated_pixel}")
postmark_image.putpixel(coordinates, updated_pixel)
print(f"RGB pixel {coordinates} coordinate value : {postmark_image.getpixel(coordinates)}")

# scikit-image
# reading an image
