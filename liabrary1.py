borrow_records = [
    [2, 1, 0, 0, 3],  # Member 1
    [0, 0, 0, 0, 0],  # Member 2
    [1, 3, 2, 1, 0],  # Member 3
    [0, 0, 1, 0, 0],  # Member 4
]

num_members = len(borrow_records)
num_books = len(borrow_records[0])

# 1. Average number of books borrowed
total_borrowed = 0
for member in borrow_records:
    total_borrowed += sum(member)
average_borrowed = total_borrowed / num_members
print("Average books borrowed:", average_borrowed)

# 2. Book with highest and lowest borrowings
total_per_book = [0] * num_books
for j in range(num_books):
    for i in range(num_members):
        total_per_book[j] += borrow_records[i][j]

max_borrow = max(total_per_book)
min_borrow = min(total_per_book)
max_book = total_per_book.index(max_borrow) + 1
min_book = total_per_book.index(min_borrow) + 1
print(f"Book with highest borrowings: Book {max_book} ({max_borrow})")
print(f"Book with lowest borrowings: Book {min_book} ({min_borrow})")

# 3. Count members who have not borrowed any books
no_borrow_count = 0
for member in borrow_records:
    if sum(member) == 0:
        no_borrow_count += 1
print("Members who haven't borrowed any books:", no_borrow_count)

# 4. Most frequently borrowed book (mode)
freq_count = {}
for idx, total in enumerate(total_per_book):
    freq_count[total] = freq_count.get(total, 0) + 1

most_frequent_count = max(freq_count, key=freq_count.get)
most_frequent_books = [i + 1 for i, total in enumerate(total_per_book) if total == most_frequent_count]
print(f"Most frequently borrowed book(s): {most_frequent_books} ({most_frequent_count} times)")

