#!/usr/bin/python3
"""
Lockboxes module
"""


def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.
    boxes is a list of lists; boxes[0] is unlocked and each box
    may contain keys (integers) to other boxes.
    Return True if all boxes can be opened, else False.
    """
    if not isinstance(boxes, list):
        return False
    n = len(boxes)
    if n == 0:
        return True

    opened = [False] * n
    opened[0] = True
    keys = list(boxes[0])

    while keys:
        key = keys.pop()
        if isinstance(key, int) and 0 <= key < n and not opened[key]:
            opened[key] = True
            keys.extend(boxes[key])

    return all(opened)
