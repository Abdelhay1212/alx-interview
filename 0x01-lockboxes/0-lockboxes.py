#!/usr/bin/python3
''' Lockboxes '''


def canUnlockAll(boxes):
    ''' can unlock all '''
    def dfs(box_index, visited):
        visited.add(box_index)
        for key in boxes[box_index]:
            if key < len(boxes) and key not in visited:
                dfs(key, visited)

    visited = set()
    dfs(0, visited)

    return len(visited) == len(boxes)
