import os
import random
from Cookbook import Cookbook
from Recipe import Recipe

class RecipeDatabase(object):
    def __init__(self, data_directory):
        self.data_directory = data_directory
        self.files = os.listdir(self.data_directory)
        # Fix the path in case we forget to add the final / for path operations
        if self.data_directory[-1] != '/':
            self.data_directory += '/'
    
    def getCookbook(self, name):
        if os.path.exists(self.data_directory + name):
            return Cookbook(self.data_directory + name)
        else:
            return None
    
    def findRecipe(self, name):
        # let n be the number of files in a directory
        # let g be the number of recipes in a cookbook file
        # n < g typically
        # so n is more like a constant
        # O(n*g) -> O(g)
        matches = []
        for file in os.listdir(self.data_directory):
            cookbook = Cookbook(file, self.data_directory + file)
            for recipe in cookbook.recipes:
                if name.lower() in recipe.name.lower():
                    matches.append(recipe)
        return matches
    
    def pickRandomRecipe(self):
        pass

    def __str__(self):
        message = "----- Recipe Database -----\n"
        for file in self.files:
            message += " - " + str(file) + "\n"
        return message[:-1]


#### EXAMPLE
# d1 = RecipeDatabase("./cookbooks")
# print(d1)
# print(d1.findRecipe("cake"))