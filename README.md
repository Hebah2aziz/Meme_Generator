*Meme Generator

"""A Python application to generate memes by combining quote text with images.

This project includes:

Object-Oriented Design using abstract base classes.
Quote ingestion from multiple file formats (.txt, .csv, .docx, .pdf).
Meme image creation using the Pillow library.
A Flask web server to create memes via a web interface.
Command-line interface (CLI) support with optional arguments.
PEP8-compliant code and modular architecture. """
Project Setup

"""Install required dependencies and prepare the environment."""

Clone the repository:
git clone https://github.com/Hebah2aziz/meme-generator.git
cd meme-generator
Create and activate a virtual environment:
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
Install dependencies:
pip install -r requirements.txt
Project Structure

"""Directory layout of the application."""

.
├── app.py                  # Flask web app
├── main.py                 # CLI for meme generation
├── MemeEngine/
│   └── MemeEngine.py       # Meme creation logic
├── QuoteEngine/
│   ├── QuoteModel.py       # Quote data model
│   ├── Ingestor.py         # Unified interface
│   ├── IngestorInterface.py
│   ├── TextIngestor.py
│   ├── CSVIngestor.py
│   ├── DocxIngestor.py
│   └── PDFIngestor.py
├── templates/              # Flask HTML templates
├── static/                 # Generated memes (for Flask)
├── tmp/                    # Temporary output (CLI)
└── data/                  # Input images and quote files

Usage: CLI

"""Run meme generation from the terminal using optional parameters."""

Arguments
Argument	Description	Required
--path	Path to image file	No
--body	Text body of the quote	No
--author	Author of the quote (required with body)	No
Examples
# Generate a random meme
python main.py

# Generate a meme with a custom quote
python main.py --body "Stay curious." --author "Einstein"

# Generate a meme with custom image and quote
python main.py --path ./_data/photos/dog/dog1.jpg --body "Think different." --author "Apple"
Usage: Web App

"""Use a browser interface to generate memes."""

Run the server
python app.py
Available routes
GET / – generate a random meme
GET /create – form to input custom meme
POST /create – generate meme from user input (image URL + quote)
MemeEngine

"""Generate memes by overlaying quotes on images."""

from MemeEngine.MemeEngine import MemeEngine

meme = MemeEngine('./output')
path = meme.make_meme(
    img_path='./_data/photos/dog/dog1.jpg',
    text='Be yourself; everyone else is taken.',
    author='Oscar Wilde'
)
print(f'Meme saved at: {path}')
Key Features
Resizes image to fixed width (default 500px)
Adds wrapped text quote and author
Randomly places text on image
Saves image with random filename in output directory
Font Handling
Uses ./fonts/LilitaOne-Regular.ttf if available
Falls back to system font if not found
QuoteEngine

"""Extract quotes from multiple file types."""

Supported Formats
Format	Parser	Library Used
.txt	TextIngestor	built-in open()
.csv	CSVIngestor	pandas
.docx	DocxIngestor	python-docx
.pdf	PDFIngestor	subprocess with pdftotext CLI
Usage Example
from QuoteEngine.Ingestor import Ingestor

quotes = Ingestor.parse("./_data/DogQuotes/DogQuotesTXT.txt")
for quote in quotes:
    print(quote)
Error Handling

"""Graceful error reporting with human-readable messages."""

Invalid image paths
Unsupported file types
Empty quotes or image directories
Image download errors in web app
Missing author if body is provided
Testing

"""Example to test image + quote generation together."""

from QuoteEngine.Ingestor import Ingestor
from MemeEngine.MemeEngine import MemeEngine

quotes = Ingestor.parse("_data/DogQuotes/DogQuotesTXT.txt")
meme = MemeEngine('./output')
output = meme.make_meme('./_data/photos/dog/dog1.jpg', quotes[0].body, quotes[0].author)
print(output)
Requirements

"""All dependencies are in requirements.txt"""

pip install -r requirements.txt
Flask
Pillow
Requests
Pandas
python-docx
