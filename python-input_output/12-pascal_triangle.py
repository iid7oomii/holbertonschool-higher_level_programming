def pascal_triangle(n):
    """
    return a list of integers representing pascal`s triangle
    """

    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        current_row = [1]

        for j in range(len(prev_row) - 1):

            new_number = prev_row[j] + prev_row[j + 1]
            current_row.append(new_number)

        current_row.append(1)

        triangle.append(current_row)

    return triangle
