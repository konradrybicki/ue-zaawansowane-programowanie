# -*- coding: utf-8 -*-

import src.ClientModule as cm
import src.Product as Product

""" Defines order structure, that contains products and customer data within it """

class Order:
    
    __id: int
    __client: cm.Client
    __products: [Product]
    
    @property
    def id(self) -> int:
        return self.__id
    
    @property
    def client(self) -> cm.Client:
        return self.__client
    
    @property
    def products(self) -> [Product]:
        return self.__products
     
    @id.setter
    def id(self, value: int) -> None:
        self.__id = value
        
    @client.setter
    def client(self, value: cm.Client) -> None:
        self.__client = value
        
    @products.setter
    def products(self, value: [Product]) -> None:
        self.__products = value