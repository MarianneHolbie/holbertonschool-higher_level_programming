#!/usr/bin/python3
""" This module contain 2 class : Node & SinglyLinkedList"""


class Node:
    """
    Class that defines a node of a singly linked list

    Attributes
    ----------
    __data : integer
        value of the node

    __next_node : None or Node
        pointer to next node

    """

    def __init__(self, data, next_node=None):
        """ constructor method """
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ Getter method for data"""
        return (self.__data)

    @data.setter
    def data(self, value):
        """ Setter method for data"""
        if type(value) != int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """ Getter method for next_node"""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """ Setter method for next_node"""
        if value or not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    Class that defines a singly linked list

    Attributes
    ----------
    __head : integer
        head of linked list

    """

    def __init__(self):
        """ constructor method : initialize linked list """
        self.__head = []

    def __str__(self):
        string = ""
        flagEnd = False
        for i in self.__head:
            if flagEnd is True:
                string += "\n"
            string += f"{i}"
            flagEnd = True
        return string

    def sorted_insert(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__head.append(value)
        self.__head.sort()
