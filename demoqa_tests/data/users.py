import dataclasses
from datetime import date
import enum
from typing import List


class UserHobby(enum.Enum):
    Sports = 'Sports',
    Reading = 'Reading',
    Music = 'Music'


class UserGender(enum.Enum):
    Male = 'Male',
    Female = 'Female',
    Other = 'Other'


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: str
    date_of_birth: date
    subjects: List[str]
    hobby: str
    picture: str
    address: str
    state: str
    city: str
