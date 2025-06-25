import os
import random
import argparse
from QuoteEngine.QuoteModel import QuoteModel
from QuoteEngine.Ingestor import Ingestor  # Add this import
from MemeEngine.MemeEngine import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an image path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/dog/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs.extend([os.path.join(root, name) for name in files])  # Use extend, not overwrite

        if not imgs:
            raise Exception(f"No images found in {images}")
        img = random.choice(imgs)
    else:
        img = path  # Use path directly, not path[0]

    if body is None:
        quote_files = [
            './_data/DogQuotes/DogQuotesTXT.txt',
            './_data/DogQuotes/DogQuotesDOCX.docx',
            './_data/DogQuotes/DogQuotesPDF.pdf',
            './_data/DogQuotes/DogQuotesCSV.csv'
        ]
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        if not quotes:
            raise Exception("No quotes found.")
        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    output_path = meme.make_meme(img, quote.body, quote.author)
    return output_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a meme from text and image")
    parser.add_argument('--path', type=str, help="Path to an image file")
    parser.add_argument('--body', type=str, help="Quote body text")
    parser.add_argument('--author', type=str, help="Author of the quote")

    args = parser.parse_args()

    print(generate_meme(args.path, args.body, args.author))
