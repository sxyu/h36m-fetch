#!/home/sxyu/anaconda3/bin/python
import h5py
import sys
if len(sys.argv) != 3:
    print('Wrong number of arguments', len(sys.argv), 'expected 2 arguments: file imageidx')
    sys.exit()

fname = sys.argv[1]
idx = int(sys.argv[2])

from matplotlib import pyplot as plt
import numpy as np
with h5py.File(fname, 'r') as f:
    autokey = sorted(list(f.keys()))[-1]
    print('Using key:', autokey)
    print(len(f[autokey]))
    print('Load', idx, 'of', len(f[autokey]))
    im = f[f[autokey][idx, 0]]
    print('Shape', im.shape)
    plt.imshow(np.array(im).T, cmap='Greys')
    plt.show()
