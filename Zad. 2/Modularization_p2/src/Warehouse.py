# -*- coding: utf-8 -*-

import src.Product as Product

""" Defines a warehouse structure, which can contain products within it (static class) """

class Warehouse:
    
    products: [Product]
    
    @staticmethod
    def __str__(self):
        print(f"Products in warehouse: {self.products}")