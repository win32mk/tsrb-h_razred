# -*- coding: utf-8 -*-

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

r = np.arange(1, 8, 0.0001)
k = float(9 * 10**9)

# Data for plotting
q = 50*10**-9
e = k * (q/(r*r))

fig, ax = plt.subplots()
ax.plot(r, e)

ax.set(xlabel='r (m)', ylabel='E (N/C)', title=u'Jakost električnog polja točkastog naboja\n(ovisnost o udaljenosti)')
ax.grid(b='false')

ax.set_yticklabels([])
ax.set_xticklabels([])

#plt.xlim(xmin=0)
#plt.ylim(ymin=0)

plt.show()