"""

Draw text with an outline

Credit to https://mail.python.org/pipermail/image-sig/2009-May/005681.html

"""

from PIL import Image, ImageDraw, ImageFont

# The same text, in the outline color, is drawn four times -
# up a little, down a little, left a little, right a little,
# of the desired text.
# Then the text is drawn on top of the outline.

outline_color = 'orange'
text_color = 'red'

car_image = Image.open('car_airplane_superlativeco_unsplash.jpeg')

img_draw = ImageDraw.Draw(car_image)

text_x = 500   # How far to the right
text_y = 600   # How far down

outline_width = 3

text = 'Car and Airplane'

font = ImageFont.truetype('DejaVuSans.ttf', 100)
img_draw.text( [text_x + outline_width, text_y], text=text, fill=outline_color, font=font)  # To the right
img_draw.text( [text_x - outline_width, text_y], text=text, fill=outline_color, font=font)  # To the left
img_draw.text( [text_x, text_y + outline_width], text=text, fill=outline_color, font=font)  # Below
img_draw.text( [text_x, text_y - outline_width], text=text, fill=outline_color, font=font)  # Above

img_draw.text( [text_x, text_y], fill=text_color, text=text, font=font)

car_image.save('outline_text_image.jpg')


