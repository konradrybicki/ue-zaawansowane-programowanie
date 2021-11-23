# -*- coding: utf-8 -*-

from src.FileReader import FileReader
from src.Movie import Movie

rows: [[str]] = FileReader.getRows()
movies = []

for row in rows:
    
    id = row[0]
    title = row[1]
    genres = row[2]
    
    movie = Movie(id, title, genres)
    movies.append(movie)
    
for movie in movies:
    print(movie.__dict__)