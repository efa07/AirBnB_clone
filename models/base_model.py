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

            self.updated_at = datetime.utcnow().isoformat
            models.storage.save()

        def to_dict(self):
            """Returns a dictionary representation of self"""
    
        temp = {**self.__dict__}
        temp['__class__'] = type(self).__name__
        temp['created_at'] = self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        temp['updated_at'] = self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f')
        return temp

    @classmethod
    def all(cls):
        """Retrieve all current instances of cls"""
        return models.storage.find_all(cls.__name__)

    @classmethod
    def count(cls):
        """Get the number of all current instances of cls"""
        return len(models.storage.find_all(cls.__name__))

    @classmethod
    def create(cls, *args, **kwargs):
        """Creates an Instance"""
        new = cls(*args, **kwargs)
        return new.id

    @classmethod
    def show(cls, instance_id):
        """Retrieve an instance"""
        return models.storage.find_by_id(
            cls.__name__,
            instance_id
        )

    @classmethod
    def destroy(cls, instance_id):
        """Deletes an instance"""
        return models.storage.delete_by_id(
            cls.__name__,
            instance_id
        )

    @classmethod
    def update(cls, instance_id, *args):
        """Updates an instance
        if args has one elem and its a dict:
        it updates by key value
        else:
        updates by first being key and second being value"""
        if not len(args):
            print("** attribute name missing **")
            return
        if len(args) == 1 and isinstance(args[0], dict):
            args = args[0].items()
        else:
            args = [args[:2]]
        for arg in args:
            models.storage.update_one(
                cls.__name__,
                instance_id,
                *arg
            )
