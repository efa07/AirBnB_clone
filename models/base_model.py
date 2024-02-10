#!/usr/bin/python3

"""
This file defines the BaseModel class which will serve as the base of our model.
"""

from uuid import uuid4
from datetime import datetime

from datetime import datetime
from uuid import uuid4

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            self.id = kwargs.pop("__class__", str(uuid4()))  # Use pop to remove class key
            self.created_at = datetime.fromisoformat(kwargs.pop("created_at"))
            self.updated_at = datetime.fromisoformat(kwargs.pop("updated_at"))
            # Update instance attributes with remaining kwargs
            self.__dict__.update(kwargs)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        output_dict = {
            "__class__": self.__class__.__name__,
            **self.__dict__,
        }
        # Convert datetime objects to ISO format
        for key, value in output_dict.items():
            if isinstance(value, datetime):
                output_dict[key] = value.isoformat()
        return output_dict