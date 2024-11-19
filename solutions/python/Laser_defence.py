data = [int(x) for x in input().split()]
L = data[0]
A = data[1]
B = data[2]

laser_a_u = []
laser_a_r = []
laser_b_u = []
laser_b_l = []

area = 1


for i in range(A):
    laser = input().split()
    place = laser[0]
    coordinate = int(laser[1])
    if place == "U":
        laser_a_u.append(laser[1])
    else:
        laser_a_r.append(laser[1])

for i in range(B):
    laser = input().split()
    place = laser[0]
    coordinate = int(laser[1])
    if place == "U":
        laser_b_u.append(laser[1])
    else:
        laser_b_l.append(laser[1])


area = area + A + B

area = area + len (laser_b_l) * A + len(laser_b_u) * len(laser_a_r)

for laser_b in laser_b_u:
    for laser_a in laser_a_u:
        if int(laser_b) < int(laser_a):
            area = area + 1

print(area)
