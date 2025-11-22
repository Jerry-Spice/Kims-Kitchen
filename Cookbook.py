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
            self.recipes.append(Recipe(recipe["name"], recipe["ingredients"],recipe["description"],recipe["instructions"],recipe["tags"],recipe["tag_colors"],recipe["prep_time"],recipe["cook_time"],recipe["serves"],recipe["calories"]))

    def add_recipe(self, new_recipe):
        self.recipes.append(new_recipe)

    def remove_recipe(self, target_name):
        for recipe in self.recipes:
            if recipe.name == target_name:
                self.recipes.remove(recipe)
        self.save_recipes()
        self.load_recipes()

    def save_recipes(self):
        file = {"recipes": []}
        for recipe in self.recipes:
            file["recipes"].append(recipe.toJSON())
        f = open(self.recipe_file, "w+")
        f.write(json.dumps(file))
        f.close()

    def __str__(self):
        message = f"** {self.name} **\n"
        for recipe in self.recipes:
            message += str(recipe) + "\n"
        return message

#### EXAMPLE
# cookbook1 = Cookbook("Classic Cooks", "./cookbooks/Classic.json")
# cookbook1.save_recipes()
