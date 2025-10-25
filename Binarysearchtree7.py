class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# BST class containing all operations
class BST:
    def __init__(self):
        self.root = None

    # Insertion in BST
    def insert(self, root, key):
        if root is None:
            return Node(key)
        if key < root.data:
            root.left = self.insert(root.left, key)
        elif key > root.data:
            root.right = self.insert(root.right, key)
        return root

    # Inorder Traversal (sorted order)
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    # Search for a value in BST
    def search(self, root, key):
        if root is None:
            return False
        if root.data == key:
            return True
        elif key < root.data:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    # Find the minimum value node in BST
    def minValueNode(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    # Delete a node from BST
    def delete(self, root, key):
        if root is None:
            return root

        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Node with two children: Get inorder successor
            temp = self.minValueNode(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        return root


# --- Usage Example ---
bst = BST()
root = None

# Inserting elements
elements = [50, 30, 20, 40, 70, 60, 80]
for el in elements:
    root = bst.insert(root, el)

print("Inorder traversal of BST:")
bst.inorder(root)
print()

# Searching elements
key = 40
if bst.search(root, key):
    print(f"{key} found in BST")
else:
    print(f"{key} not found in BST")

# Deleting an element
root = bst.delete(root, 20)
print("Inorder traversal after deleting 20:")
bst.inorder(root)
print()

root = bst.delete(root, 30)
print("Inorder traversal after deleting 30:")
bst.inorder(root)
print()

root = bst.delete(root, 50)
print("Inorder traversal after deleting 50:")
bst.inorder(root)
print()
