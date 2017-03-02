from PILLOW import Image
img = Image.open("GICOMBAT.jpg")
half_the_width = img.size[0] / 2
half_the_height = img.size[1] / 2
img4 = img.crop(
    (
        half_the_width - 50,
        half_the_height - 75,
        half_the_width + 50,
        half_the_height + 75
    )
)
img4.save("img4.jpg")