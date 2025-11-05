from PIL import Image
import numpy as np


def transition(i1, i2):
    a = np.array(Image.open(i1))
    b = np.array(Image.open(i2))
    al, ac, ar = np.hsplit(a, 3)
    bl, bc, br = np.hsplit(b, 3)
    length = ac.shape[1]
    print(length)
    c = np.linspace(99, 1, length) / 100
    c = c[np.newaxis, :, np.newaxis]
    ac = ac * c
    c = np.linspace(1, 99, length) / 100
    c = c[np.newaxis, :, np.newaxis]
    bc = bc * c
    nc = ac + bc
    n = np.hstack((al, nc, br))
    Image.fromarray(n.astype(np.uint8)).save('pic.png')