from http import server
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
import requests
import server_utils

app = FastAPI()

app.mount("/client/build", StaticFiles(directory="client/build"), name="static")

@app.get("/")
def root():
    return FileResponse("./client/build/index.html")


@app.get("/recipes")
def get_recipes(ingredient, dairyFree="", glutenFree=""):
    recipes = requests.get(f"https://recipes-goodness.herokuapp.com/recipes/{ingredient}").json()["results"]
    dairyFree = True if dairyFree == "true" else False
    glutenFree = True if dairyFree == "true" else False
    filtered_recipes = server_utils.filter_recipes(recipes, dairyFree, glutenFree)
    return {"recipes": filtered_recipes}


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
