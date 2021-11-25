# -*- coding: utf-8 -*-

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