from PIL import Image, ImageFilter

image = Image.open('carezza_lake_riccardoch_unsplash.jpeg')
embossed_image = image.filter(ImageFilter.EMBOSS)
embossed_image.show()

contoured_image = image.filter(ImageFilter.CONTOUR)
contoured_image.show()

image_edges = image.filter(ImageFilter.FIND_EDGES)
image_edges.show()

smoothed_image = image.filter(ImageFilter.SMOOTH_MORE)
smoothed_image.show()

# Can save any image if needed
smoothed_image.save('smoothed_lake.jpeg')
