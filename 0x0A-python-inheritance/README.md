# Python - Inheritance

Note on task 101

The ``__dict__`` attribute is a dictionary that stores an object's writable attributes or instance variables.

Here are a few examples of Python objects that typically do not have a ``__dict__`` attribute:

Built-in types: Most built-in types, such as integers (int), floating-point numbers (float), and strings (str), do not have a `__dict__` attribute. These types are generally immutable, meaning their attributes cannot be modified.

Class objects: The class objects themselves do not have a `__dict__` attribute. However, instances of classes do have a `__dict__` attribute, which holds the instance's attributes.

Objects that use slots: Python allows defining classes with the `__slots__` attribute, which restricts the set of attributes that an instance can have. When a class uses slots, it does not have a `__dict__` attribute because the instance attributes are stored in a more memory-efficient manner. The use of `__slots__` is an optimization technique and is not necessary for most scenarios.

It's important to note that while these objects may not have a `__dict__` attribute, they still have attributes and methods that can be accessed or modified using other means. For example, built-in types have predefined attributes and methods that can be accessed directly or through other built-in functions.

Keep in mind that these examples represent typical cases, but there might be exceptions or custom implementations where certain objects have a modified behavior and include a `__dict__` attribute.
