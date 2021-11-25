# -*- coding: utf-8 -*-

class Link:

    """ Defines a source-file-related link structure """
    
    movieID: int
    imdbID: str
    tmdbID: str
    
    def __init__(self, movieID: int, imdbID: str, tmdbID: str):
        self.movieID = movieID
        self.imdbID = imdbID
        self.tmdbID = tmdbID