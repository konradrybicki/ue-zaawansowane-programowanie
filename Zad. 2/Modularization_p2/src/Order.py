# -*- coding: utf-8 -*-

import src.ClientModule as cmd
import src.Product as Product

""" Defines order structure, that contains products and customer data within it """

class Order:
    
    __id: int
    __client: cmd.Client
    __products: [Product]
    
    @property
    def getId(self) -> int:
        return self.__id
    
    @property
    def getClient(self) -> cmd.Client:
        return self.__client
    
    @property
    def getProducts(self) -> [Product]:
        return self.__products
     
    @id.setter
    def setId(self, value: int) -> None:
        self.__id = value
        
    @client.setter
    def setClient(self, value: cmd.Client) -> None:
        self.__client = value
        
    @products.setter
    def setProducts(self, value: [Product]) -> None:
        self.__products = value