import random
import os
import requests
from flask import Flask, render_template, abort, request


from MemeEngine.MemeEngine import MemeEngine
from QuoteEngine.Ingestor import Ingestor

app = Flask(__name__)
meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = [
        './_data/DogQuotes/DogQuotesTXT.txt',
        './_data/DogQuotes/DogQuotesDOCX.docx',
        './_data/DogQuotes/DogQuotesPDF.pdf',
        './_data/DogQuotes/DogQuotesCSV.csv'
    ]

  
    quotes = []
    for file in quote_files:
        try:
            quotes.extend(Ingestor.parse(file))
        except Exception as e:
            print(f"Error parsing {file}: {e}")

  
    images_path = "./_data/photos/dog/"
    imgs = []
    for root, _, files in os.walk(images_path):
        imgs.extend([
            os.path.join(root, name)
            for name in files if name.lower().endswith(('jpg', 'png', 'jpeg'))
        ])

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    if not quotes or not imgs:
        return "Quotes or images not found!", 500

    quote = random.choice(quotes)
    img = random.choice(imgs)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    image_url = request.form.get('image_url')
    body = request.form.get('body')
    author = request.form.get('author')

    if not image_url or not body or not author:
        return "All fields are required!", 400

    try:
       
        response = requests.get(image_url)
        if response.status_code != 200:
            return "Unable to download image from URL", 400

        tmp_image_path = f"./tmp/{random.randint(0, 1000000)}.jpg"
        os.makedirs(os.path.dirname(tmp_image_path), exist_ok=True)

        with open(tmp_image_path, 'wb') as f:
            f.write(response.content)

     
        path = meme.make_meme(tmp_image_path, body, author)

     
        os.remove(tmp_image_path)

    except Exception as e:
        return f"Error creating meme: {e}", 500

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
