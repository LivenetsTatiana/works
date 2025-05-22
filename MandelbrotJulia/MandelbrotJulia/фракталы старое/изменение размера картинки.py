from PIL import Image

def resize(width, height, image):
    img = Image.open(image)
    resized_img = img.resize((width, height), Image.ANTIALIAS)
    resized_img.save(image)

resize(100, 100, 'image.png')