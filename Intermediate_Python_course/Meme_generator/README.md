**Meme_generator Project**

Second Project in the Udacity Intermediate Python Nanodegree 

In this project,  a "meme generator" is constructed – an application to generate memes: an image with an overwritten quote. 
The possible quotes to overwrite can come from a variety of file types: pdf, txt, docs, cvs.
Aditionally, a quote can be manually inserted. 

**General Overview**

The constructed application will perform the following tasks: 
    
    - Get quotes from a variety of file types: pdf, txt, docs, cvs
    - Load images and manipulate them
    - Save manipulated images with the quotes overwritten
    - Get imput to the meme creator through the command-line
    
**Folders in the project**

*_data*: SimpleLines/DogQuotes. Files with quotes in different formats(csv,docx,pdf,txt). 
                 
*templates*: HTML template files to be used as web service interaction

*QuoteEngine*: This module is responsible for ingesting many types of files that contain quotes. 
    IngestorInterface.py: contains an abstract base class, IngestorInterface, which is realized by separate strategic objects (aka helper classes) 
    for each file type. 
    Ingestor.py: Ingestor class that inherits the IngestorInterface abstract class and parses all the 
    different types of files. To parse each of the file types there are 4 different helpers: 
        CSVImporter, DocxImporte, TXTImporter, PDFImporter
    QuoteModel.py: Defines a class to store the "message body" & its corresponding "message author" once the quotes are parsed.

*MemeEngine*: This module is responsible for manipulating images and overwritting text on them. 
In the MemeEngine class, first, the image is resized and then the quote is overwritten on that image. 


**Package our Application**

*meme.py*
This script returns a path to a generated meme that is generated using the previous Quote Engine & Meme Engine modules.

*app.py*
Create a Flask app that interacts with the web service.
The app uses the Quote Engine Module and Meme Generator Modules to generate a random captioned meme.
It also captures an image from a user submitted URL.

**Output Folders**

The output memes generated are saved in tmp/static folders when running "meme.py"/ "app.py".

*tmp*: Stores the output memes generated when "meme.py" script is run

*static*: Stores the output memes generated when "app.py" script is run

**Requirements**

*Requirements.txt*
This file contains the complete list of python dependencies used throughout this project

**Note**:

I have run my code in Anaconda and created a virtual enviroment as follows with the previous 'Requirements.txt' dependencies:

conda create --name mariaenv --file requirements.txt

To activate it: 
conda activate mariaenv

It has not been possible to install 'pdftotext' and 'python-docx' from the requirements.txt because they belong to 'conda-forge' 
so have commented it in the .txt file and I have installed one the virtuall enviroment has been activated:

conda install -c conda-forge pyhton-docx
conda install -c conda-forge pdftotext


  

