from fastapi import FastAPI

def get_app():
    app = FastAPI()

    return app


app = get_app()
