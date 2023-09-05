import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    nickuser = Column(String(40), unique=True)
    userID = Column(Integer, primary_key=True)
    first_name = Column(String(30), nullable=False)
    last_name = Column(String(30), nullable=False)
    email = Column(String(40), nullable=False, unique=True)
    post = relationship('post')


class Media(Base):
    __tablename__ = 'media'
    mediaID = Column(Integer, primary_key=True)
    url = Column(String(250))
    postID = relationship('Post')

class Comment (Base):
    __tablename__ = 'comments'
    commentID = Column(Integer, primary_key=True)
    comment_text = Column(String(500), nullable=False)
    userId = relationship('User')
    postid= Column(Integer, primary_key=True)

class Post(Base):
    __tablename__ = 'post'
    mediaId = Column(Integer, ForeignKey('media.mediaID'))
    commentID = Column (Integer, ForeignKey('comment. commentID'))              
    postId = Column(Integer, primary_key=True)
    comment = relationship('commment')
    media = relationship('media')


    # userID = relationship('User')

class Follower(Base):
    __tablename__ = 'follower'
    followerID = Column(Integer, primary_key=True)
    userID = relationship('User')

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
