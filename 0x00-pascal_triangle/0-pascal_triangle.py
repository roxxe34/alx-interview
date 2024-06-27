def pascal_triangle(n):
    if n <= 0:
        return []

    triangl = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangl[i-1][j-1] + triangl[i-1][j])
        row.append(1)
        triangl.append(row)

    return triangl