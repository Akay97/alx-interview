#!/usr/bin/python3
"""
This algorithm solves the lockbox problem
"""


def canUnlockAll(boxes):
    """
    check to open he lock box based on the key
    """
    if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    for i in range(1, len(boxes) - 1):
        boxes_checked = False
        for idx in range(len(boxes)):
            boxes_checked = i in boxes[idx] and i != idx
            if boxes_checked:
                break
        if boxes_checked is False:
            return boxes_checked
    return True
