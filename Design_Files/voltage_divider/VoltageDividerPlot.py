import ltspice
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="whitegrid")

#Input Plot file
filepath = r'VoltageDivider.raw'
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
xAxisValues = l.get_data('var_r1')
yAxisValues = l.get_data('v(vout)')

#Plot X/Y aksen og ha med lavelen Vout
plt.plot(xAxisValues, yAxisValues,label='Vout')

#Sett akse navn
plt.xlabel('R1 [%s]'%ohm)
plt.ylabel('Vout [V]')

#Sett navn på plottet
plt.title("Utgans spenningen Vout")

#Vis labelen 'Vout'
plt.legend()

#Vis plot dialogboksen
plt.show()
