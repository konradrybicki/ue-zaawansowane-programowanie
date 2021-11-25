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