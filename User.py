from Cookbook import Cookbook
from Recipe import Recipe

class User(object):
    def __init__(self, name, cookbooks=[]):
        self.name = name
        self.cookbooks = cookbooks
    
    def __str__(self):
        message = f"{self.name}\nCookbooks:\n"
        for cookbook in self.cookbooks:
            message += " - " + cookbook.name + "\n"
        return message

#### EXAMPLE
# user1 = User("JerrySpice", [Cookbook("Classic Cooks", "./cookbooks/Classic.json"), Cookbook("Simple Cooks", "./cookbooks/Simple.json")])
# print(user1)