import cv2 
import arabic_reshaper
from bidi.algorithm import get_display
import numpy as np 
from PIL import ImageFont, ImageDraw, Image

class Zarnevis:
    def __init__(self, image, text, font_file, font_size, text_coords, color) -> None:
        self.image = image
        self.text = text
        self.font_file = font_file
        self.font_size = font_size
        self.text_coords = text_coords
        self.color = color

    def draw_text(self):
        font = ImageFont.truetype(self.font_file, size=self.font_size)
        image_array = Image.fromarray(self.image)
        draw = ImageDraw.Draw(image_array)
        final_image = draw.text(self.text_coords, self.text, font=font, fill=self.color)

        return np.array(final_image)