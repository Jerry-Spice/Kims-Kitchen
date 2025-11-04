from Recipe import Recipe
import json

class Cookbook(object):
    def __init__(self, name, recipe_file):
        self.name = name
        self.recipe_file = recipe_file
        self.recipes = []

        self.load_recipes()
    
    def load_recipes(self):
        with open(self.recipe_file, "r") as f:
            data = f.read()
            f.close()
        recipes = json.loads(data)["recipes"]
        for recipe in recipes:
            self.recipes.append(Recipe(recipe["name"], recipe["ingredients"],recipe["description"],recipe["instructions"],recipe["tags"],recipe["prep time"],recipe["cooking time"],recipe["serves"],recipe["calories"]))
    
    def __str__(self):
        message = f"** {self.name} **\n"
        for recipe in self.recipes:
            message += str(recipe) + "\n"
        return message

#### EXAMPLE
# cookbook1 = Cookbook("Classic Cooks", "./cookbooks/Classic.json")
# print(cookbook1)
