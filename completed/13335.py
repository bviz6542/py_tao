# 다리 위에 트럭들 올라가는데 다리에 무게 제한 있음

from collections import deque

n, w, l = map(int, input().split())
cars = deque()
cars.extend(list(map(int, input().split())))

current_car_pos = deque()
current_car_pos.extend([0] * w)
time = 0
current_w_tot = 0

first_car = cars.popleft()
current_car_pos.append(first_car)
current_car_pos.popleft()
time = 1
current_w_tot += first_car

while current_w_tot != 0:
    out_car = current_car_pos.popleft()
    current_w_tot -= out_car
    time += 1
    if cars:
        in_car = cars[0]
        if in_car + current_w_tot <= l:
            cars.popleft()
            current_car_pos.append(in_car)
            current_w_tot += in_car
        else:
            current_car_pos.append(0)
    else:
        current_car_pos.append(0)

print(time)