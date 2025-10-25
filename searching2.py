def linear_search(account_list, target):
    for acc in account_list:
        if acc == target:
            return True
    return False

def binary_search(account_list, target):
    low = 0
    high = len(account_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if account_list[mid] == target:
            return True
        elif account_list[mid] < target:
            low = mid + 1
        else:

            high = mid - 1
    return False

accounts = [101, 103, 107, 109, 112, 115, 118, 121, 125]

print("Customer Accounts:", accounts)

target = int(input("Enter account ID to search: "))

# Linear Search
if linear_search(accounts, target):
    print("✅ Account found using Linear Search")
else:
    print("❌ Account not found using Linear Search")

# Binary Search (list must be sorted)
if binary_search(accounts, target):
    print("✅ Account found using Binary Search")
else:
    print("❌ Account not found using Binary Search")
