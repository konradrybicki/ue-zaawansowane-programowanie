# -*- coding: utf-8 -*-

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