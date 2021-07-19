# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 14:37:34 2021

@author: U324451
"""
import random
import os
import requests
from flask import Flask, render_template, abort, request

from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeEngine

meme = MemeEngine('./static')

app = Flask(__name__)

def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/dog/"

    imagenes =[]
    for root, dirs, files in os.walk(images_path):
        imagenes = [os.path.join(root, name) for name in files]

    return quotes, imagenes


quotes, imagenes = setup()

@app.route('/hola2')
def meme_rand():
    """ Generate a random meme """

    imagen = imagenes[random.randint(0, len(imagenes))]
    quote = quotes[random.randint(0, len(quotes))]
    path = meme.make_meme(imagen, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')
   
if __name__ == "__main__":
      app.run()



