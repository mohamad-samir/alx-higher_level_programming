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
    def save_to_file_csv(cls, list_objs):
        """Serializes a list of objects to a CSV file.

        Args:
            list_objs (list): List of objects whose data is to be saved to CSV.
        """
        filename = f"{cls.__name__}.csv"
        with open(filename, mode="w", encoding="utf-8") as csv_file:
            if cls.__name__ == "Rectangle":
                columns = ["id", "width", "height", "x", "y"]
            else:
                columns = ["id", "size", "x", "y"]

            writer = csv.DictWriter(csv_file, columns)
            writer.writerows([obj.to_dictionary() for obj in list_objs])

    @classmethod
    def load_from_file_csv(cls):
        """
        Read a CSV file and create instances from the dicts
        Args:
          - cls: New instance (Square or Rectangle)
        """

        filename = cls.__name__ + ".csv"
        rectangle_props = ["id", "width", "height", "x", "y"]
        square_props = ["id", "size", "x", "y"]
        result = []

        if os.path.exists("./{:s}".format(filename)):
            with open(filename, mode="r", encoding="utf-8") as _file:
                data_csv = csv.reader(_file)
                if (cls.__name__ == "Rectangle"):
                    for data in data_csv:
                        new_dict = {}
                        for key, value in zip(rectangle_props, data):
                            new_dict[key] = int(value)
                        result.append(cls.create(**new_dict))
                elif (cls.__name__ == "Square"):
                    for data in data_csv:
                        new_dict = {}
                        for key, value in zip(square_props, data):
                            new_dict[key] = int(value)
                        result.append(cls.create(**new_dict))

        return (result)

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
