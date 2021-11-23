# -*- coding: utf-8 -*-

class Movie:
    
    """ Defines a source-file-related movie structure """
    
    id: int
    title: str
    genres: str
    
    def __init__(self, id: str, title: str, genres: str):
        self.id = id
        self.title = title
        self.genres = genres