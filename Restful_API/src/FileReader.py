# -*- coding: utf-8 -*-

import csv

class FileReader:
    
    """ Is responsible for reading data from a source file (movies.csv) """
    
    __sourceFilePath: '../movies.csv'
    
    @staticmethod
    def getHeader(self) -> []:
        
        """ Reads only the header from a source file """
        
        f = open(self.__sourceFilePath)
        
        reader = csv.reader(f)
        header = next(reader)
        
        f.close()
        
        return header
    
    @staticmethod
    def getRows(self) -> [[]]:
        
        """ Reads all the rows from a source file (excluding the header) """
        
        f = open(self.__sourceFilePath)
        
        reader = csv.reader(f)
        container = []
        
        for row in reader:
            container.append(row)
            
        f.close()
        
        return container