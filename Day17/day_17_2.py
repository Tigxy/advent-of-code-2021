from utils import *

x_min, x_max, y_min, y_max = parse_file("input.txt")

# determine minimum x velocity to reach field
x = 0
i = 0
while x < x_min:
    i += 1
    x += i
min_x_vel = i
max_x_vel = x_max

min_y_vel = y_min - 1
max_y_vel = 79     # from task 1 we already know that max y is this value

successful_trials = sum([1 for vel_x in range(min_x_vel, max_x_vel + 1) for vel_y in range(min_y_vel, max_y_vel + 1)
                         if (r := simulate_trajectory(vel_x, vel_y, x_min, x_max, y_min, y_max)) and r[0]])

print(successful_trials)  # result is 1928
