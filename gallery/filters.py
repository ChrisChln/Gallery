from PIL import Image, ImageFilter, ImageEnhance, ImageOps

def apply_gray(image):
    return ImageOps.grayscale(image)

def apply_blur(image):
    return image.filter(ImageFilter.BLUR)

def apply_edge(image):
    image = ImageOps.grayscale(image)
    return image.filter(ImageFilter.FIND_EDGES)

def apply_solar(image):
    return ImageOps.solarize(image, threshold=80)

def apply_poster(image):
    return ImageOps.posterize(image, bits=3)

def apply_sepia(image):
    image = image.convert("L")
    sepia = []
    r, g, b = (239, 224, 185)
    for i in range(255):
        sepia.extend((r*i//255, g*i//255, b*i//255))
    image.putpalette(sepia)
    image = image.convert("RGB")
    return image


FILTERS = {
    'gray': apply_gray,
    'blur': apply_blur,
    'edge': apply_edge,
    'solar': apply_solar,
    'poster': apply_poster,
    'sepia': apply_sepia,
}
