import rubik
from myqueue import *

def get_path(parent, end):
    if end not in parent:
        return []

    shortest_path = []
    while parent[end] != None:                      #backtracking to the source (start)
        end = parent[end]
        move = end[1]
        shortest_path.append(move)
        end = end[0]

    shortest_path.reverse()                         #since we're backtracking, we're going in opposite direction
    return shortest_path

def bfs_shortest_path(start, end):
    count = 0
    flag = 0
    parent_visited = {start: None}
    visit_next = [start]                            #queue ADT

    while isempty(visit_next) is False:             #vertices to visit next in the queue until no more vertices
        count += 1
        config = dequeue(visit_next)
        next_positions = rubik.neighbours(config, True, False)

        for face in next_positions:                                  #check edges of the current vertex
            if next_positions[face] in parent_visited:               #if already visited
                continue
            if end in parent_visited:
                flag = 1
                break
            else:                                                                #if not visit yet
                parent_visited[next_positions[face]] = (config, face)            #config is the parent of the current vertex
                enqueue(visit_next, next_positions[face])

        if flag:
            break
    print("Visit %d vertices" % count)
    return get_path(parent_visited, end)

def bidirectional_bfs_shortest_path(start, end):
    count = 0
    parent_forward = {start: None}
    parent_backward = {end: None}
    visit_forward = [start]
    visit_backward = [end]

    if start == end:
        return []

    while True:         #or while isempty(visit_forward) is False or isempty(visit_backward) is False:
        count += 1
        config_forward = dequeue(visit_forward)
        config_backward = dequeue(visit_backward)
        forward = rubik.neighbours(config_forward, True, False)
        backward = rubik.neighbours(config_backward, False, True)

        for vertex in forward:
            if forward[vertex] not in parent_forward:
                parent_forward[forward[vertex]] = (config_forward, vertex)
                enqueue(visit_forward, forward[vertex])

            if forward[vertex] in parent_backward:
                path_forward = get_path(parent_forward, forward[vertex])
                path_backward = get_path(parent_backward, forward[vertex])
                path_backward.reverse()

                print("Visit %d vertices" % (count * 2))
                return path_forward + path_backward

        for vertex in backward:
            if backward[vertex] not in parent_backward:
                parent_backward[backward[vertex]] = (config_backward, vertex)
                enqueue(visit_backward, backward[vertex])

            if backward[vertex] in parent_forward:
                path_forward = get_path(parent_forward, backward[vertex])
                path_backward = get_path(parent_backward, backward[vertex])
                path_backward.reverse()

                print("Visit %d vertices" % (count * 2))
                return path_forward + path_backward




