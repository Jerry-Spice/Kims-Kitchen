class Recipe(object):
    def __init__(self, name, ingredients, description, instructions, tags, prep_time, cook_time, serves, calories):
          self.name = name                  # String
          self.ingredients = ingredients    # String
          self.description = description    # String
          self.instructions = instructions  # String
          self.tags = tags                  # String
          self.prep_time = prep_time        # Number
          self.cook_time = cook_time        # Number
          self.serves = serves              # Number
          self.calories = calories          # Number
    
    def __str__(self):
        return f"{self.name} [{self.tags.replace("\n",", ")}]\nPrep: {self.prep_time}\nCook: {self.cook_time}\nServes: {self.serves}\nCalories: {self.calories}\n\nDescription:\n{self.description}\n\nIngredients:\n{self.ingredients}\n\nInstructions:\n{self.instructions}"

#### EXAMPLE
## CAKE

# cake = Recipe("Cake", "Milk\nEggs\nCake Mix\netc.", "A cake! It's yummy.", "1. Mix\n2. Bake", "christmas, birthday, dessert", "20 minutes", "60 minutes", 8, 2000)

# print(cake)