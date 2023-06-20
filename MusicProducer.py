import numpy as np
from scipy.io.wavfile import write

samplerate = 44100
amplitude = 4096

def Freq(note):
    base = 261.63
    octave = {'c ' : 0, 'c#' : 1, 'db' : 1, 'd ' : 2, 'd#' : 3, 'eb' : 3, 'e ' : 4, 'f ' : 5, 'f#' : 6, 'gb' : 6, 'g ' : 7, 'g#' : 8, 'ab' : 8, 'a ' : 9, 'a#' : 10, 'bb' : 11, 'b ' : 11}
    note = note.lower()

    if note[0] == ' ':
        return 0.0

    try:
        return base * pow(2, (octave[note[:2]] / 12)) * pow(2, int(note[2]) - 4)
    except:
        print(f'invalid note: {note}')

def Wave(freq, duration=0.25):
    t = np.linspace(0, duration, int(samplerate * duration))
    wave = amplitude * np.sin(2 * np.pi * freq * t)

    return wave

def Song(notes):
    if len(notes) % 3 != 0:
        print("wrong length of songs notes; must be divisible by 3")
        return None

    song = [Wave(Freq(notes[i*3] + notes[i*3+1] + notes[i*3+2])) for i in range(int(len(notes) / 3))]
    song = np.concatenate(song)
    return song

def Compile(notes, changes, octaves):
    if len(notes) != len(changes) or len(notes) != len(octaves):
        print("wrong lengths of notes, changes, or octaves")
        return None

    ret = ''
    for i in range(len(notes)):
        ret += notes[i] + changes[i] + octaves[i]
    return ret


def Producer(notes, changes, octaves, name):
    # notes   = 'ddd a   a g f dfg'
    # changes = '        b        '
    # octaves = '44544444444444444'

    notes = Compile(notes, changes, octaves)
    song = Song(notes)

    return song

def main():
    Producer(None, None, None, None)

if __name__ == '__main__':
    main()
