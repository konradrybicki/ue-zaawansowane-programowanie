# -*- coding: utf-8 -*-

#%% Flask app initialization

from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/movies")
def getMovies():
    movies: [json] = getJsonData_movies()
    return jsonify(movies)

@app.route("/links")
def getLinks():
    links: [json] = getJsonData_links()
    return jsonify(links)

@app.route("/ratings")
def getRatings():
    ratings: [json] = getJsonData_ratings()
    return jsonify(ratings)

@app.route("/tags")
def getTags():
    tags: [json] = getJsonData_tags()
    return jsonify(tags)

#%% Data gathering methods

from src.FileReader import FileReader
from src.Data import Movie, Link, Rating, Tag

from tests.FileReaderTests import getAbsolutePathUsing

def getJsonData_movies():
    
    # source file data reading
    
    movies_relative = "data/movies.csv"
    movies_absolute = getAbsolutePathUsing(movies_relative)
    
    FileReader.sourceFilePath = movies_absolute
    movies: [[str]] = FileReader.getRows()
    
    # read data modelling and serialization
    
    movies_json = []
    
    for row in movies:
        
        movieID: int = row[0]
        title: str = row[1]
        genres: str = row[2]
        
        movie = Movie(movieID, title, genres)
        movies_json.append(movie.__dict__)
    
    return movies_json

def getJsonData_links():
    
    links_relative = "data/links.csv"
    links_absolute = getAbsolutePathUsing(links_relative)
    
    FileReader.sourceFilePath = links_absolute
    links: [[str]] = FileReader.getRows()
    
    links_json = []
    
    for row in links:
        
        movieID: int = row[0]
        imdbID: str = row[1]
        tmdbID: str = row[2]
        
        link = Link(movieID, imdbID, tmdbID)
        links_json.append(link.__dict__)
    
    return links_json

def getJsonData_ratings():
    
    ratings_relative = "data/ratings.csv"
    ratings_absolute = getAbsolutePathUsing(ratings_relative)
    
    FileReader.sourceFilePath = ratings_absolute
    ratings: [[str]] = FileReader.getRows()
    
    ratings_json = []
    
    for row in ratings:
        
        userID: int = row[0]
        movieID: int = row[1]
        rating: int = row[2]
        timestamp: str = row[3]
        
        rating = Rating(userID, movieID, rating, timestamp)
        ratings_json.append(rating.__dict__)
    
    return ratings_json

def getJsonData_tags():
    
    tags_relative = "data/tags.csv"
    tags_absolute = getAbsolutePathUsing(tags_relative)
    
    FileReader.sourceFilePath = tags_absolute
    tags: [[str]] = FileReader.getRows()
    
    tags_json = []
    
    for row in tags:
        
        userID: int = row[0]
        movieID: int = row[1]
        tag: str = row[2]
        timestamp: str = row[3]
        
        tag = Tag(userID, movieID, tag, timestamp)
        tags_json.append(tag.__dict__)
    
    return tags_json

#%% JSON type alias (dict)

from typing import NewType
json = NewType("json", dict)