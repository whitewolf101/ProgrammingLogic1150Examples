from PIL import Image, ImageDraw, ImageFont

hard_drive_image = Image.open('hard_drive_heapdump_unsplash.jpeg')

img_draw = ImageDraw.Draw(hard_drive_image)

# The img_draw object modifies the original image

# The list of points are the coordinates of the top left corner X and Y,
# and the bottom right corner X and Y.
img_draw.rectangle([900, 620, 1100, 720], outline='red')

# Ensure you have the font file DejaVuSans.ttf in your project
# Can use other fonts if desired - can find font files online
font = ImageFont.truetype('DejaVuSans.ttf', 50)
img_draw.text([780, 780], 'read/write head', fill='purple', font=font)

hard_drive_image.show()


# Draw on another image

new_york_image = Image.open('new_york_robertbye_unsplash.jpeg')
new_york_image.thumbnail((800, 800))   # Resize - can combine Pillow options

img_draw = ImageDraw.Draw(new_york_image)

img_draw.rectangle([275, 75, 370, 300], outline='cyan')
img_draw.text([20, 10], 'Chrysler Building', fill='orange', font=font)

new_york_image.show()
