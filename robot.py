import turtle


matrix = []
direction = 1


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

def create_node(neighbor_value, g_score, current_node, target_node):
    global matrix
    h_score = heuristic_distance(neighbor_value, target_node)

    node = {}
    node['Node'] = neighbor_value
    node['g'] = g_score
    node['h'] = h_score
    node['f'] = h_score + g_score

    return node

def get_neighbour(matrix, bricks, closed_list, current_node, target_node):
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
    top_neigh = None
    bottom_neigh = None

    top_right_neigh = None
    bottom_right_neigh = None
    top_left_neigh = None

    bottom_left_neigh = None
    right_neigh = None
    left_neigh = None
    
    # Index all neighbours
    if top_index is not None and col_index is not None:
        top_neigh = matrix[top_index][col_index]
        if top_neigh not in bricks and top_neigh not in closed_list:
            neighbours.append(create_node(top_neigh, 10, current_node, target_node))

    if bottom_index is not None and col_index is not None:
        bottom_neigh = matrix[bottom_index][col_index]
        if bottom_neigh not in bricks and bottom_neigh not in closed_list:
            neighbours.append(create_node(bottom_neigh, 10, current_node, target_node))

    if top_index is not None and right_index is not None:
        top_right_neigh = matrix[top_index][right_index]
        if top_right_neigh not in bricks and top_right_neigh not in closed_list:
            neighbours.append(create_node(top_right_neigh, 14, current_node, target_node))

    if bottom_index is not None and right_index is not None:
        bottom_right_neigh = matrix[bottom_index][right_index]
        if bottom_right_neigh not in bricks and bottom_right_neigh not in closed_list:
            neighbours.append(create_node(bottom_right_neigh, 14, current_node, target_node))

    if top_index is not None and left_index is not None:
        top_left_neigh = matrix[top_index][left_index]
        if top_left_neigh not in bricks and top_left_neigh not in closed_list:
            neighbours.append(create_node(top_left_neigh, 14, current_node, target_node))

    if bottom_index is not None and left_index is not None:
        bottom_left_neigh = matrix[bottom_index][left_index]
        if bottom_left_neigh not in bricks and bottom_left_neigh not in closed_list:
            neighbours.append(create_node(bottom_left_neigh, 14, current_node, target_node))

    if right_index is not None and row_index is not None:
        right_neigh = matrix[row_index][right_index]
        if right_neigh not in bricks and right_neigh not in closed_list:
            neighbours.append(create_node(right_neigh, 10, current_node, target_node))

    if left_index is not None and row_index is not None:
        left_neigh = matrix[row_index][left_index]
        if left_neigh not in bricks and left_neigh not in closed_list:
            neighbours.append(create_node(left_neigh, 10, current_node, target_node))

    neighbours = sorted(neighbours, key=lambda x: x['Node'])

    return neighbours


def parse_node(number):
    nums = []

    for i, digit in enumerate(str(number)):
        if i == 0 and len(str(number)) == 1:
            nums.append(0)
        nums.append(int(digit))

    return nums


def manhattan_distance(point1, point2):
    x1, y1 = divmod(point1, 20)  # Assuming the maze is represented as a 10x10 grid
    x2, y2 = divmod(point2, 10)
    s = abs(x2 - x1) + abs(y2 - y1)
    return s * 10


def are_diagonal(point1: int, point2: int) -> bool:
    """
    Check if two points are diagonal to each other in a 2D grid.

    Explanation:
    Two points (x1, y1) and (x2, y2) are considered diagonal if and only if
    the absolute differences between their x-coordinates and y-coordinates are equal.
    In other words, |x2 - x1| must be equal to |y2 - y1|.

    Parameters:
    - point1 (int): The first point in the form of a single integer representing its position in a 2D grid.
    - point2 (int): The second point in the form of a single integer representing its position in a 2D grid.

    Returns:
    - bool: True if the points are diagonal, False otherwise.
    """
    x1, y1 = divmod(point1, 10)  # Assuming the maze is represented as a 10x10 grid
    x2, y2 = divmod(point2, 10)

    if abs(x2 - x1) != abs(y2 - y1):
        return 10

    return 14


def draw_maze(x, y, square_size=20):
    
    draw_filled_square(square_size, x, y)


# Continue with the rest of your turtle program...
def init_turtle(coordinates_matrix, position_index):
    turtle_robot = turtle.Turtle()
    x, y = get_coordinates(position_index, coordinates_matrix)
    
    turtle_robot.shape('turtle')
    turtle_robot.setheading(90)
    turtle_robot.penup()

    turtle_robot.goto(x, y)
    turtle_robot.pendown()

    return turtle_robot


def screen_turtle():
    # Set up the turtle screen
    screen = turtle.Screen()
    screen.setup(width=480, height=768)

    # Clear the screen and reset the background
    screen.clear()
    screen.bgcolor("white")  # Change the background color if needed

    return screen


def draw_constraint(width, height):
    # Draw a box around the turtle screen
    # init_turtle => goto(x-10, y-5)

    constraint_turtle = turtle.Turtle()
    constraint_turtle.hideturtle()
    constraint_turtle.penup()
    constraint_turtle.setheading(90)
    constraint_turtle.forward(height-5)  # offset with -5 to accomodate the turtle
    constraint_turtle.right(90)
    constraint_turtle.forward(width-10)  # offset with +10 to accomodate the turtle
    constraint_turtle.right(90)
    constraint_turtle.pendown()
    constraint_turtle.pencolor('red')

    for _ in range(2):
        constraint_turtle.forward(height * 2)  # Width of the box
        constraint_turtle.right(90)
        constraint_turtle.forward(width * 2)  # Height of the box
        constraint_turtle.right(90)

# Function to draw a filled square at a specified location


def draw_maze(coordinates_matrix, target_node, square_size):
    counter = 0
    for coords in coordinates_matrix:
        for x, y in coords:
            if counter in bricks:
                draw_filled_square(square_size, x, y)

            if counter == target_node:
                draw_filled_square(square_size, x, y, color='blue')
            
            counter += 1


def draw_filled_square(side_length, x, y, color=None):
    color = 'green' if not color else color

    # Create a turtle object
    my_turtle = turtle.Turtle()
    my_turtle.hideturtle()

    my_turtle.penup()  # Lift the pen to move without drawing
    my_turtle.goto(x-10, y-5)  # offset by 10 and 5 to accomodate the turtle to be on the center of each block
    my_turtle.pendown()  # Lower the pen to start drawing
 
    my_turtle.fillcolor(color)  # Set the fill color
    my_turtle.pencolor('red')  # Set the pen color
    my_turtle.speed("fastest")  # Increase the drawing speed

    my_turtle.begin_fill()  # Begin filling the shape

    for _ in range(4):
        my_turtle.forward(side_length)
        my_turtle.left(90)

    my_turtle.end_fill()    # End filling the shape


def gen_matrix_tuple(width, height):
    rows = 10
    columns = 20
    step = 20

    coords = []
    row_range = 200
    column_range = -100

    for _ in range(columns):
        row_range -= step
        column_range = -100

        corr = []
        for _ in range(rows):
            corr.append((column_range, row_range))
            column_range += 20

        coords.append(corr)

    return coords


def gen_matrix(width, height):
    matrix = []

    for j in range(height):
        row = []
        for i in range(width):
            row.append(i + j*width)
        matrix.append(row)

    return matrix


def get_node_position(coordinates: tuple, coordinates_matrix: list) -> int:
    counter = 0

    for col in coordinates_matrix:
        for _, row in enumerate(col):
            if coordinates == row:
                return counter
            counter += 1

    return None


def get_coordinates(position_index: int, coordinates_matrix: list) -> tuple:
    counter = 0
    pos_coord = None

    for coordinates in coordinates_matrix:
        for coord in coordinates:
            if counter == position_index:
                pos_coord = coord
                break
            counter += 1
        if pos_coord:
            break

    return pos_coord


def get_lowest_f_score(neighbors):
    if not neighbors:
        return None
    
    min_f_score = float('inf')
    min_f_node = None
    
    for node in neighbors:
        if node['f'] < min_f_score:
            min_f_score = node['f']
            min_f_node = node
    
    return min_f_node


def get_bricks(matrix: list, paths: list) -> list:
    bricks = []

    for row in matrix:
        for col in row:
            if col not in paths:
                bricks.append(col)

    return bricks


if __name__ == "__main__":
    screen = screen_turtle()

    height = 200
    width = 100
    columns = 20
    square_size = 20

    draw_constraint(width, height)

    x_coord, y_coord = (-width, -200)
    coordinates_matrix =  gen_matrix_tuple(width, height)
    matrix = gen_matrix(10, 20)
    
    current_node = 19 # we started at node: 42
    target_node = 90

    open_list = []
    closed_list = [current_node] # This list contains current node, and traversed node.

    turtle_robot = init_turtle(coordinates_matrix, current_node)

    # bricks = [0, 10, 20, 30, 40, 190, 34, 54, 1, 11, 19, 29, 9,
    #           44, 179, 189, 199, 188, 196, 197, 198]
    

    paths = [19, 18, 17, 27, 24, 25,26, 14,
             13, 12, 11, 21, 31, 32, 42, 52,
             53, 54, 44, 64, 74, 61, 62, 63, 65,
             66, 67, 68, 46, 56, 57, 58, 48, 78, 88,
             87, 86, 96, 95, 94, 93, 92, 91, 90]
    
    bricks = get_bricks(matrix, paths)

    draw_maze(coordinates_matrix, target_node, square_size)

    # name = input('What do you want to name your robot? ')
    name = 'HALD'
    robot_pos = (0, 0)

    loop = 0
    for x in matrix:
        print(x)

    while True:
        robot_pos = turtle_robot.pos()
        print('robot_pos: ', robot_pos)
        x = robot_pos[0]
        y = robot_pos[1]
        
        current_node = get_node_position((x, y), coordinates_matrix)
        closed_list.append(current_node)

        if current_node == target_node:
            print('Destination reached...')
            break
        
        neighbour = get_neighbour(matrix, bricks, closed_list, current_node, target_node)

        print('neighbours of : ', current_node)
        for n in neighbour:
            print(n)

        print('current location: ', current_node)

        low_f_score = get_lowest_f_score(neighbour).get('Node', None)
        print('low_f_score: ', low_f_score)

        get_pos = get_coordinates(low_f_score, coordinates_matrix)
        turtle_robot.goto(get_pos[0], get_pos[1])

        # turtle.done() # to keep turtle screen open, for dev only...

    turtle.done()
        # command = input(f'{name}: What must I do next? ').strip()

        # if command == 'off':
        #     screen.bye()
        #     break

        # if command == 'right':
        #     turtle_robot.right(90)
        #     direction = (direction % 4) + 1

        # if command == 'left':
        #     turtle_robot.left(90)
        #     direction = (direction - 2) % 4 + 1

        # if command.startswith('forward'):
        #     args = command.split(' ')

        #     if not (len(args) >= 2 and args[1].isdigit()):
        #         print(f'{name}, Sorry, I did not understand {command}.')
        #         continue

        #     distance = int(args[1])
        #     turtle_robot.forward(distance)
