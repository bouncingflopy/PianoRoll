import numpy as np
from tkinter import Tk, Button
import keyboard as kb
from MusicProducer import Producer
from scipy.io.wavfile import write

class button():
    text = '-'
    textBlank = '-'
    colorBlank = 'white'
    colorPressed = 'lightblue'
    note = 'c '

    def __init__(self, root, note, colorPressed, column, row):
        self.obj = Button(root, text='-', command=self.Switch, width=1, heigh=1, bg='white')
        self.note = note
        self.colorPressed = colorPressed
        self.column = column
        self.row = row

    def Switch(self):
        if self.obj['text'] == '-':
            self.obj['text'] = self.note
            self.obj['bg'] = self.colorPressed
            self.text = self.note
            self.color = self.colorPressed
        else:
            self.obj['text'] = self.textBlank
            self.obj['bg'] = self.colorBlank
            self.text = self.textBlank
            self.color = self.colorBlank

def TkSetup(beats):
    root = Tk()
    notes = ['c ', 'c#', 'd ', 'd#', 'e ', 'f ', 'f#', 'g ', 'g#', 'a ', 'a#', 'b ']
    colors = ['red', 'orange', 'yellow', 'lightgreen', 'darkgreen', 'darkblue', 'blue', 'lightblue', 'pink', 'magenta', 'purple', 'violet']
    pad = [[button(root, notes[11-r], colors[11-r], i, r) for i in range(beats)] for r in range(12)]

    for p in pad:
        for b in p:
            b.obj.grid(column=b.column, row=b.row)

    return root, pad

def main():
    root, pad = TkSetup(16)

    while not kb.is_pressed('SPACE'):
        root.update_idletasks()
        root.update()

    mainNotes = ['c ', 'c#', 'd ', 'd#', 'e ', 'f ', 'f#', 'g ', 'g#', 'a ', 'a#', 'b ']
    notes = [[(pad[11-i][n].text[0] if pad[11-i][n].text[0] == mainNotes[i][0] else ' ') for n in range(len(pad[i]))] for i in range(len(pad))]
    notes = [''.join(note) for note in notes]
    changes = [' ' * len(pad[0]), '#' * len(pad[0]), ' ' * len(pad[0]),
                '#' * len(pad[0]), ' ' * len(pad[0]), ' ' * len(pad[0]),
                '#' * len(pad[0]), ' ' * len(pad[0]), '#' * len(pad[0]),
                ' ' * len(pad[0]), '#' * len(pad[0]), ' ' * len(pad[0])]
    octaves = ['4'*len(pad[0]) for i in range(len(pad))]

    output = Producer(notes[0], changes[0], octaves[0], f'n0')
    for i in range(len(pad)-1):
        output += Producer(notes[i+1], changes[i+1], octaves[i+1], f'n{i+1}')

    samplerate = 44100
    output = output * (16300/np.max(output))
    write(f'song.mp3', samplerate, output.astype(np.int16))

if __name__ == '__main__':
    main()
