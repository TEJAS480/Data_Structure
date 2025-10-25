class TextEditor:
    def __init__(self):
        self.text = ""          # Current text
        self.undo_stack = []    # Stores history for Undo
        self.redo_stack = []    # Stores undone actions for Redo

    def make_change(self, new_text):
        self.undo_stack.append(self.text)
        self.text = new_text
        self.redo_stack.clear()  # Once new change is made, redo history resets
        print("✅ Change made.")

    def undo_action(self):
        if not self.undo_stack:
            print("⚠️ Nothing to undo.")
            return
        self.redo_stack.append(self.text)
        self.text = self.undo_stack.pop()
        print("↩️ Undo performed.")

    def redo_action(self):
        if not self.redo_stack:
            print("⚠️ Nothing to redo.")
            return
        self.undo_stack.append(self.text)
        self.text = self.redo_stack.pop()
        print("↪️ Redo performed.")

    def display_document_state(self):
        print("📄 Current Document State:", self.text)


# -------- MAIN PROGRAM --------
editor = TextEditor()

while True:
    print("\n--- Text Editor Menu ---")
    print("1. Make a Change")
    print("2. Undo")
    print("3. Redo")
    print("4. Display Document State")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        new_text = input("Enter new document text: ")
        editor.make_change(new_text)
    elif choice == "2":
        editor.undo_action()
    elif choice == "3":
        editor.redo_action()
    elif choice == "4":
        editor.display_document_state()
    elif choice == "5":
        print("👋 Exiting program...")
        break
    else:
        print("❌ Invalid choice. Try again.")
