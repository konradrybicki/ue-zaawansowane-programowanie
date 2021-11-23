# -*- coding: utf-8 -*-

import unittest
from src.FileReader import FileReader

class FileReaderTests(unittest.TestCase):
    
    def testGetHeader(self):
        header = FileReader.getHeader()
        self.assertIsNotNone(header)
        
    def testGetRows(self):
        rows = FileReader.getRows()
        rowsEmpty = not rows
        self.assertFalse(rowsEmpty)
    
if __name__ == "__main__":
    unittest.main()