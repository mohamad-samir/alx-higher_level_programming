#!/usr/bin/python3
"""
This program define a Base class for other classes
"""
import csv
import json
import os
import turtle


class Base:
    """
    Base class for future inheritance to Shapes
    """
    # Public Class Attributes
    __nb_objects = 0

    # Constructor
    def __init__(self, id=None):
        """
        Constructor of base Class with id.
        Args:
          - id: int (optional)
        """
        if (id is not None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # Class Methods
    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of `list_objs` to a file.

        Args:
            list_objs (list of objs): List of instances.
        """
        filename = f"{cls.__name__}.json"
        with open(filename, mode="w", encoding="utf-8") as json_file:
            if not list_objs:
                json_file.write(cls.to_json_string([]))
            else:
                dict_objs = [obj.to_dictionary() for obj in list_objs]
                json_file.write(cls.to_json_string(dict_objs))

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.

        Args:
            **dictionary: A double pointer to a dictionary.

        Returns:
            An instance of the class with attributes
            set according to `dictionary`.
        """
        # Create a dummy instance with default values for mandatory attributes
        dummy = cls(1, 1, 1, 1)

        # Use update to set the actual values
        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Read a JSON file and create instances from the dicts
        Args:
          - cls: New instance (Square or Rectangle)
        """

        filename = cls.__name__ + ".json"
        json_string = ""
        result = []

        if os.path.exists('./{:s}'.format(filename)):
            with open(filename, mode="r", encoding="utf-8") as _file:
                json_string = _file.read()

            list_of_instances = cls.from_json_string(json_string)
            for instance in list_of_instances:
                result.append(cls.create(**instance))

        return (result)

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances from a file.

        The filename must be: <Class name>.json.
        If the file doesn’t exist, return an empty list.
        Otherwise, return a list of instances.

        Returns:
            list of instances: The type of these instances depends on cls.
        """
        filename = cls.__name__ + ".json"

        if not os.path.exists(filename):
            return []

        with open(filename, "r") as file:
            list_dicts = cls.from_json_string(file.read())

        return [cls.create(**dict_) for dict_ in list_dicts]

    @classmethod
    def load_from_file_csv(cls):
        """
        Reads a CSV file and creates instances from the dictionaries.
        The CSV file name should be the same as the class name.
        """

        # create the filename from the class name
        file_name = cls.__name__ + ".csv"

        # this list will store the instances created from the CSV data
        instances = []

        # check if the file exists
        if os.path.exists(file_name):

            # open the file
            with open(file_name, "r", encoding="utf-8") as csv_file:

                # create a CSV reader
                reader = csv.reader(csv_file)

                # determine the attributes based on the class name
                attributes = ["id", "width", "height", "x", "y"]\
                    if cls.__name__ == "Rectangle"\
                    else ["id", "size", "x", "y"]

                # for each row in the CSV data
                for row in reader:

                    # create a dictionary from the row data
                    instance_data = {key: int(value)
                                     for key, value in zip(attributes, row)}

                    # create instance from dictionary and add it to the list
                    instances.append(cls.create(**instance_data))

        # return the list of instances
        return instances

    # Static Methods
    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Return the JSON representation of a list of dictionaries
        Args:
          - list_dictionaries: list[dict]
        """
        if (list_dictionaries is None or len(list_dictionaries) == 0):
            return ("[]")

        return (json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON to a python type
        Args:
          - json_string: str (that contains list[dict])
        """

        if ((json_string is None) or (len(json_string) == 0)):
            return []

        return (json.loads(json_string))

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Takes all instances based with the class Base
        and draws it.
        Args:
          - list_rectangles: Rectangles[]
          - list_squares: Squares[]
        """
        turtle.color('purple', 'lightblue')
        turtle.speed(4)
        turtle.shape('turtle')

        if all(inst.__class__.__name__ == 'Rectangle'
               for inst in list_rectangles):
            for rectangle in list_rectangles:
                turtle.goto(rectangle.x, rectangle.y)
                for _ in range(4):
                    turtle.pendown()
                    turtle.fd(rectangle.width)
                    turtle.rt(90)
                    turtle.fd(rectangle.height)
                    turtle.penup()

        if all(inst.__class__.__name__ == 'Square'
               for inst in list_squares):
            for square in list_squares:
                turtle.goto(square.x, square.y)
                for _ in range(4):
                    turtle.pendown()
                    turtle.fd(square.size)
                    turtle.rt(90)
                    turtle.penup()

        turtle.done()
