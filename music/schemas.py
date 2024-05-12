from pydantic import BaseModel

from database import intpk
from database import str256


class AuthorBase(BaseModel):
    name: str256
    surname: str256


class SongBase(BaseModel):
    author_id: int
    title: str256
    duration: float


class AuthorCreate(AuthorBase):
    pass


class SongCreate(SongBase):
    pass


class Song(SongBase):
    id: intpk
    author: AuthorBase
    co_authors: list["AuthorBase"] = []

    class Config:
        from_attributes = True


class SongAuthor(BaseModel):
    Song: SongBase
    author_name: str


class Author(AuthorBase):
    id: intpk
    songs: list["SongBase"] = []
    features: list["SongBase"] = []

    class Config:
        from_attributes = True
