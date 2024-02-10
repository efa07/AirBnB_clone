#!/usr/bin/python3

"""
This file defines the BaseModel class which will serve as the base of our model.
"""

from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Base class for all our classes"""

    def __init__(self, *args, **kwargs):
        """Deserialize and serialize a class"""

        # Initialize if nothing is passed
        if kwargs == {}:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()
            models.storage.new(self)
            return

        # Using keyword arguments (deserialize)
        if 'id' not in kwargs:
            kwargs['id'] = str(uuid4())
        self.id = kwargs['id']

        for key, val in kwargs.items():
            if key == "__class_":
                continue
            if key == "created_at":
                self.created_at = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
            elif key == "updated_at":
                self.updated_at = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
            else:
                setattr(self, key, val)

    def __str__(self):
        """Override the string representation of self"""
        fmt = "[{}] ({}) {}"
        return fmt.format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """Update the 'updated_at' variable and save the instance"""
        self.updated_at = datetime.utcnow()
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
        """Create an instance"""
        new_instance = cls(*args, **kwargs)
        return new_instance.id

    @classmethod
    def show(cls, instance_id):
        """Retrieve an instance"""
        return models.storage.find_by_id(cls.__name__, instance_id)

    @classmethod
    def destroy(cls, instance_id):
        """Delete an instance"""
        return models.storage.delete_by_id(cls.__name__, instance_id)

    @classmethod
    def update(cls, instance_id, *args):
        """Update an instance
        If args has one element and it's a dict,
        it updates by key-value.
        Otherwise, it updates by the first element being the key and the second element being the value."""
        if not len(args):
            print("** attribute name missing **")
            return
        if len(args) == 1 and isinstance(args[0], dict):
            args = args[0].items()
        else:
            args = [args[:2]]
        for arg in args:
            models.storage.update_one(cls.__name__, instance_id, *arg)