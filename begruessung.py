# Ein kleines Python-Begrüßungsprogramm

# --- NEU: Liste für mehrere Namen ---
namen = []

# --- NEU: Schleife – fragt 3x nach einem Namen ---
for i in range(3):
    name = input(f"Person {i + 1}, wie heißt du? ")
    namen.append(name)

# --- Ausgabe für jede Person ---
print("\nHallo an alle!")

for name in namen:
    laenge = len(name)
    print(f"  {name} – {laenge} Buchstaben", end="")

    if laenge > 5:
        print(" (langer Name!)")
    else:
        print(" (kurzer Name!)")

# --- NEU: Zusammenfassung ---
print(f"\nInsgesamt {len(namen)} Personen begrüßt.")
print(f"Alle Namen: {', '.join(namen)}")