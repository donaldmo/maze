matrix = []

def init_matrix():
    return 

def gen_matrix(width, height):
    matrix = []

    for j in range(height):
        row = []
        for i in range(width):
            row.append(i + j*width)
        matrix.append(row)

    return matrix

def parse_node(number):
    nums = []

    for i, digit in enumerate(str(number)):
        if i == 0 and len(str(number)) == 1:
            nums.append(0)
        nums.append(int(digit))

    return nums


def manhattan_distance(a, b, num_cols=20):
    row_a, col_a = divmod(a, num_cols)
    row_b, col_b = divmod(b, num_cols)
    distance = abs(row_b - row_a) + abs(col_b - col_a)

    return distance * 10


def heuristic_distance(point, goal):
    global matrix
    h_score = None

    point_row, point_col = get_indexes(point, matrix)
    goal_row, goal_col = get_indexes(goal, matrix)

    # check if they're on the same row
    same_row = True if point_row == goal_row else False

    if same_row:
        h_score = abs(point_col - goal_col)
    else:
        h_score = (abs(point_row - goal_row) + abs(point_col - goal_col))

    return h_score * 10

    
def are_diagonal(point1: int, point2: int) -> bool:
    x1, y1 = divmod(point1, 10)  # Assuming the maze is represented as a 10x10 grid
    x2, y2 = divmod(point2, 10)

    if abs(x2 - x1) != abs(y2 - y1):
        return 10

    return 14


def find_indices(matrix, value):
    for i, row in enumerate(matrix):
        if value in row:
            return i, row.index(value)


def get_indexes(node, matrix):
    index = None

    for i, mat_list in enumerate(matrix):
        for val in mat_list:
            if node == val:
                index = (i, mat_list.index(node))
                break

    return index


def create_node(neighbor_value, g_score, current_node, target_node):
    global matrix
    h_score = heuristic_distance(neighbor_value, target_node)

    node = {}
    node['Node'] = neighbor_value
    node['g'] = g_score
    node['h'] = h_score
    node['f'] = h_score + g_score

    return node

def get_neighbour(matrix, current_node, target_node):
    # current_node = 42, target_node = 46
    
    # width: 10, height: 20
    matrix_row = len(matrix[0])
    matrix_column = len(matrix)
    row_index, col_index = find_indices(matrix, current_node)
    
    # Declare indeces for all neighbours
    top_index = row_index - 1 if row_index > 0 else None
    bottom_index = row_index + 1 if row_index < len(matrix) -1 else None

    left_index = col_index - 1 if col_index > 0 else None
    right_index = col_index + 1 if col_index < len(matrix[0]) -1 else None

    neighbours = []
    
    # Index all neighbours
    if top_index is not None and col_index is not None:
        top_neigh = matrix[top_index][col_index]
        neighbours.append(create_node(top_neigh, 10, current_node, target_node))
    else:
        top_neigh = None

    if bottom_index is not None and col_index is not None:
        bottom_neigh = matrix[bottom_index][col_index]
        neighbours.append(create_node(bottom_neigh, 10, current_node, target_node))
    else:
        bottom_neigh = None

    if top_index is not None and right_index is not None:
        top_right_neigh = matrix[top_index][right_index]
        neighbours.append(create_node(top_right_neigh, 14, current_node, target_node))
    else:
        top_right_neigh = None

    if bottom_index is not None and right_index is not None:
        bottom_right_neigh = matrix[bottom_index][right_index]
        neighbours.append(create_node(bottom_right_neigh, 14, current_node, target_node))
    else:
        bottom_right_neigh = None

    if top_index is not None and left_index is not None:
        top_left_neigh = matrix[top_index][left_index]
        neighbours.append(create_node(top_left_neigh, 14, current_node, target_node))
    else:
        top_left_neigh = None

    if bottom_index is not None and left_index is not None:
        bottom_left_neigh = matrix[bottom_index][left_index]
        neighbours.append(create_node(bottom_left_neigh, 14, current_node, target_node))
    else:
        bottom_left_neigh = None

    if right_index is not None and row_index is not None:
        right_neigh = matrix[row_index][right_index]
        neighbours.append(create_node(right_neigh, 10, current_node, target_node))
    else:
        right_neigh = None

    if left_index is not None and row_index is not None:
        left_neigh = matrix[row_index][left_index]
        neighbours.append(create_node(left_neigh, 10, current_node, target_node))
    else:
        left_neigh = None

    neighbours = sorted(neighbours, key=lambda x: x['Node'])

    return neighbours


if __name__ == "__main__":
    
    matrix = gen_matrix(10, 20)
    
    for x in matrix:
        print(x)
    print()
    
    bricks = [0, 10, 20, 30, 40, 190, 34, 54, 1, 11, 19, 29, 9,
              44, 179, 189, 199, 188, 196, 197, 198]
    
    neighbours = get_neighbour(matrix, 42, 46)
    # print('neighbours: ', neighbours)
    for n in neighbours:
        print(n)


