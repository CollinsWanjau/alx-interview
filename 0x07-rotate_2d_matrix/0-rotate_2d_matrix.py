def rotate_2d_matrix(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix)
    # Transposing the Matrix
    for i in range(0, n):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
        # shifting the elements accodingly...
    for i in range(0, n):
        for j in range(0, n//2):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n-1-j]
            matrix[i][n-j-1] = temp
