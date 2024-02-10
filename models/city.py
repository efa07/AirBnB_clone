#!/usr/bin/python3
"""
Defines City model and
inherits from BaseMode
"""


from models.base_model import BaseModel


class City(BaseModel):

    state_id: str = ''
    name: str = ''
