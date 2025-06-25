from PIL import Image, ImageDraw, ImageFont
import os
import random
import textwrap


class MemeEngine:
    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def make_meme(self, img_path: str, text: str, author: str, width: int = 500) -> str:
        """Create a meme with quote text and save it to the output directory.

        Args:
            img_path (str): path to the input image
            text (str): quote text
            author (str): quote author
            width (int): optional desired image width

        Returns:
            str: path to the saved meme image
        """
        try:
            img = Image.open(img_path)
        except Exception as e:
            raise ValueError(f"Cannot open image {img_path}: {e}")

        # Resize image keeping aspect ratio
        original_width, original_height = img.size
        ratio = width / float(original_width)
        height = int(ratio * original_height)
        img = img.resize((width, height), Image.Resampling.LANCZOS)

        draw = ImageDraw.Draw(img)
        font_path = "./fonts/LilitaOne-Regular.ttf"  
        try:
            font = ImageFont.truetype(font_path, size=20)
        except IOError:
            font = ImageFont.load_default()

        quote = f'"{text}"\n- {author}'
        wrapped = textwrap.fill(quote, width=40)

        # Calculate approximate text size
        # Note: multiline_textbbox is better but requires Pillow >= 8.0.0
        # fallback to multiline_textsize if needed
        
        try:
            bbox = draw.multiline_textbbox((0, 0), wrapped, font=font, stroke_width=1)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
        except AttributeError:
            text_width, text_height = draw.multiline_textsize(wrapped, font=font)

        # Make sure text fits inside image
        max_x = max(10, width - text_width - 10)
        max_y = max(10, height - text_height - 10)

        x = random.randint(10, max_x)
        y = random.randint(10, max_y)

        draw.multiline_text(
            (x, y),
            wrapped,
            font=font,
            fill='white',
            stroke_fill='black',
            stroke_width=1,
            spacing=4
        )

        # Save meme to output directory
        out_path = os.path.join(self.output_dir, f'meme_{random.randint(0, 1000000)}.jpg')
        img.save(out_path)

        return out_path
