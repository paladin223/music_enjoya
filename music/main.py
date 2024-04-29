# uvicorn main:app --reload
from fastapi import FastAPI

import crud
import schemas

app = FastAPI()


@app.get("/start/")
def refresh_db():
    crud.drop_tables()
    crud.create_tables()


@app.get("/songs/", response_model=list[schemas.Song])
def get_songs():
    songs = crud.get_songs()
    return songs


@app.post("/songs/", response_model=schemas.SongCreate)
def create_songs(song: schemas.SongCreate):
    songs = crud.add_song(song)
    return songs
