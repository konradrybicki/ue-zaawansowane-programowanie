# -*- coding: utf-8 -*-

class Movie:
    
    """ Defines a source-file-related movie structure """
    
    movieID: int
    title: str
    genres: str
    
    def __init__(self, movieID: int, title: str, genres: str):
        self.movieID = movieID
        self.title = title
        self.genres = genres
        
class Link:

    """ Defines a source-file-related link structure """
    
    movieID: int
    imdbID: str
    tmdbID: str
    
    def __init__(self, movieID: int, imdbID: str, tmdbID: str):
        self.movieID = movieID
        self.imdbID = imdbID
        self.tmdbID = tmdbID
        
class Rating:

    """ Defines a source-file-related rating structure """
    
    userID: int
    movieID: int
    rating: int
    timestamp: str
    
    def __init__(self, userID: int, movieID: int, rating: int, timestamp: str):
        self.userID = userID
        self.movieID = movieID
        self.rating = rating
        self.timestamp = timestamp
        
class Tag:
    
    """ Defines a source-file-related tag structure """
    
    userID: int
    movieID: int
    tag: str
    timestamp: str
    
    def __init__(self, userID: int, movieID: int, tag: str, timestamp: str):
        self.userID = userID
        self.movieID = movieID
        self.tag = tag
        self.timestamp = timestamp