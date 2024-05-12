from sqlalchemy import func
from sqlalchemy import select
from sqlalchemy.orm import joinedload
from sqlalchemy.orm import selectinload

from database import Base
from database import session_factory
from database import sync_engine
import models
import schemas


def create_tables():
    Base.metadata.create_all(sync_engine)


def drop_tables():
    Base.metadata.drop_all(sync_engine)


def add_song(song: schemas.SongCreate):
    with session_factory() as session:
        new_song = models.Song(**song.model_dump())
        session.add(new_song)
        session.commit()
        session.refresh(new_song)
    return new_song


def get_songs():
    with session_factory() as session:
        query = (
            select(
                models.Song,
            )
            .join(models.Song.author)
            .options(selectinload(models.Song.co_authors))
            .add_columns(func.reverse(models.Author.name).label("author_name"))
        )
        songs = session.execute(query)
        returned_songs = songs.all()
    return returned_songs


def get_songs2():
    with session_factory() as session:
        author_name_cte = select(
            func.reverse(models.Author.name).label("author_name")
        ).cte("author_name_cte")
        query = (
            select(models.Song, author_name_cte.c.author_name)
            .options(joinedload(models.Song.author))
            .options(selectinload(models.Song.co_authors))
        )
        songs = session.execute(query)
        returned_songs = songs.all()
    return returned_songs


def add_author(author: schemas.AuthorCreate):
    with session_factory() as session:
        new_author = models.Author(**author.model_dump())
        session.add(new_author)
        session.commit()
        session.refresh(new_author)
    return new_author


def get_authors():
    with session_factory() as session:
        query = (
            select(models.Author)
            .options(joinedload(models.Author.songs))
            .options(selectinload(models.Author.features))
            .order_by(models.Author.id)
        )
        authors = session.execute(query)
        returned_authors = authors.unique().scalars().all()
    return returned_authors


def add_feat(author_id: int, song_id: int):
    with session_factory() as session:
        song = (
            session.query(models.Song)
            .options(joinedload(models.Song.co_authors))
            .filter(models.Song.id == song_id)
            .first()
        )
        author = session.get(models.Author, author_id)
        song.co_authors.append(author)
        session.commit()
        session.refresh(song)
    return song
