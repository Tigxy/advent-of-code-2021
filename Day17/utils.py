import re


def parse_file(file):
    with open(file) as fh:
        pattern = r"x=([\-0-9]+)\.\.([\-0-9]+).*y=([\-0-9]+)\.\.([\-0-9]+)"
        result = re.search(pattern, fh.read())

    return [int(result[i]) for i in range(1, result.lastindex + 1)]


def step_in_x(x, vel_x):
    x += vel_x
    if vel_x > 0:
        vel_x -= int(vel_x / abs(vel_x))
    return x, vel_x


def step_in_y(y, vel_y):
    y += vel_y
    vel_y -= 1
    return y, vel_y


def simulate_trajectory(vel_x, vel_y, x_min, x_max, y_min, y_max):
    steps = []
    current_x, current_y = 0, 0
    while current_x <= x_max and current_y >= y_min:
        step = (current_x, current_y)
        steps.append(step)

        if x_min <= current_x <= x_max and y_min <= current_y <= y_max:
            return True, steps

        current_x, vel_x = step_in_x(current_x, vel_x)
        current_y, vel_y = step_in_y(current_y, vel_y)

    return False, steps
