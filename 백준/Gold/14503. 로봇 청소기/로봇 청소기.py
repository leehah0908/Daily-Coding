# r, c, d = 7, 4, 0
# room_map = [
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
#     [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
#     [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
#     [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
#     [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
#     [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# ]

N, M = map(int, input().split())
r, c, d = map(int, input().split())
room_map = []

for i in range(N):
    room_map.append(list(map(int, input().split())))

front_calculator_r = [-1, 0, 1, 0]
front_calculator_c = [0, 1, 0, -1]

back_calculator_r = [1, 0, -1, 0]
back_calculator_c = [0, -1, 0, 1]

def go_left(r, c, d):
    if d == 0:
        d = 3
    else:
        d -= 1

    r += front_calculator_r[d]
    c += front_calculator_c[d]
    return r, c, d

def go_back(r, c, d):
    r += back_calculator_r[d]
    c += back_calculator_c[d]
    return r, c


def get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map):
    room_map[r][c] = 2
    clean_count = 1

    while True:
        for i in range(4):
            new_r, new_c, new_d = go_left(r, c, d)

            if room_map[new_r][new_c] == 0:
                room_map[new_r][new_c] = 2
                clean_count += 1
                r, c, d = new_r, new_c, new_d
                break
            else:
                d = new_d

            if i == 3:
                new_r, new_c = go_back(r, c, d)
                if room_map[new_r][new_c] == 1:
                    return clean_count
                r, c = new_r, new_c

print(get_count_of_departments_cleaned_by_robot_vacuum(r, c, d, room_map))