#!/usr/bin/python3

"""
The BaseModel class is a class which will serve as the
base of our model
"""

from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """The base class of all class"""

    def __init__(self,*args, **kwargs):
        """serializeing and deserializing class"""

        if 'id' not in kwargs:
            kwargs['id'] = str(uuid4)
        self.id = kwargs['id']

        for Key, Val in kwargs.items():
            if Key == '__class__':
                continue
        if "created_at" in kwargs:
            self.created_at = datetime.now().isoformat()
        if "updated_at" in kwargs:
            self.updated_at = datetime.now().isoformat()

        def __str__(self):
            """string represention on self"""

            str_r = "[{}] ({}) {}"
            return str_r.format(type(self).__name__,
                    self.id,
                    self.__dict__)

        def save(self):
            """update the variable that updated"""

            self.updated_at = datetime.utcnow().isoformat()
            models.storage.save()

        def to_dict(self):
            """Returns a dictionary representation of self"""
    
        temp = {**self.__dict__}
        temp['__class__'] = type(self).__name__
        temp['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        temp['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return temp
