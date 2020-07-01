""" Codewars - Multiplication table """


def multiplication_table(size):
    table = []
    row = []
    for a in range(1, size + 1, size):
        for b in range(1, size + 1, size):
            row.append(a * b)
        table.append(row)
    return table

    """
    table = []
    row = []
    for a in range(1, size + 1):
        for b in range(1, size + 1, size):
            row.append(a * b)
        table.append(row)
    return table
    """


print(multiplication_table(3))
# , [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

"""
    [
        [1,2],
        [2,4]
    ]
    [
        [1, 2, 3],
        [2, 4, 6],
        [3, 6, 9]
    ]
    [
        [1,2,3,4],
        [2,4,6,8],
        [3,6,9,12],
        [4,8,12,16]    
    ]
    [
        [1,2,3,4,5],
        [2,4,6,8,10],
        [3,6,9,12,15],
        [4,8,12,16,20],
        [5,10,15,20,25]
    ]
    


"""
