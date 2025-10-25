# Hash Table Implementation using Division Method and Chaining

class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [[] for _ in range(self.size)]  # Create 10 empty lists for chaining

    # Hash function using division method
    def hash_function(self, key):
        return key % self.size

    # Insert key-value pair
    def insert(self, key, value):
        index = self.hash_function(key)
        # Check if key already exists, update value if it does
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                print(f"Updated: Key {key} -> Value {value}")
                return
        # Otherwise, add new pair
        self.table[index].append([key, value])
        print(f"Inserted: Key {key} -> Value {value}")

    # Search for a value using key
    def search(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                print(f"Found: Key {key} -> Value {pair[1]}")
                return pair[1]
        print(f"Key {key} not found.")
        return None

    # Delete key-value pair
    def delete(self, key):
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                self.table[index].remove(pair)
                print(f"Deleted: Key {key}")
                return
        print(f"Key {key} not found. Cannot delete.")

    # Display hash table contents
    def display(self):
        print("\nHash Table:")
        for i, bucket in enumerate(self.table):
            print(f"Index {i}: {bucket}")

# -----------------------------
# Example Usage
# -----------------------------
if __name__ == "__main__":
    ht = HashTable()

    # Insert elements
    ht.insert(15, "Apple")
    ht.insert(25, "Banana")
    ht.insert(35, "Cherry")
    ht.insert(5, "Mango")

    ht.display()

    # Search elements
    ht.search(25)
    ht.search(40)

    # Delete element
    ht.delete(15)
    ht.display()
