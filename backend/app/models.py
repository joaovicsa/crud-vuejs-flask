# models.py
from dataclasses import dataclass
from typing import List

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