from pygame import mixer

mixer.init()
C = mixer.Sound("music/Sounds/c4.wav")
D = mixer.Sound("music/Sounds/d4.wav")
Db = mixer.Sound("music/Sounds/c40.wav")
E = mixer.Sound("music/Sounds/e4.wav")
Eb = mixer.Sound("music/Sounds/d40.wav")
F = mixer.Sound("music/Sounds/f4.wav")
G = mixer.Sound("music/Sounds/g4.wav")
Gb = mixer.Sound("music/Sounds/f40.wav")
A = mixer.Sound("music/Sounds/a4.wav")
Ab = mixer.Sound("music/Sounds/g40.wav")
B = mixer.Sound("music/Sounds/b4.wav")
Bb = mixer.Sound("music/Sounds/a40.wav")

C1 = mixer.Sound("music/Sounds/c5.wav")
D1 = mixer.Sound("music/Sounds/d5.wav")
D1b = mixer.Sound("music/Sounds/c50.wav")
E1 = mixer.Sound("music/Sounds/e5.wav")
E1b = mixer.Sound("music/Sounds/d50.wav")
F1 = mixer.Sound("music/Sounds/f5.wav")
G1b = mixer.Sound("music/Sounds/f50.wav")
G1 = mixer.Sound("music/Sounds/g5.wav")
A1 = mixer.Sound("music/Sounds/a5.wav")
A1b = mixer.Sound("music/Sounds/g50.wav")
B1 = mixer.Sound("music/Sounds/b5.wav")
B1b = mixer.Sound("music/Sounds/a50.wav")

note_to_sound = {"C": C, "Db": Db, "D": D, "Eb": Eb, "E": E, "F": F, "Gb": Gb, "G": G, "Ab": Ab, "A": A, "Bb": Bb, "B": B,
                 "C1": C1, "D1b": D1b, "D1": D1, "E1b": E1b, "E1": E1, "F1": F1, "G1b": G1b, "G1": G1, "A1b": A1b, "A1": A1, "B1b": B1b, "B1": B1}
sound_to_note = {}
for key in note_to_sound:
    sound_to_note[note_to_sound[key]] = key

chromatic = [C, Db, D, Eb, E, F, Gb, G, Ab, A, Bb, B, C1, D1b, D1, E1b, E1, F1, G1b, G1, A1b, A1, B1b, B1]

scales = {'C': ["C", "D", "E", "F", "G", "A", "B"],             #these are just some examples of the music scales
          'D': ["D", "E", "Gb", "G", "A", "B", "Db"],
          'G': ["G", "A", "B", "C", "D", "E", "Gb"],
          'A': ["A", "B", "Db", "D", "E", "Gb", "Ab"],
          'F': ["F", "G", "A", "Bb", "C", "D", "E"],
          'E': ["E", "Gb", "Ab", "A", "B", "Db", "Eb"],
          'B': ["B", "Db", "Eb", "E", "Gb", "Ab", "Bb"],
          }

progression = [1, 4, 0]

f_inversion = [1, [1, 2, 3, 0]]         # 1st inversion of chord
s_inversion = [2, [2, 3, 0, 1]]         # 2nd inversion of chord
t_inversion = [3, [3, 0, 1, 2]]         # 3rd inversion of chord
root = [0, [0, 1, 2, 3]]                # original chord

map = {('F', 'U', 'R'): t_inversion,
       ('F2', 'U2', 'R2'): s_inversion,
       ('Fc', 'Uc', 'Rc'): f_inversion}


def build(str, scale):                  # stack up the notes like a snowman to build a chord
    sound = []
    name = []
    ptr = scale.index(str)
    for i in range(4):
        sound.append(note_to_sound[scale[ptr]])
        name.append(scale[ptr])
        ptr = (ptr + 2) % 7

    return sound, name


def get_chords(key):
    chords = []
    names = []
    for i in progression:
        tmp = []
        name = []
        base = scales[key][i]

        if i == 4:                                  # it's a dominant7 chord
            tmp, name = build(base, scales[key])
            tmp, name = chord_inversion(tmp, s_inversion[1], 0)

        else:                                       # else it's a major7 chord or a minor7 chord
            tmp, name = build(base, scales[key])

        chords.append(tmp)
        names.append(name)
    return chords, names


def assign_chord(face, chord):
    for key in map:
        if face in key:
            play, name = chord_inversion(chord, map[key][1], map[key][0])

    return play, name               #return the chord to play


def chord_inversion(chord, inversion, count):
    new = []
    name = []
    for i in range(4):
        new.append(chord[inversion[i]])
        name.append(sound_to_note[chord[inversion[i]]])

    for i in range(1, count + 1):
        tmp = new[-i]
        new[-i] = chromatic[chromatic.index(new[-i]) + 12]                  #an octave higher
        name[-i] = sound_to_note[chromatic[chromatic.index(tmp) + 12]]      #an octave higher
    return new, name

