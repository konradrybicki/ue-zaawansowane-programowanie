# -*- coding: utf-8 -*-

""" Defines a single product structure """

class Product:
    
    __id: int
    __name: str
    __price: float
    __description: str
    __available: bool
    
    @property
    def getId(self) -> int:
        return self.__id
    
    @property
    def getName(self) -> str:
        return self.__name
     
    @property
    def getPrice(self) -> float:
        return self.__price
     
    @property
    def getDescription(self) -> str:
        return self.__description
     
    @property
    def getAvailabilityStatus(self) -> bool:
        return self.__available
    
    def __init__(self, id: int, name: str, price: float, description: str, available: bool):
        self.__id = id
        self.__name = name
        self.__price = price
        self.__description = description
        self.__available = available
        
    def __str__(self):
        
        id_str = str(self.id)
        price_str = str(self.price)
        available_str = str(self.available)
        
        print(f"Product data:\n\
              id: {id_str}\n\
              name: {self.name}\n\
              price: {price_str}\n\
              description: {self.description}\n\
              available: {available_str}")
