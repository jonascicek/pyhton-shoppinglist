# python-shoppinglist

# Leere Einkaufsliste
shoppinglist = []

# Funktion zum hinzufügen eines Artikels
def add_item():
    item = input("Welche Artikel sollen auf die Einkaufsliste hinzugefügt werden: ")
    shoppinglist.append(item)
    print(f"{item} wurde der Einkaufsliste hinzugefügt.")
