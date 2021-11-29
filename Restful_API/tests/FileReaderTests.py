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
        rows: [[str]] = FileReader.getRows()
        
        # then
        rowsEmpty: bool = not rows
        self.assertFalse(rowsEmpty)
        
    

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