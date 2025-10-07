def transpose(mat: list[list[float | int ]]) -> list[list]:
    if not mat:
        return []
    
    row_length = len(mat[0])
    for i, row in enumerate(mat):
        if len(row) != row_length:
            raise ValueError(f"Строка {i} имеет длину {len(row)}, ожидалось {row_length}")
        
    return [[row[j] for row in mat] for j in range(len(mat[0]))]


def row_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    
    first_row_len = len(mat[0])
    for row in mat:
        if len(row) != first_row_len:
            raise ValueError("Матрица должна быть прямоугольной")

    sums = []
    for row in mat:
        sums.append(sum(row))
    return sums


def col_sums(mat: list[list[float | int]]) -> list[float]:
    if not mat:
        return []
    
    first_row_len = len(mat[0])
    for row in mat:
        if len(row) != first_row_len:
            raise ValueError("Матрица должна быть прямоугольной")
        
    num_cols = len(mat[0])
    sums = []
        
    for j in range(num_cols):
        column_sum = 0
        for row in mat:
            column_sum += row[j]
        sums.append(column_sum)
        
    return sums


print('transpose',
    transpose([[1, 2, 3]]),
    transpose([[1], [2], [3]]),
    transpose([[1, 2], [3, 4]]),
    transpose([]),
    transpose([[1, 2], [3]]),
)

print('row_sums',
    row_sums([[1, 2, 3], [4, 5, 6]]),
    row_sums([[-1, 1], [10, -10]]),
    row_sums([[0, 0], [0, 0]]),
    row_sums([[1, 2], [3]]),
)

print('col_sums',
    col_sums([[1, 2, 3], [4, 5, 6]]),
    col_sums([[-1, 1], [10, -10]]),
    col_sums([[0, 0], [0, 0]]),
    col_sums([[1, 2], [3]]),
)