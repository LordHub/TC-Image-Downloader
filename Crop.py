from PIL import Image
img = Image.open("SUPERMAN_TC_RS.jpg")
half_the_width = img.size[0] / 2
half_the_height = img.size[1] / 2
reduce_the_width = half_the_width - half_the_width / 15
reduce_the_height = half_the_height - half_the_height / 15
img4 = img.crop(
    (
        half_the_width - reduce_the_width,
        half_the_height - reduce_the_height,
        half_the_width + reduce_the_width,
        half_the_height + reduce_the_height
    )
)
img4.save("img8h1.jpg")
