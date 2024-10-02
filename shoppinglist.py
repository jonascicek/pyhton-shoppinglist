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

show_shoppinglist()