import requests
from .config import URL
from fastapi import FastAPI



app = FastAPI()

@app.get('/')
def root(name):
    r = requests.get(f'{URL}cards/random?q=is%3Acommander&cc_key=').text
    return r
