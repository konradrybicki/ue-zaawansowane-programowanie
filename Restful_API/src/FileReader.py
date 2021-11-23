# -*- coding: utf-8 -*-

import csv

class FileReader:
    
    """ Is responsible for reading data from a source file (movies.csv) """
    
    __sourceFilePath = '../movies.csv'
    
    @classmethod
    def getHeader(cls) -> [str]:
        
        """ Reads only the header from a source file """
        
        f = open(cls.__sourceFilePath)
        
        reader = csv.reader(f)
        header = next(reader)
        
        f.close()
        
        return header
    
    @classmethod
    def getRows(cls) -> [[str]]:
        
        """ Reads all the rows from a source file (excluding the header) """
        
        f = open(cls.__sourceFilePath, encoding='utf8')
        
        reader = csv.reader(f)
        rows = []
        
        for row in reader:
            rows.append(row)
            
        f.close()
        
        return rows