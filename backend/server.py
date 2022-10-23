from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
# from routers import pokemons_api, trainers_api
import uvicorn

app = FastAPI()
# app.include_router(module.router)

app.mount("/client/build", StaticFiles(directory="client/build"), name="static")

@app.get("/")
def root():
    return FileResponse("./client/build/index.html")


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8000, reload=True)
