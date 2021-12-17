from utils import *

x_min, x_max, y_min, y_max = parse_file("input.txt")

# example trajectories from instructions
trajectories = [(7, 2), (6, 3), (9, 0), (6, 9), (17, -4)]
for tx, ty in trajectories:
    success, steps = simulate_trajectory(tx, ty, x_min, x_max, y_min, y_max)
    X, Y = zip(*steps)
    print("Simulating trajectory with initial value x=%d y=%d" % (tx, ty))
    print("Successfully hit zone:", success)
    print("Trajectory:", steps)
    print("Max y reached:", max(Y))
    print()

