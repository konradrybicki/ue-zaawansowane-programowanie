# -*- coding: utf-8 -*-

import Customer
import Product

""" Defines order structure, that contains products and customer data within it """

class Order:
    
    __id: int
    __customer: Customer
    __products: [Product]
    
    @property
    def getId(self) -> int:
        return self.__id
    
    @property
    def getCustomer(self) -> Customer:
        return self.__customer
    
    @property
    def getProducts(self) -> [Product]:
        return self.__products
     
    @id.setter
    def setId(self, value: int) -> None:
        self.__id = value
        
    @customer.setter
    def setCustomer(self, value: Customer) -> None:
        self.__customer = value
        
    @products.setter
    def setProducts(self, value: [Product]) -> None:
        self.__products = value