#!/usr/bin/python3
"""writing a method that determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    """Returns True if all boxes can be opened, else return False
    Args
    Boxes - list of lists"""

    """create a set to keep track of the keys we have
    we have the key for box [0]"""
    keys = set([0])
    """initialize a set to track the boxes we've visited"""
    visited = set()
    """start a queue with the first box"""
    queue = [0]
    """iterate through the queue till it's empty"""
    while queue:
        """pop the first box from the queue"""
        current = queue.pop(0)
        """mark the first box as visited"""
        visited.add(current)
        """iterate through keys in the first box"""
        for key in boxes[current]:
            """if it's a key we don't have and it corresponds to a box"""
            if key not in keys and key < len(boxes):
                """add the key to out collection"""
                keys.add(key)
                """add the box to the queue so that you can explore
                it later"""
                queue.append(key)

    """return true if all boxes are visited, false otherwise"""
    return len(visited) == len(boxes)
