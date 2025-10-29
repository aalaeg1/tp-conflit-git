from fastapi import FastAPI

# Création de l'application FastAPI
app = FastAPI()

# Route principale
@app.get("/")
def read_root():
    return {"message": "Hello World"}

# Route avec paramètre
@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello {name}!"}
