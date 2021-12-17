from utils import *

x_min, x_max, y_min, y_max = parse_file("input.txt")

# we reach highest y by limiting the steps as much as possible
# i.e., we want to prevent from moving out of the zone in x
# as this allows y a steep fall
x = 0
i = 0
while x < x_min:
    i += 1
    x += i
print(x, i)

vel_x = i
y_peak = 0
vel_y_peak = None

for vel_y in range(-200, 200):
    success, steps = simulate_trajectory(vel_x, vel_y, x_min, x_max, y_min, y_max)
    if success:
        _, Y = zip(*steps)
        if max(Y) > y_peak:
            y_peak = max(Y)
            vel_y_peak = vel_y

print(vel_x, vel_y_peak, y_peak)  # peak y is 3160
