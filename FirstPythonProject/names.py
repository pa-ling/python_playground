# Aufgabe:
#
# Im Ordner "names" gibt es einige Textdateien, die Namen von Personen enthalten (zufällig generiert).
#
# Aufgabe:
#   Schreibe ein Programm, welches alle Textdateien aus dem Ordner "names" einliest, und ermittelt, wie oft der Name
#   "Max" insgesamt in allen Dateien vorkommt.
#
# Beispiel:
#   Käme der Name "Max" in der Datei "1.txt" 1x vor, und in der Datei "2.txt" 2x, sonst aber nie, soll das Programm
#   die Zahl 3 ausgeben.

import os
from collections import defaultdict

data_path = os.path.join(os.path.dirname(__file__), "names")
data_files = os.listdir(data_path)

names_count = defaultdict(int)

for file_name in data_files:
    file_path = os.path.join(data_path, file_name)

    with open(file_path, encoding="utf-8") as file:
        for full_name in file:
            forename = full_name.split()[0]
            names_count[forename] = names_count[forename] + 1

print("The name 'Max' was found " + str(names_count["Max"]) + " times")