#!/usr/bin/python3

"""Island Perimeter """


def island_perimeter(grid):
    """
        Args:
            grid int[][]
        Return: int
    """
    perimeter = 0

    for x in range(len(grid)):
        for y in range(len(grid[x])):
            p1 = grid[x - 1][y] if x - 1 >= 0 else 0
            p2 = grid[x][y - 1] if y - 1 >= 0 else 0
            p3 = grid[x][y + 1] if y + 1 < len(grid[x]) else 0
            p4 = grid[x + 1][y] if x + 1 < len(grid) else 0
            if grid[x][y] == 1:
                if p1 == 0:
                    perimeter = perimeter + 1
                if p2 == 0:
                    perimeter = perimeter + 1
                if p3 == 0:
                    perimeter = perimeter + 1
                if p4 == 0:
                    perimeter = perimeter + 1
    return perimeter
