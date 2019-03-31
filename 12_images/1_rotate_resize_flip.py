from PIL import Image

# Open image into an object in your program
image = Image.open('car_airplane_superlativeco_unsplash.jpeg')

# Rotate 90 degrees left
rotated_image = image.rotate(90, expand=True)
# Save the rotated image to a file
rotated_image.save('rotated_car_left.jpeg')

# Rotate 90 degrees right
rotated_image = image.rotate(-90, expand=True)
rotated_image.save('rotated_car_right.jpeg')

# Rotate 180 degrees
rotated_image = image.rotate(180)
rotated_image.save('rotated_car_upside_down.jpeg')

# Rotate by any angle!
rotated_image = image.rotate(42)
rotated_image.show()

# Resize to a fixed size - image may be squashed/stretched
smaller_image = image.resize((500, 500))
smaller_image.save("smaller_car.jpeg")

# Preserve aspect ratio - get image's width and height
width = image.width
height = image.height

print(width, height)

# Calculate half of width and height
# Ensure both values are int
half_width = int(width / 2)
half_height = int(height / 2)

# And call resize
half_size = image.resize((half_width, half_height))
half_size.save('half_size_car.jpeg')


# Flip image on the vertical axis, or left to right
flip_vertical = image.transpose(Image.FLIP_LEFT_RIGHT)
flip_vertical.show()

# Flip image on horizontal axis, or top to bottom
flip_horizontal = image.transpose(Image.FLIP_TOP_BOTTOM)
flip_horizontal.show()

# Create thumbnail image. Preserves aspect ratio
# Also modifies the original image -
# unlike resize, rotate, transpose, which all create a new image and don't modify the original
image.thumbnail((250, 250))
image.save('car_thumbnail.jpeg')
image.show()  # Opens the image viewing app on your computer
