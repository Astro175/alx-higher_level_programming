#!/usr/bin/python3
"""Defines a module"""


class Node:
    """class that creates new nodes"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """returns a square data"""
        return self.__data

    @data.setter
    def data(self, value):
        """sets the value"""
        if not isinstance(value, int):
            raise TypeError("must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """returns the new_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """sets the value"""
        if (value is not None and not isinstance(value, Node)):
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """defines a linked list"""
    def __init__(self):
        """initialises head"""
        self.head = None

    def __str__(self):
        """initialise current"""
        current = self.head
        res = ""
        while current:
            res += str(current.data) + "\n"
            current = current.next_node
        return res[:-1]

    def sorted_insert(self, value):
        """
        sorts a list from smallest to largest
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        if value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
            return
        current = self.head
        while current.next_node and current.next_node.data < value:
            current = current.next_node
        new_node.next_node = current.next_node
        current.next_node = new_node
