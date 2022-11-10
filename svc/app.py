import requests
from ..config import URL
from fastapi import FastAPI



app = FastAPI()

@app.get('/')
def root():
    return requests.get(f'{URL}catalog/card-names').text