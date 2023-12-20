#!/usr/bin/python3
"""
Singly_linked_list.py.

This module has two classes and zero functions.

Classes:
    Node:
        A class that defines a node of a singly linked list.

    SinglyLinkedList:
        A class representing a singly linked list.

Functions:
    This module has no functions.
"""


class Node:
    """
    A class that defines a node in a singly linked list.

    Attributes:
        data (int): A private instance attribute.
            The data stored in the new node.

        next_node (Node) : A private instance attribute.
            The next node in the linked list that the new node points to.

    Methods:
        __init__(self, data, next_node=None) :
            Initializes a new Node object with the given attributes.

        data(self) : @property
            Gets the property `data`.

        data(self, value) : @data.setter
            Sets the property `data`.

        next_node(self) : @property
            Gets the property `next_node`.

        next_node(self, value) : @next_node.setter
            Sets the property `next_node`.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new Node object with the given attributes.

        Args:
            data (int): A private instance attribute.
                The data stored in the new node.

            next_node (Node) : A private instance attribute.
                The next node in the linked list that the new node points to.
                Its default value = None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Gets the property `data`.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Sets the property `data`.

        Args:
            value (int) : A private instance attribute.
                The data stored in the new node.

        Raises:
            TypeError : Exception
                If `value` is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """
        Gets the property `next_node`.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Sets the property `next_node`.

        Args:
            value (Node) : A private instance attribute.
                The next node in the linked list that the current node
                points to.

        Raises:
            TypeError : Exception
                If `value` is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """
    A class representing a singly linked list.

    Attributes:
        head (Node) : Private instance attribute.
            The head of the singly linked list.

    Methods:
        __init__(self) :
            Initializes a new singly linked list with the given attribute.

        sorted_insert(self, value) :
            Inserts a new `Node` into the singly liked list.
    """

    def __init__(self):
        """
        Initializes a new singly linked list with the given attribute.

        Args:
            head (Node) : Private instance attribute.
                The head of the singly linked list.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new Node into the singly liked list.

        The new Node is inserted in the correct sorted position in the
        list (increasing order).

        Args:
            value (Node) :
                The new node to be inserted in the singly linked list.
        """
        new_node = Node(value)

        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node
        elif new_node.data <= self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current_node = self.__head
            while (current_node.next_node is not None and
                   new_node.data > current_node.next_node.data):
                current_node = current_node.next_node
            new_node.next_node = current_node.next_node
            current_node.next_node = new_node

    def __str__(self):
        """
        A string representation of the singly linked list.

        The string contains the data in each node of the singly linked list.

        Returns:
            list_string (string) :
                The entire list of data in the list, printed one node per
                line.
        """
        list_string = ""

        # Get the data in each node, starting from the head, and store it in
        # the nodes_data list.
        nodes_data = []

        current_node = self.__head
        while current_node is not None:
            nodes_data.append(current_node.data)
            current_node = current_node.next_node

        # Join each value in the node_data list together in a string.
        # Each data stands singly on its line.
        for index in range(len(nodes_data)):
            if index == len(nodes_data) - 1:
                list_string += str(nodes_data[index])
            else:
                list_string += str(nodes_data[index]) + "\n"

        return list_string
