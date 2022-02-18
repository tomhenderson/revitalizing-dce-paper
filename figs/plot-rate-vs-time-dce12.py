#!/usr/bin/env python3
import matplotlib
matplotlib.use("agg")
import matplotlib.pyplot as plt
import sys
import numpy as np

title = "Sending rate vs wall clock time"
filename = 'rate-vs-time-dce12.png'

#f = open("rate-vs-time.dce11.elf.dat")
#rate = []
#clock = []
#for line in f:
#    if not line.startswith('#'):
#        columns = line.split()
#        rate.append(float(columns[2]))
#        clock.append (float(columns[4]))
#f.close()

#f2 = open("rate-vs-time.tazaki.dat")
#rate2 = []
#clock2 = []
#for line in f2:
#    if not line.startswith('#'):
#        columns = line.split()
#        rate2.append(float(columns[2]))
#        clock2.append (float(columns[4]))
#f2.close()

f3 = open("rate-vs-time.dce12.ns3.dat")
rate3 = []
clock3 = []
for line in f3:
    if not line.startswith('#'):
        columns = line.split()
        rate3.append(float(columns[2]))
        clock3.append (float(columns[4]))
f3.close()

f4 = open("rate-vs-time.dce12.dat")
rate4 = []
clock4 = []
for line in f4:
    if not line.startswith('#'):
        columns = line.split()
        rate4.append(float(columns[2]))
        clock4.append (float(columns[4]))
f4.close()

f5 = open("rate-vs-time.dce12.5.10.docker.dat")
rate5 = []
clock5 = []
for line in f5:
    if not line.startswith('#'):
        columns = line.split()
        rate5.append(float(columns[2]))
        clock5.append (float(columns[4]))
f5.close()

f6 = open("rate-vs-time.dce12.5.10.dat")
rate6 = []
clock6 = []
for line in f6:
    if not line.startswith('#'):
        columns = line.split()
        rate6.append(float(columns[2]))
        clock6.append (float(columns[4]))
f6.close()

f7 = open("rate-vs-time.dce12.4.4.dat")
rate7 = []
clock7 = []
for line in f4:
    if not line.startswith('#'):
        columns = line.split()
        rate7.append(float(columns[2]))
        clock7.append (float(columns[4]))
f7.close()

plt.xlabel('Sending rate (Mbps)')
plt.ylabel('Wall clock time (s)')
#plt.xlim([20,20.5])
#plt.title(title, fontdict = {'fontsize' : 12})
plt.axhline(y=100, color='black', linestyle='--')
plt.plot(rate4, clock4, marker='x', color='red', label='DCE-1.12')
plt.plot(rate7, clock7, marker='v', color='orange', label='DCE-1.12 kernel 4.4')
plt.plot(rate6, clock6, marker='^', color='purple', label='DCE-1.12 kernel 5.10')
plt.plot(rate5, clock5, marker='+', color='black', label='DCE-1.12 kernel 5.10 Docker')
#plt.plot(rate2, clock2, marker='*', color='green', label='Tazaki [1]')
plt.plot(rate3, clock3, marker='o', color='blue', label='ns-3')
plt.legend(loc='upper left')
plt.ticklabel_format(useOffset=False)
#plt.show()
#plt.savefig(filename, format='pdf')
plt.savefig(filename, format='png')
plt.close()
