import random
import os
import requests
from flask import Flask, render_template, abort, request

from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


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


@app.route('/prueba')
def meme_rand():
    """ Generate a random meme """

    imagen = imagenes[random.randint(0, len(imagenes))]
    quote = quotes[random.randint(0, len(quotes))]
    path = meme.make_meme(imagen, quote.body, quote.author)
    print(quote)
    #return render_template('meme.html', path=path)


#@app.route('/create', methods=['GET'])
#def meme_form():
#    """ User input for meme information """
#    return render_template('meme_form.html')
#
#
#@app.route('/create', methods=['POST'])
#def meme_post():
#    """ Create a user defined meme """
#    
#    img_url = request.form["image_url"]
#    body = request.form["body"]
#    author = request.form["author"]
#    r = requests.get(imag_url)
#    tmp = f'./tmp/imagen_tmp_{random.randint(0,100000000)}.png'
#
#    open(tmp,'wb').write(r.content)
#
#    path = meme.make_meme(tmp, body, author) 
#    
#    os.remove(tmp)
#
#    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()


