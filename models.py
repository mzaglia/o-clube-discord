from os import getenv

from sqlalchemy import BigInteger, Boolean, Column, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.sqltypes import Boolean, Date, DateTime

Base = declarative_base()

engine = create_engine(getenv("DATABASE_URL", "sqlite:///test.db"))

Session = sessionmaker(bind=engine)
session = Session()

class Warzone(Base):
    __tablename__ = "warzone"
    battletag = Column(String, primary_key=True)
    channel_id = Column(BigInteger, nullable=True)
    member_id = Column(BigInteger, nullable=False)
    track = Column(Boolean, nullable=False, default=False)
    last_match = Column(String, nullable=True)


class User(Base):
    __tablename__ = "user"
    member_id = Column(BigInteger, primary_key=True)
    guild_id = Column(BigInteger, primary_key=True)
    birthday = Column(Date, nullable=True)
    name = Column(String, nullable=False)


class BDay(Base):
    __tablename__ = "bday"
    guild_id = Column(BigInteger, primary_key=True)
    channel_id = Column(BigInteger, default=None)
    last_notify = Column(Date, nullable=True)

class Correios(Base):
    __tablename__ = "correios"
    guild_id = Column(BigInteger, primary_key=True)
    channel_id = Column(BigInteger, default=None)
    last_notify = Column(Date, nullable=True)

class Package(Base):
    __tablename__ = "package"
    id = Column(String, primary_key=True)
    guild_id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, nullable=False)
    tag = Column(String)
    latest_message_id = Column(BigInteger)
    last_update = Column(DateTime)


Base.metadata.create_all(engine)
