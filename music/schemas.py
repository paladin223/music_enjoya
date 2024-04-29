from pydantic import BaseModel

from database import intpk
from database import str256


class AuthorBase(BaseModel):
    name: str256
    surname: str256


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: intpk


class SongBase(BaseModel):
    title: str256
    duration: float


class SongCreate(SongBase):
    pass


class Song(SongBase):
    id: intpk
