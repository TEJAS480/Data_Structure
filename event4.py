from collections import deque

class EventSystem:
    def __init__(self):
        self.queue = deque()

    def add_event(self, event):
        self.queue.append(event)
        print(f"✅ Event '{event}' added to queue.")

    def process_next_event(self):
        if not self.queue:
            print("⚠️ No events to process.")
            return
        event = self.queue.popleft()
        print(f"⚡ Event '{event}' processed and removed from queue.")

    def display_pending_events(self):
        if not self.queue:
            print("📭 No pending events.")
        else:
            print("📋 Pending Events:", list(self.queue))

    def cancel_event(self, event):
        if event in self.queue:
            self.queue.remove(event)
            print(f"❌ Event '{event}' canceled successfully.")
        else:
            print(f"⚠️ Event '{event}' not found or already processed.")


# -------- MAIN PROGRAM --------
system = EventSystem()

while True:
    print("\n--- Real-Time Event Processing System ---")
    print("1. Add an Event")
    print("2. Process Next Event")
    print("3. Display Pending Events")
    print("4. Cancel an Event")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        event = input("Enter event name: ")
        system.add_event(event)
    elif choice == "2":
        system.process_next_event()
    elif choice == "3":
        system.display_pending_events()
    elif choice == "4":
        event = input("Enter event name to cancel: ")
        system.cancel_event(event)
    elif choice == "5":
        print("👋 Exiting system...")
        break
    else:
        print("❌ Invalid choice. Try again.")
