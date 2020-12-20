import rubik
import solve
import play
import random
import time

I = rubik.I
choices = rubik.move_faces

scramble = I
step = []
for i in range(15):
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
print("\n")


play.playing(steps)
