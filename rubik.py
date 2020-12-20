I = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23)

# 0-3: F - orange
# 4-7: R - blue
# 8-11: B - red
# 12-15: L - green
# 16-19: U - yellow
# 20-23: D - white

def apply_move(face, current_config):       #permute
    new_config = []
    for i in range(24):
        new_config.append(current_config[face[i]])
    return tuple(new_config)                #tuple is hashable


def get_counterclockwise_move(face):        #inverse permute
    cc_move = [0] * 24
    for i in range(24):
        cc_move[face[i]] = i
    return tuple(cc_move)

F = (3, 0, 1, 2, 19, 5, 6, 18, 8, 9, 10, 11, 12, 20, 21, 15, 16, 17, 13, 14, 7, 4, 22, 23)
Fc = get_counterclockwise_move(F)
F2 = (2, 3, 0, 1, 14, 5, 6, 13, 8, 9, 10, 11, 12, 7, 4, 15, 16, 17, 20, 21, 18, 19, 22, 23)


R = (0, 21, 22, 3, 7, 4, 5, 6, 18, 9, 10, 17, 12, 13, 14, 15, 16, 1, 2, 19, 20, 11, 8, 23)
Rc = get_counterclockwise_move(R)
R2 = (0, 11, 8, 3, 6, 7, 4, 5, 2, 9, 10, 1, 12, 13, 14, 15, 16, 21, 22, 19, 20, 17, 18, 23)


U = (4, 5, 2, 3, 8, 9, 6, 7, 12, 13, 10, 11, 0, 1, 14, 15, 19, 16, 17, 18, 20, 21, 22, 23)
Uc = get_counterclockwise_move(U)
U2 = (8, 9, 2, 3, 12, 13, 6, 7, 0, 1, 10, 11, 4, 5, 14, 15, 18, 19, 16, 17, 20, 21, 22, 23)


move_faces = [F, Fc, F2, R, Rc, R2, U, Uc, U2]
face_dict = {F: 'F',
             Fc: 'Fc',
             F2: 'F2',
             R: 'R',
             Rc: 'Rc',
             R2: 'R2',
             U: 'U',
             Uc: 'Uc',
             U2: 'U2'}


def color_config(config):
    config = list(config)
    for i in range(24):
        if 0 <= i and i <= 3:
            config[i] = 'o'
        elif 4 <= i and i <= 7:
            config[i] = 'b'
        elif 8 <= i and i <= 11:
            config[i] = 'r'
        elif 12 <= i and i <= 15:
            config[i] = 'g'
        elif 16 <= i and i <= 19:
            config[i] = 'y'
        elif 20 <= i and i <= 23:
            config[i] = 'w'

    return config


def neighbours(config, forward, backward):
    nxt_pos = {}
    if forward:
        for face in move_faces:
            nxt_pos[face_dict[face]] = apply_move(face, config)
        return nxt_pos

    else:
        for face in move_faces:
            nxt_pos[face_dict[get_counterclockwise_move(face)]] = apply_move(face, config)
        return nxt_pos
