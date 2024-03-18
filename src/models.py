import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Users(Base):
     __tablename__ = 'user'
     id = Column(Integer, primary_key=True)
     name = Column(String(30), nullable=False)
     last_name = Column(String(30), nullable=False)
     email = Column(String(50), nullable=False)
     password = Column(String(50), nullable=False)

class Planet(Base):
     __tablename__ = 'planet'
     id = Column(Integer, primary_key=True)
     name = Column(String(50), nullable=False)

class Planets_Favs(Base):
     __tablename__ = 'planet_fav'
     id = Column(Integer, primary_key=True)
     user_id = Column(Integer, ForeignKey('user.id'))
     planet_id = Column(Integer, ForeignKey('planet.id'))
     planet = relationship(Planet)

class Characters(Base):
     __tablename__ = 'character'
     id = Column(Integer, primary_key=True)
     name = Column(String(130), nullable = False)
     info = Column(String(130), nullable = False)

class Characters_Favs(Base):
     __tablename__ = 'character_fav'
     id = Column(Integer, primary_key=True)
     user_id = Column(Integer, ForeignKey('user.id'))
     user = relationship(Users)
     Character_id = Column(Integer, ForeignKey('character.id'))
     Character = relationship(Characters)


     def to_dict(self):
          return {}







     ## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
