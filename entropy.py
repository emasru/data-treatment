s_liste = [-10, 0.9, 5.1, 1.5, -0.1, 3, -0.4, 0.5, 0.8, 0.1]
h_liste = [100, 12, -100, -75, -20, 10, 20, -35, 49, -10]
T = 298
spontaneous_count = 0  # Definerer verdier


def is_spontaneous(entropy, enthalpy):
    energy = enthalpy - (T * entropy)
    if energy < 0:
        return True
    else:
        return False  # Lager en funksjon som sjekker om to verdier gjør reaksjonen spotant


for x in s_liste:
    for y in h_liste:
        spontaneous = is_spontaneous(x, y)
        if spontaneous is True:
            spontaneous_count += 1  # Sjekker listene med alle muligheter

print("Antallet mulige spontane reaksjoner:", spontaneous_count)
