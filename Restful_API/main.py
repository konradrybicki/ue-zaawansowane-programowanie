#%% Movie data gathering

from src.FileReader import FileReader
from src.Movie import Movie

def getMovieData():
    
    # source file data read

    rows: [[str]] = FileReader.getRows()
    
    # read data modelling and serialization
    
    movies_json = []
    
    for row in rows:
        
        id = row[0]
        title = row[1]
        genres = row[2]
        
        movie = Movie(id, title, genres)
        movies_json.append(movie.__dict__)
    
    return movies_json
    
#%% Flask app initialization

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/movies")
def getMovies():
    movies = getMovieData()
    return jsonify(movies)