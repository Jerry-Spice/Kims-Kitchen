from flask import Flask, render_template, request, redirect, url_for

import random

from Recipe import Recipe
from Cookbook import Cookbook
from Database import Database

library = Database("./cookbooks")


app = Flask(__name__)

@app.route("/")
def index():
    recipePool = library.getAllRecipes()
    tagPool = library.getAllTags()

    shuffle = random.randint(0, len(tagPool[0]))
    for i in range(shuffle):
        index = random.randint(0, len(tagPool[0]) - 1)
        temp = tagPool[0][index]
        tagPool[0][index] = tagPool[0][i]
        tagPool[0][i] = temp
        temp = tagPool[1][index]
        tagPool[1][index] = tagPool[1][i]
        tagPool[1][i] = temp

    randomRecipes = []
    for i in range(6):
        if (len(recipePool) - 1) <= 0:
            break
        item = recipePool[random.randint(0, len(recipePool) - 1)]
        recipePool.remove(item)
        randomRecipes.append(item)

    return render_template("index.html", randomRecipes1=randomRecipes[0:3], randomRecipes2=randomRecipes[3:6], tagPool=tagPool)

@app.route("/search", methods=["POST"])
def recipe_search():
    data = request.form
    recipes = library.findRecipe(data["target_recipe"], fuzzy=True)
    print(recipes)
    if len(recipes) == 0:
        return render_template("recipe_failure.html", recipe_search=data["target_recipe"])
    elif len(recipes) == 1:
        return redirect(f"/recipes/{recipes[0].name}", code=302)
    else:
        jsonRecipes = []
        for recipe in recipes:
            jsonRecipes.append(recipe.toJSON())
        return render_template("recipe_options.html", recipes=jsonRecipes)

@app.route("/recipes/<recipe_name>")
def recipe_pages(recipe_name):
    recipes = library.findRecipe(recipe_name)
    if len(recipes) == 0:
        return render_template("recipe_failure.html")
    if len(recipes) > 1:
        return render_template("recipe_options.html")
    return render_template("recipe.html", recipe=recipes[0].toJSON())

@app.route("/tags/<tag_name>")
def tag_pages(tag_name):
    tags = library.findAllWithTag(tag_name)
    if len(tags) == 0:
        return render_template("recipe_failure.html", recipe_search=tag_name)
    elif len(tags) == 1:
        return redirect(f"/recipes/{tags[0].name}", code=302)
    else:
        jsonRecipes = []
        for tag in tags:
            jsonRecipes.append(tag.toJSON())
        return render_template("recipe_options.html", recipes=jsonRecipes)
    return render_template("recipe_options.html", recipes=jsonRecipes)

@app.route("/cookbooks/<cookbook_name>")
def show_cookbook(cookbook_name):
    recipes = library.getCookbook(cookbook_name).recipes

    jsonRecipes = []
    temp = []
    index = 0
    for recipe in recipes:
        if index % 3 == 0 and index != 0:
            jsonRecipes.append(temp)
            temp = []
        temp.append(recipe.toJSON())
        index += 1
    jsonRecipes.append(temp)
    return render_template("cookbook_manager.html", cookbook_name=cookbook_name, recipes=jsonRecipes)

@app.route("/cookbooks/<cookbook_name>/remove/<recipe_name>", methods=["POST"])
def remove_recipe_from_cookbook(cookbook_name, recipe_name):
    cookbook = library.getCookbook(cookbook_name)
    cookbook.remove_recipe(recipe_name)
    return redirect(f"/cookbooks/{cookbook_name}", code=302)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
