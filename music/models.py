from sqlalchemy.orm import Mapped

from database import Base
from database import intpk
from database import str256

# class Album(Base):
#     __tablename__ = "albums"


class Song(Base):
    __tablename__ = "songs"

    id: Mapped[intpk]
    title: Mapped[str256]
    duration: Mapped[float]


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[intpk]
    name: Mapped[str256]
    surname: Mapped[str256]
