#!/usr/bin/python3

"""
0- pascl tringle
"""


def pascal_triangle(n):
    """
    function for creation pascal triangle
    Args: 
        n: the height of the triangle
    Return: list of lists of int
    """
    prev = [1]
    res = []

    if n <= 0:
        return res

    for i in range(1, n + 1):
        prt1 = 0
        prt2 = 1
        cur_res = [1]
        cur = i
        while cur > 0:
            if i == 1:
                cur_res = [1]
                prev = cur_res
                break
            if i == 2:
                cur_res = [1, 1]
                prev = cur_res
                break
            if prt2 < len(prev):
                cur_res.append(prev[prt1] + prev[prt2])
            else:
                cur_res.append(1)
                break
            prt1 += 1
            prt2 += 1
            cur -= 1
        prev = cur_res
        res.append(cur_res)
    return res
