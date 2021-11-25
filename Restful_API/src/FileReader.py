# -*- coding: utf-8 -*-

import csv

class FileReader:
    
    """ Is responsible for reading data from the source files """
    
    sourceFilePath: str
    
    @classmethod
    def getRows(cls) -> [[str]]:
        
        """ Reads all the rows from a specified source file (excluding the header) """
        
        f = open(cls.sourceFilePath, encoding='utf8')
        
        reader = csv.reader(f)
        rows = []
        
        for row in reader:
            rows.append(row)
        else:
            rows.pop(0)
            
        f.close()
        
        return rows