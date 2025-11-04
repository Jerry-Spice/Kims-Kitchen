# Moms Recipes

This is meant to be a website to organize and access my moms recipes. She has lots of recipe cards and it's hard to keep track of them all and to find the ones she wants to use. This system will make it easier to access them.

## Design Considerations

Let's take a look at what information is stored on a recipe card. 
A recipe card has the following information:
 - Recipe Name
 - Ingredient List
 - Short Description
 - Instructions
 - Tags (Salad, Entree, Christmas, etc.)
 - Prep Time
 - Cooking Time
 - Serves X people
 - Calorie Count

## Display Format

Ideally I want the recipe card information displayed like this:

+-------------------------------------------------+
|                                                 |
| <tags>                                          |
| Cake                                            |
| <Description>                                   |
|                                                 |
+-------------------------------------------------+
|                                                 |
| Ingredients:                                    |
|  - Milk                                         |
|  - Eggs                                         |
|  - Flour                                        |
|  - Sugar                                        |
|  - Cake Mix                                     |
|                                                 |
+-------------------------------------------------+
|                                                 |
| Instructions:                                   |
|  1. Mix Ingredients                             |
|  2. Preheat Oven                                |
|  3. Bake                                        |
|  4. Cool                                        |
|                                                 |
+-------------------------------------------------+

## Project Elements

There's a few things that need to be done to build a MVP
1. Database
    - Storing Recipes
    - Recalling Recipes
    - Storing User Log In Info
    - Verifying Log In Info
2. Backend
    - Reading Database Entries
    - Verify Log In Info
    - Keeping Track of Specific User Instances
    - 
3. Frontend

## Design Ideas

Color Pallate: https://coolors.co/c7e8f3-bf9aca-8e4162-41393e-eda2c0