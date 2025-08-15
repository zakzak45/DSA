#brute force 



grid =[
    [2,8,6],
    [3,4,9],
    [0,2,7]
]


def Search2d(Grid, target):
    

    for i in range(len(grid)):
        for j in  range(len(grid[0])):
            if grid[i][j] == target:
                return True
    return False





print(Search2d(grid, 14))