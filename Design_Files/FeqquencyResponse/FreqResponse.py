"""
===========================
"""
import numpy as np
import matplotlib.pyplot as plt
import ltspice
import matplotlib.pyplot as plt
import math
import numpy as np
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)



filepath = r'FreqResponse.raw'
l = ltspice.Ltspice(filepath)
l.parse() # Data loading sequence. It may take few minutes for huge file.
print("Filen "+ filepath)
print("Inneholder følgende variabler : ")
for name in l.variables:
    print(name)

#For å legge inn matematiske utrykk inn i plotet se:
# W  riting mathematical expressions in Matplotlib. https://matplotlib.org/stable/tutorials/text/mathtext.html
ohm=r'$\Omega$'

#Data Som skal plottes på X/Y-Aksen
xAxisValues = l.get_data('frequency')
yAxisValues = l.get_data('v(vout)')

data2=np.angle(yAxisValues)*360/(math.pi*2)
data1=20*np.log10(abs(yAxisValues))
frequency=xAxisValues;

fig, ax1 = plt.subplots()


color = 'tab:blue'
ax1.set_xlabel('Frequency  [Hz]')
ax1.set_ylabel('Amplitude [dB]', color=color)
ax1.plot(frequency, data1, color=color,label="Phase",linestyle='-')

ax1.grid(linestyle='-', linewidth='0.5', color='red')
ax1.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
ax1.grid(which='major', linestyle=':', linewidth='0.5', color='black')
ax1.grid(True)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:red'
ax2.set_ylabel('Phase [deg]', color=color)  # we already handled the x-label with ax1
ax2.plot(frequency, data2, color=color,label="Amplitude",linestyle='dashed')

#Position Legends
ax1.legend(loc="upper left", bbox_to_anchor=(0.7,1.0))
ax2.legend(loc="upper left", bbox_to_anchor=(0.7,0.95))

plt.title("frekvens responsen målt i Vout")
plt.xscale('log')
fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()
