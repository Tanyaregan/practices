# First step: find the center of the matrix where the rabbit starts off


def find_matrix_center(matrix):
    """Find the middle coordinates [index of row, column] of the matrix."""

    # First we'll find out how big our matrix is

    number_of_rows = len(matrix)
    number_of_columns = len(matrix[0])

    middle_coords = []

    # If the matrix has an even number of rows, we'll need to find
    # the two numbers closest to center and pick the larger.

    if number_of_rows % 2 == 0:

        middle_row_1 = (number_of_rows / 2) - 1
        middle_column_1 = matrix[middle_row_1][(number_of_columns / 2) - 1]

        center_1 = matrix[middle_row_1][middle_column_1]

        middle_row_2 = number_of_rows / 2
        middle_column_2 = matrix[middle_row][(number_of_columns / 2)]

        center_2 = matrix[middle_row_2][middle_column_2]

        if center_1 > center_2:
            middle_coords.append(middle_row_1)
            middle_coords.append(middle_column_1)
        else:
            middle_coords.append(middle_row_2)
            middle_coords.append(middle_column_2)

    # otherwise we can just divide the rows and columns to find the exact middle

    else:
        middle_row = number_of_rows / 2
        middle_column = matrix[middle_row][(number_of_columns / 2)]

        middle_coords.append(middle_row)
        middle_coords.append(middle_column)

    return middle_coords

# Now that we know where the rabbit starts, we can begin hopping around


def counting_carrots(matrix):
    """Starting with the center position, keep finding the highest surrounding number.
    Add each number to a running total until there are no more spots with numbers."""

    starting_position = find_matrix_center(matrix)
    row = starting_position[0]
    column = starting_position[1]

    current_num_carrots = matrix[row][column]

    # We need to find the highest number surrounding the rabbit's current position

        left_num_carrots = matrix[row][column - 1]
        right_num_carrots = matrix[row][column + 1]
        upper_num_carrots = matrix[row - 1][column]
        lower_num_carrots = matrix[row + 1][column]

# I ran out of time.  I'm sorry!

# I was going to find the highest of the 4 variables above, and then move the
# rabbit to that position.

# Then I would update the row and column coordinates to the new ones,
# add the number of carrots to the total,
# and keep on like that until there is no number > 0.

# Then return the total number of carrots





