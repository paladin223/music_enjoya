# uvicorn main:app --reload

from fastapi import FastAPI

import crud
import schemas

# from fastapi import Path


app = FastAPI()


@app.get("/start/")
def refresh_db():
    crud.drop_tables()
    crud.create_tables()


@app.get(
    "/songs/",
    response_model=list[schemas.SongAuthor],
)
def get_songs():
    songs = crud.get_songs()
    print(songs[0][0])
    return songs


@app.post("/song/", response_model=schemas.SongCreate)
def create_song(song: schemas.SongCreate):
    new_song = crud.add_song(song)
    return new_song


@app.get("/authors/", response_model=list[schemas.Author])
def get_authors():
    authors = crud.get_authors()
    return authors


@app.post("/author/", response_model=schemas.AuthorCreate)
def create_author(author: schemas.AuthorCreate):
    new_author = crud.add_author(author)
    return new_author


@app.post("/feat/", response_model=schemas.Song)
def create_feat(author_id: int, song_id: int):
    new_song_feat = crud.add_feat(author_id, song_id)
    return new_song_feat
