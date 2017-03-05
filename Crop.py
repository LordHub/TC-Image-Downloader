from PIL import Image
def cropImage(file_name):
    img = Image.open(file_name)
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
    img4.save(file_name)
