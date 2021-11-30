# -*- coding: utf-8 -*-

#%% flask app initialization

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/movies")
def getMovies():
    movies = getMovieData()
    return jsonify(movies)

#%% helper methods

from src.FileReader import FileReader
import src.Data

from tests.FileReaderTests import getAbsolutePathUsing

def getMovieData():
    
    # source file data read
    
    movies_relative = "data/movies.csv"
    movies_absolute = getAbsolutePathUsing(movies_relative)
    
    FileReader.sourceFilePath = movies_absolute
    movies: [[str]] = FileReader.getRows()
    
    # read data modelling and serialization
    
    movies_json = []
    
    for row in rows:
        
        movieID: int = row[0]
        title: str = row[1]
        genres: str = row[2]
        
        movie = Movie(movieID, title, genres)
        movies_json.append(movie.__dict__)
    
    return movies_json
    


