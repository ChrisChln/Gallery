from PIL import Image, ImageFilter, ImageEnhance

def apply_gray(image):
    return image.convert('L')

def apply_blur(image):
    return image.filter(ImageFilter.GaussianBlur(radius=2))

def apply_edge(image):
    return image.filter(ImageFilter.FIND_EDGES)

def apply_solar(image):
    return ImageEnhance.Brightness(image).enhance(1.5)

FILTERS = {
    'gray': apply_gray,
    'blur': apply_blur,
    'edge': apply_edge,
    'solar': apply_solar
}