#!/usr/bin/python3
"""
    class Square inherit from Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        subclass of Rectangle

        Attribute
        ---------
            size : size of square
            x andy :position in space of square

        Method
        ---------
            __str__: print definition of square

            update : public, assigns attributes

            to_dictionary : return dictionary representation of a Rectangle

    """

    def __init__(self, size, x=0, y=0, id=None):
        """
            constructeur
        """
        super().__init__(height=size, width=size, x=x, y=y, id=id)

    @property
    def size(self):
        return (self.width)

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self.width = value
            self.height = value
        else:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')

    def __str__(self):
        """
            function that print definition of square
        """
        return ("[Square] ({}) {}/{} - {}".
                format(self.id, self.x, self.y,
                       self.width))

    def update(self, *args, **kwargs):
        """
            function that assigns argument to each attribute
        """
        if len(args) != 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.size = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
        else:
            if kwargs is not None:
                for key, value in kwargs.items():
                    if key == 'id':
                        self.id = value
                    if key == 'size':
                        self.size = value
                    if key == 'x':
                        self.x = value
                    if key == 'y':
                        self.y = value

    def to_dictionary(self):
        """
            construct dictionary representation of square
        """
        return (dict(id=self.id, size=self.size, x=self.x, y=self.y))
