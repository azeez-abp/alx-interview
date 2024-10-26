# Island Perimeter
- We are looking for perimeter;
- is that you have a square, perimeter is sum of lenght of lines tht surround it
- if we assume that the length of the line is 1 unit, the sum is 4
- in a grid that consist of many square, some lines are not part of the perimeter
```
-----------------
|_1_|_2_|_3_|_4_|   
|_5_|_6_|_7_|_8_| 

- In the grid above there 8 grids, the lines that contributed to perimeter are 
grid 1: 2 lines  ----
                 | 1

grid 2: 1 line -----
                 2
grid 3: 1 line  ----
                 3

grid 4: 2 lines -----
                 4  |

grid 5: 2 lines 
                |_5_

grid 6: 1 line _6_

grid 7: 1 line _7_

grid 8: 2 lines _8_|

```
so the total lines is 12
which is the island perimeter

## For this challege, just look for the grid that is part of the island  and count the number of lines its contributed to the perimeter


   

     
