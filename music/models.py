from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from database import Base
from database import intpk
from database import str256

# class Album(Base):
#     __tablename__ = "albums"


class Author(Base):
    __tablename__ = "authors"

    id: Mapped[intpk]
    name: Mapped[str256]
    surname: Mapped[str256]

    songs: Mapped[list["Song"]] = relationship(back_populates="author")
    features: Mapped[list["Song"]] = relationship(
        back_populates="co_authors", secondary="featured_authors"
    )


class Song(Base):
    __tablename__ = "songs"

    id: Mapped[intpk]
    title: Mapped[str256]
    duration: Mapped[float]
    author_id: Mapped[int] = mapped_column(
        ForeignKey("authors.id", ondelete="SET NULL")
    )

    author: Mapped["Author"] = relationship(back_populates="songs")
    co_authors: Mapped[list["Author"]] = relationship(
        back_populates="features", secondary="featured_authors"
    )


class Featured(Base):
    __tablename__ = "featured_authors"

    song_id: Mapped[int] = mapped_column(
        ForeignKey("songs.id", ondelete="SET NULL"), primary_key=True
    )
    authors_id: Mapped[int] = mapped_column(
        ForeignKey("authors.id", ondelete="SET NULL"), primary_key=True
    )
