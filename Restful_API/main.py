# -*- coding: utf-8 -*-

from src.FileReader import FileReader
from src.Movie import Movie

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
    
# (print)

for movie in movies_json:
    print(movie)