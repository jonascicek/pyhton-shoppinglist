# Import von sqlite
import sqlite3

# Connection to sqlite-DB (if this does not exist, one will be created)
conn = sqlite3.connect('shoppinglist.db')

# Creation of cursor to execute sql command. 
cursor = conn.cursor()

# Creation of tables in shoppinglist.db
cursor.execute('''
    CREATE TABLE IF NOT EXISTS shoppinglist (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(32) NOT NULL,
    amount INTEGER NOT NULL,
    price INTEGER NOT NULL
    );
''')

# Add first function (CREATE)
def add_item(name, amount, price):
    cursor.execute('''
    INSERT INTO shoppinglist (name, amount, price) VALUES (?, ?, ?)
    ''',(name, amount, price))
    conn.commit()
    print(f"{name} wurde hinzugefügt")

# Creation of READ function
def show_items():
    cursor.execute('SELECT id, name FROM shoppinglist')
    shoppinglist = cursor.fetchall()
    for name in shoppinglist:
        print(name)

# Update function to update Shoppinglist data
def update_item(id, name, amount, price):
    cursor.execute('''
    UPDATE shoppinglist SET id = ?, name = ?, amount = ?, price = ?
    WHERE id = ?               
    ''',(id, name, amount, price))
    conn.commit()
    print(f"updated shoppinglist with id {id}")

# Adding a delete function to delete a item
def delete_item(id):
    cursor.execute('''
    DELETE FROM shoppinglst WHERE id = ?                
    ''',(id,))
    conn.commit()
    print(f"Item has been deleted with id {id}")

# define main function to get the user input
# user can choose from create, read, update and delete function
def main():
    while True:
        print("\n----- shoppinglist -----")
        print("1. Add item")
        print("2. Show shoppinglist")
        print("3. Update item")
        print("4. Delete item")       
        print("5. Exit shoppinglist")

        choice = input("Please choose (1,2,3,4 or 5): ")

        if choice == "1":
            print("Please write down the new item")
            name = input("name: ")
            amount = input("amount: ")
            price = input("price: ")
            add_item(name, amount, price)
        elif choice == "2":
            show_items()
        elif choice == "3":
            print("Please update with id")
            id = input("id: ")
            name = input("name: ")
            amount = input("amount: ")
            price = input("price: ")
            update_item(id, name, amount, price)
        elif choice == "4":
            print("Please choose the id to be deleted")
            id = input("id: ")
            delete_item(id)
        elif choice == "5":
            print("Exiting programm, have a good day!")
            break
        else:
            print("False entry! Please choose 1,2,3,4 or 5")

if __name__ == "__main__":
    main()
