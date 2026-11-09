def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Your code here
    c = []
    for column in range(len(a[0])):
        b = []
        for row in range(len(a)):
            b.append(a[row][column])
        c.append(b)

    return c
    pass