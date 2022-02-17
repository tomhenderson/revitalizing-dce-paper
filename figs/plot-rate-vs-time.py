#!/usr/bin/env python3
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
import sys
import numpy as np

title = "Sending rate vs wall clock time"
filename = 'rate-vs-time.png'

f = open("rate-vs-time.dce11.elf.dat")
rate = []
clock = []
for line in f:
    if not line.startswith('#'):
        columns = line.split()
        rate.append(float(columns[2]))
        clock.append (float(columns[4]))
f.close()

f2 = open("rate-vs-time.tazaki.dat")
rate2 = []
clock2 = []
for line in f2:
    if not line.startswith('#'):
        columns = line.split()
        rate2.append(float(columns[2]))
        clock2.append (float(columns[4]))
f2.close()

f3 = open("rate-vs-time.ns3.dat")
rate3 = []
clock3 = []
for line in f3:
    if not line.startswith('#'):
        columns = line.split()
        rate3.append(float(columns[2]))
        clock3.append (float(columns[4]))
f3.close()

f4 = open("rate-vs-time.dce11.dat")
rate4 = []
clock4 = []
for line in f4:
    if not line.startswith('#'):
        columns = line.split()
        rate4.append(float(columns[2]))
        clock4.append (float(columns[4]))
f4.close()


plt.xlabel('Sending rate (Mbps)')
plt.ylabel('Wall clock time (s)')
#plt.xlim([20,20.5])
#plt.title(title, fontdict = {'fontsize' : 12})
plt.axhline(y=100, color='black', linestyle='--')
plt.plot(rate4, clock4, marker='x', color='red', label='4 hops DCE-1.11')
plt.plot(rate, clock, marker='+', color='black', label='4 hops DCE-1.11 ELF')
plt.plot(rate2, clock2, marker='*', color='green', label='4 hops Tazaki')
plt.plot(rate3, clock3, marker='o', color='blue', label='4 hops ns-3')
plt.legend(loc='upper left')
plt.ticklabel_format(useOffset=False)
#plt.show()
#plt.savefig(filename, format='pdf')
plt.savefig(filename, format='png')
plt.close()
