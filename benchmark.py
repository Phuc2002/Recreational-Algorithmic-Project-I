import solve
import rubik
import random
import time

I = rubik.I
choices = rubik.move_faces

for j in range(0, 13):
    scramble = I
    step = []
    for i in range(j+1):
        step.append(choices[random.randint(0, 8)])
        new = rubik.apply_move(step[i], scramble)
        scramble = new
        step[i] = rubik.face_dict[step[i]]


    start = scramble
    end = I
    print("Scramble", step)

    s = time.time()
    steps = solve.bidirectional_bfs_shortest_path(start, end)
    e = time.time()
    print("Solve with 2-way BFS", steps, e - s)
    #print("\n\n")

    s = time.time()
    steps1 = solve.bfs_shortest_path(start, end)
    e = time.time()
    print("Solve with 1-way BFS", steps1, e - s)
    print("\n")

