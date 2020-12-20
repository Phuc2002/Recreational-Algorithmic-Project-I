from music import *
from pygame.mixer import Channel
import time


def jazz(chord, style):
    if style == "H":
        base, t, f, s = chord
        Channel(0).play(base)
        # time.sleep(0.60)
        Channel(1).play(t)
        # time.sleep(0.60)
        Channel(2).play(f)
        # time.sleep(0.60)
        Channel(3).play(s)
        time.sleep(1.6)
    else:
        i = 0
        for note in chord:
            Channel(i).play(note)               #change the channel so that it doesn't get stuck with multiple sounds at once
            time.sleep(0.75)
            i += 1
            if i == 7:
                i = 0


def playing(moves):
    assign = {("F", "Fc", "F2"): None, ("U", "Uc", "U2"): None, ("R", "Rc", "R2"): None}
    music = {}

    scale = input("""What music scale you want to play in:
Enter A, B, C, D, E, F or G: """)
    style = input("What style? Enter A for Arpeggio or H for Harmonious chords: ")
    chords, names = get_chords(scale)
    i = 0
    for key in assign:
        assign[key] = chords[i]
        i += 1

    for key in assign:
        for face in key:
            music[face] = assign_chord(face, assign[key])

    print(names)
    for chord in chords:
        jazz(chord, style)

    for move in moves:
        sound, name = music[move]
        print(name)
        jazz(sound, style)

    print(names)
    for chord in chords:
        jazz(chord, style)
