# models.py
from dataclasses import dataclass
from typing import List

from flask_pymongo import PyMongo

mongo = PyMongo()


def init_app(app):
    mongo.init_app(app)
    print(mongo.db)


@dataclass
class UserPreferences:
    timezone: str

@dataclass
class User:
    username: str
    password: str
    roles: List[str]
    preferences: UserPreferences
    created_ts: float
    active: bool = True