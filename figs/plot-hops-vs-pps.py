#!/usr/bin/env python3
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
import sys
import numpy as np

title = "Figure 3-like experiment"
filename = 'hops-vs-pps.png'

f = open("hops-vs-pps.dce11.elf.dat")
hops = []
pps = []
for line in f:
    columns = line.split()
    hops.append(float(columns[1]))
    pps.append (float(columns[5]))
f.close()

f2 = open("hops-vs-pps.tazaki.dat")
hops2 = []
pps2 = []
for line in f2:
    columns = line.split()
    hops2.append(float(columns[0]))
    pps2.append (float(columns[1]))
f2.close()

plt.xlabel('Number of hops')
plt.ylabel('Received packets per wall clock (pps)')
#plt.xlim([20,20.5])
#plt.title(title, fontdict = {'fontsize' : 12})
plt.plot(hops, pps, marker='+', color='black', label='DCE-1.11 ELF')
plt.plot(hops2, pps2, marker='*', color='green', label='Tazaki')
plt.legend(loc='upper right')
plt.ticklabel_format(useOffset=False)
#plt.show()
plt.savefig(filename, format='png')
plt.close()
