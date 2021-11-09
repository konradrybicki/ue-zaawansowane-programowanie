# -*- coding: utf-8 -*-

""" Defines an overall client structure """

class Client:
    _id: int
    _adress: str
    
""" Defines a detailed client structure """

class DetailedClient(Client):
    
    __name: str
    __surname: str
    
    @property
    def getId(self) -> int:
        return self.__id
    
    @property
    def getAdress(self) -> str:
        return self.__adress
    
    @property
    def getName(self) -> str:
        return self.__name
    
    @property
    def getSurname(self) -> str:
        return self.__surname
    
    def __init__(self, id: int, adress: str, name: str, surname: str):
        self.__id = id
        self.__adress = adress
        self.__name = name
        self.__surname = surname
        
    def __str__(self):
        
        id_str = str(self.__id)
        
        print(f"Detailed client data:\n\
              id: {id_str}\n\
              adress: {self.__adress}\n\
              name: {self.__name}\n\
              surname: {self.__surname}")
    
""" Defines a buisness client structure """

class BuisnessClient(Client):
    
    __organizationName: str
    __organizationIdentifier: int # cos ala NIP ;)
    
    @property
    def getId(self) -> int:
        return self.__id
    
    @property
    def getAdress(self) -> str:
        return self.__adress
    
    @property
    def getOrganizationName(self) -> str:
        return self.__organizationName
    
    @property
    def getOrganizationIdentifier(self) -> int:
        return self.__organizationIdentifier
    
    def __init__(self, id: int, adress: str, organizationName: str, organizationIdentifier: int):
         self.__id = id
         self.__adress = adress
         self.__organizationName = organizationName
         self.__organizationIdentifier = organizationIdentifier
    
    def __str__(self):
        
        id_str = str(self.__id)
        organizationIdentifier_str = str(self.__organizationIdentifier)
        
        print(f"Detailed client data:\n\
              id: {id_str}\n\
              adress: {self.__adress}\n\
              organization name: {self.__organizationName}\n\
              organization identifier: {organizationIdentifier_str}")
    
    
    
    
    
    