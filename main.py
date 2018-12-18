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


temperature = read()
print("Dato     Gjennomsnittstemperatur     Normaltemperatur")
for x in range(len(temperature[0])):
    print(temperature[0][x], str(temperature[1][x]), str(temperature[2][x]))  # Printer ut hver data, rekke for rekke

temperature_len = []
for x in range(len(temperature[0])):
    temperature_len.append(x)

# plt.bar(temperature_len, temperature[1], tick_label=temperature[0])
ax = plt.subplot(111)
ax.bar([x+0.8 for x in temperature_len], temperature[1], color="r", tick_label=temperature[0])
ax.bar(temperature_len, temperature[2], color="g")
plt.show()
