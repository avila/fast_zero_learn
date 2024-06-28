from fastapi import FastAPI

# inicia instancia do app
app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}
