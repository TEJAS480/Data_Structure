SIZE = 10  # fixed size

hash_table = [-1] * SIZE


def hash_function(key):
    return key % SIZE


def insert(key):
    index = hash_function(key)
    start_index = index
    while hash_table[index] != -1:
        index = (index + 1) % SIZE
        if index == start_index:
            print("Hash table full! Cannot insert", key)
            return
    hash_table[index] = key
    print(f"Inserted {key} at index {index}")


def search(key):
    index = hash_function(key)
    start_index = index
    while hash_table[index] != -1:
        if hash_table[index] == key:
            print(f"Key {key} found at index {index}")
            return
        index = (index + 1) % SIZE
        if index == start_index:
            break
    print(f"Key {key} not found")


def delete(key):
    index = hash_function(key)
    start_index = index
    while hash_table[index] != -1:
        if hash_table[index] == key:
            hash_table[index] = -1
            print(f"Key {key} deleted from index {index}")
            return
        index = (index + 1) % SIZE
        if index == start_index:
            break
    print(f"Key {key} not found")


def display():
    print("\nHash Table:")
    for i, val in enumerate(hash_table):
        if val != -1:
            print(f"{i} --> {val}")
        else:
            print(f"{i} --> [empty]")


# Simple Menu
while True:
    print("\n1. Insert  2. Search  3. Delete  4. Display  5. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        key = int(input("Enter key to insert: "))
        insert(key)
    elif choice == 2:
        key = int(input("Enter key to search: "))
        search(key)
    elif choice == 3:
        key = int(input("Enter key to delete: "))
        delete(key)
    elif choice == 4:
        display()
    elif choice == 5:
        break
    else:
        print("Invalid choice! Try again.")
