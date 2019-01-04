# Author: henning.s.strandaa@gmail.com
# Git: emasru

import matplotlib.pyplot as plt


def read():
    f = open("temperaturer.txt", "r")

    date = []
    average = []
    normal = []  # Åpner filen og lager nye lister

    for row in f:
        data = row.split()
        date.append(str(data[0]))
        average.append(float(data[1]))
        normal.append(float(data[2]))  # Skriver dataen inn i listen for hver rad, splittet med mellomrom

    f.close()
    data = [date, average, normal]
    return data  # Lukker fila, og lager en ny liste som inneholder alle de andre listene, og returnerer denne


file_data = read()
print("Dato     Gjennomsnittstemperatur     Normaltemperatur")
for x in range(len(file_data[0])):
    print(file_data[0][x], str(file_data[1][x]), str(file_data[2][x]))  # Printer ut hver data, rekke for rekke

file_data_len = []
for x in range(len(file_data[0])):
    file_data_len.append(x)  # Lager en liste med lengden til dataen, noe some trengs til plottingen

# plt.bar(temperature_len, temperature[1], tick_label=temperature[0])
ax = plt.subplot(111)
ax.bar([x + 0.5 for x in file_data_len], file_data[1], color="r", tick_label=file_data[0], label="Gjennomsnittstemperatur")
ax.bar(file_data_len, file_data[2], color="g", label="Normaltemperatur")
ax.legend(loc='upper left')
plt.show()


