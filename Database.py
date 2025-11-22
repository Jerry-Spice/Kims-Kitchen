import os
import random
from Cookbook import Cookbook
from Recipe import Recipe

class Database(object):
    def __init__(self, data_directory):
        self.data_directory = data_directory
        self.files = os.listdir(self.data_directory)
        # Fix the path in case we forget to add the final / for path operations
        if self.data_directory[-1] != '/':
            self.data_directory += '/'

    def getCookbook(self, name, file_extension=".json"):
        if os.path.exists(self.data_directory + name + file_extension):
            return Cookbook(name, self.data_directory + name + file_extension)
        else:
            return None

    def findRecipe(self, name, fuzzy=False):
        # let n be the number of files in a directory
        # let g be the number of recipes in a cookbook file
        # n < g typically
        # so n is more like a constant
        # O(n*g) -> O(g)
        matches = []
        for file in os.listdir(self.data_directory):
            cookbook = Cookbook(file, self.data_directory + file)
            for recipe in cookbook.recipes:
                if fuzzy:
                    if name.lower() in recipe.name.lower():
                        matches.append(recipe)
                else:
                    if name.lower() == recipe.name.lower():
                        matches.append(recipe)
        return matches

    def getAllRecipes(self, mode=1):
        matches = []
        files = os.listdir(self.data_directory)
        for i in range(0,len(files), mode):
            file = files[i]
            cookbook = Cookbook(file, self.data_directory + file)
            for recipe in cookbook.recipes:
                matches.append(recipe)
        return matches

    def getAllTags(self):
        recipes = self.getAllRecipes()
        tags = []
        tag_colors = []
        for recipe in recipes:
            for i in range(len(recipe.tags)):
                if recipe.tags[i] not in tags:
                    tags.append(recipe.tags[i])
                    tag_colors.append(recipe.tag_colors[i])
        return [tags, tag_colors]

    def findAllWithTag(self, target):
        recipes = self.getAllRecipes()
        results = []
        for recipe in recipes:
            for tag in recipe.tags:
                if tag.lower() == target.lower():
                    results.append(recipe)
                    break
        return results

    def __str__(self):
        message = "----- Recipe Database -----\n"
        for file in self.files:
            message += " - " + str(file) + "\n"
        return message[:-1]

#### EXAMPLE
# d1 = Database("./cookbooks")
# print(d1)
# cakes = d1.findRecipe("cake")
# for cake in cakes:
#     print(cake.name)
