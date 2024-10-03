# python-shoppinglist

# Leere Einkaufsliste
shoppinglist = []

# Funktion zum hinzufügen eines Artikels
def add_item():
    item = input("Welche Artikel sollen auf die Einkaufsliste hinzugefügt werden: ")
    shoppinglist.append(item)
    print(f"{item} wurde der Einkaufsliste hinzugefügt.")

# Funktion zum Anzeigen der Einkaufsliste

def show_shoppinglist():
    if shoppinglist:
        print("Deine Einkaufliste:")
        for item in shoppinglist:
            print(f"{item}")
    else:
        print("Die Einkaufsliste ist leer.")

# Haupt Funktion

def main():
    while True:
        print("-----Einkaufsliste-----")
        print("1. Artikel zur Einkaufsliste hinzufügen")
        print("2. Einkaufsliste anzeigen")
        print("3. Programm beenden")

    # Speichere die Eingabe des Benutzers in der Variable choice
        choice = input("Gib deine Wahl ein (1/2/3)")
        if choice == "1":
            add_item()
        elif choice == "2":
            show_shoppinglist()
        elif choice == "3":
            print("Programm wird beendet! Auf Wiedersehen")
            break
        else:
            print("Ungültige Auswahl. Bitte wähle 1, 2 oder 3")

# Wenn erst das Script gestartet wird soll das Hauptprogramm ausgeführt werden.

if __name__ == "__main__":
    main()
