# Author: henning.s.strandaa@gmail.com
# Git: emasru

import matplotlib.pyplot as plt


def read():
    f = open("weather.txt", "r")

    date = []
    temperature = []
    downfall = []
    wind = []  # Åpner filen og lager nye lister

    for row in f:
        data = row.split()
        date.append(str(data[0]))
        temperature.append(float(data[1]))
        downfall.append(float(data[2]))
        wind.append(float(data[3]))  # Skriver dataen inn i listen for hver rad, splittet med mellomrom

    f.close()
    data = [date, temperature, downfall, wind]
    return data  # Lukker fila, og lager en ny liste som inneholder alle de andre listene, og returnerer denne


file_data = read()
print("Dato     Temperatur      Nedbør      Vind")
for x in range(len(file_data[0])):
    print(file_data[0][x], str(file_data[1][x]), str(file_data[2][x]), str(file_data[3][x]))  # Printer ut hver data, rekke for rekke

file_data_len = []
for x in range(len(file_data[0])):
    file_data_len.append(x)  # Lager en liste med lengden til dataen, noe some trengs til plottingen
print("")

user = input("Skriv inn om du vil ha temperatur(C), nedbør(mm), eller vind(m/s): ")
ax = plt.subplot(111)
try:
    if user == "temperatur":
        ax.bar(file_data_len, file_data[1], color="g")
    elif user == "nedbør":
        ax.bar(file_data_len, file_data[2], color="g")
    elif user == "vind":
        ax.bar(file_data_len, file_data[3], color="g")  # Sjekker input og plotter
    plt.show()
except ValueError:
    print("Noe du skrev inn ble feil, husk ingen stor bokstav")