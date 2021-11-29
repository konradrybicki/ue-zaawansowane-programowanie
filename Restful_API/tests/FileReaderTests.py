# -*- coding: utf-8 -*-

#%% unit tests

import unittest
from src.FileReader import FileReader

class FileReaderTests(unittest.TestCase):
    
    # boundary conditions - success
    
    def testGetRows_movies(self):
        
        # given
        movies_relative = '../data/movies.csv'
        movies_absolute = getAbsolutePathUsing(movies_relative)
        FileReader.sourceFilePath = movies_absolute
        
        # when
        movies: [[str]] = FileReader.getRows()
        
        # then
        moviesEmpty: bool = not movies
        self.assertFalse(moviesEmpty)
        
    def testGetRows_links(self):
        
        links_relative = '../data/links.csv'
        links_absolute = getAbsolutePathUsing(links_relative)
        FileReader.sourceFilePath = links_absolute
        
        links: [[str]] = FileReader.getRows()
        
        linksEmpty: bool = not links
        self.assertFalse(linksEmpty)
        
    def testGetRows_ratings(self):
        
        ratings_relative = '../data/ratings.csv'
        ratings_absolute = getAbsolutePathUsing(ratings_relative)
        FileReader.sourceFilePath = ratings_absolute
        
        ratings: [[str]] = FileReader.getRows()
        
        ratingsEmpty: bool = not ratings
        self.assertFalse(ratingsEmpty)
        
    def testGetRows_tags(self):
        
        tags_relative = '../data/tags.csv'
        tags_absolute = getAbsolutePathUsing(tags_relative)
        FileReader.sourceFilePath = tags_absolute
        
        tags: [[str]] = FileReader.getRows()
        
        tagsEmpty: bool = not tags
        self.assertFalse(tagsEmpty)
        
    # boundary conditions - failure
    
    def testGetRows_wrongPath(self):
        
        # given
        FileReader.sourceFilePath = "x"
        
        # when, then
        getRows = FileReader.getRows
        self.assertRaises(Exception, getRows, None, None)

#%% helper method

import os

def getAbsolutePathUsing(pathRelativeToCurrentFile: str) -> str:
    
    """ Returns an absolute path to a certain location, using a path relative to the current file """    
    
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, pathRelativeToCurrentFile)
    
    return filename

#%% tests launch

if __name__ == "__main__":
    unittest.main()