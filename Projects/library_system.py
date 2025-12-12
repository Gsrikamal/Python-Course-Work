"""
Library Management System
Save file: library_data.json
Run: python library_system.py
"""

import json
import os
from datetime import datetime

DATA_FILE = "library_data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"books": [], "issued": []}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def generate_book_id(data):
    existing = [b["id"] for b in data["books"]]
    new_id = 1
    while new_id in existing:
        new_id += 1
    return new_id

def add_book(data):
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    try:
        copies = int(input("Number of copies: ").strip())
    except ValueError:
        print("Invalid number for copies. Aborting add.")
        return
    book = {
        "id": generate_book_id(data),
        "title": title,
        "author": author,
        "total_copies": copies,
        "available_copies": copies
    }
    data["books"].append(book)
    save_data(data)
    print("Book added successfully:", book)

def list_books(data):
    if not data["books"]:
        print("No books in library.")
        return
    print("\nID | Title | Author | Available/Total")
    print("-"*50)
    for b in data["books"]:
        print(f"{b['id']} | {b['title']} | {b['author']} | {b['available_copies']}/{b['total_copies']}")
    print()

def search_books(data):
    q = input("Enter title or author to search: ").strip().lower()
    found = [b for b in data["books"] if q in b["title"].lower() or q in b["author"].lower()]
    if not found:
        print("No matching books.")
        return
    print("Matches:")
    for b in found:
        print(f"{b['id']} - {b['title']} by {b['author']} ({b['available_copies']}/{b['total_copies']})")

def find_book_by_id(data, book_id):
    for b in data["books"]:
        if b["id"] == book_id:
            return b
    return None

def issue_book(data):
    try:
        book_id = int(input("Book ID to issue: ").strip())
    except ValueError:
        print("Invalid ID.")
        return
    book = find_book_by_id(data, book_id)
    if not book:
        print("Book not found.")
        return
    if book["available_copies"] <= 0:
        print("No copies available to issue.")
        return
    student = input("Student name: ").strip()
    issue_date = datetime.now().strftime("%Y-%m-%d")
    record = {"book_id": book_id, "student": student, "issue_date": issue_date}
    data["issued"].append(record)
    book["available_copies"] -= 1
    save_data(data)
    print(f"Issued '{book['title']}' to {student} on {issue_date}.")

def return_book(data):
    try:
        book_id = int(input("Book ID to return: ").strip())
    except ValueError:
        print("Invalid ID.")
        return
    student = input("Student name (as on issue record): ").strip()
    # find matching issued record
    for i, rec in enumerate(data["issued"]):
        if rec["book_id"] == book_id and rec["student"].lower() == student.lower():
            data["issued"].pop(i)
            book = find_book_by_id(data, book_id)
            if book:
                book["available_copies"] += 1
            save_data(data)
            print(f"Book ID {book_id} returned by {student}.")
            return
    print("No matching issued record found.")

def list_issued(data):
    if not data["issued"]:
        print("No books are currently issued.")
        return
    print("\nIssued Records:")
    for rec in data["issued"]:
        book = find_book_by_id(data, rec["book_id"])
        title = book["title"] if book else "Unknown"
        print(f"{rec['book_id']} - {title} | Student: {rec['student']} | Date: {rec['issue_date']}")
    print()

def main():
    data = load_data()
    while True:
        print("\n--- Library Menu ---")
        print("1. Add Book")
        print("2. List Books")
        print("3. Search Books")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. List Issued Books")
        print("7. Exit")
        choice = input("Choice: ").strip()
        if choice == "1":
            add_book(data)
        elif choice == "2":
            list_books(data)
        elif choice == "3":
            search_books(data)
        elif choice == "4":
            issue_book(data)
        elif choice == "5":
            return_book(data)
        elif choice == "6":
            list_issued(data)
        elif choice == "7":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
