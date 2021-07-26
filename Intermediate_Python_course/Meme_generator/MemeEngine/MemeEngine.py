"""Definition on MemeEngine Class to generate a meme."""


import os
import random
from PIL import Image, ImageDraw, ImageFont


class MemeEngine():
    """Class for meme generation.

    This class creates a meme given an image and a quote
    """

    def __init__(self, out_dir: str):
        """Class instantiation."""
        self.out_dir = out_dir
        
        if not os.path.exists(self.out_dir):
            os.mkdir(self.out_dir)

    def make_meme(self, img_path: str, text, author, width=500) -> str:
        """Create a Meme with an asociated text and author of the text.

        Arguments:
            img_path {str} -- the file location for the input image.
            text {str} -- the text to be included to the output image.
            author {str} -- the author of the text included.
        Returns:
            str -- the path where the output image is saved.
        """
        imagen = Image.open(img_path)
        outfile = f'{self.out_dir}/{random.randint(0, 1000)}.png'

        if width is not None:
            ratio = width/float(imagen.size[0])
            height = int(ratio*float(imagen.size[1]))
            imagen = imagen.resize((width, height), Image.NEAREST)

        if text is not None and author is not None:
            mensaje = f'{text} - {author}'
            draw = ImageDraw.Draw(imagen)
            font = ImageFont.truetype('./_data/fonts/LilitaOne-Regular.ttf',
                                      size=20)
            draw.text((10, 30), mensaje, font=font, fill='yellow')

        imagen.save(outfile, 'JPEG')
        return outfile
