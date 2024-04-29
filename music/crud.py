from sqlalchemy import select

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
        query = select(models.Song)
        songs = session.execute(query)
        returned_songs = songs.scalars().all()
        return returned_songs
