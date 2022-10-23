from pydantic import BaseModel
from typing import Union, List
from DB.db_manager import db_manager


class RecipeData(BaseModel):
    title: Union[str, None] = None
    thumbnail: Union[str, None] = None
    href: Union[str, None] = None
    ingredients: Union[List[str], None] = None


def _is_recipe_dairy_free(recipe: RecipeData):
    recipe_ingrediants = recipe.ingredients
    dairy_ingrediants = db_manager.get_dairy_ingrediants()
    result = any(map(lambda ingrediant: ingrediant in dairy_ingrediants, recipe_ingrediants))
    return result != True


def _is_recipe_gluten_free(recipe: RecipeData):
    recipe_ingrediants = recipe.ingredients
    gluten_ingrdiants = db_manager.get_gluten_ingrediants()
    result = any(map(lambda ingrediant: ingrediant in gluten_ingrdiants, recipe_ingrediants))
    return result != True


def filter_recipes(recipes, dairyFree, glutenFree):
    recipesData = []
    for recipe in recipes:
        recipesData.append(RecipeData(**recipe))

    if dairyFree:
        recipesData = filter(lambda recipe: _is_recipe_dairy_free(recipe), recipesData)

    if  glutenFree:
        recipesData = filter(lambda recipe: _is_recipe_gluten_free(recipe), recipesData)
   
    return list(recipesData)