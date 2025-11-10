import csv

book_status = "data/student_books_in_out.csv"

def get_status(row):
    """Helper function to check for a true or false entry for books which are checked out"""
    if row["Check Out"] == "True":
        return "Out"
    else:
        return "In"

def all_books_status():
    """Function to get all books and only return those which are checked out on the dashboard"""
    books = []
    with open(book_status, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            #key = (row["Title"], row["Student"])
            status = get_status(row)
            books.append({
                "title":row["Title"],
                "author": row["Author"],
                "student": row["Student"],
                "dtg": row["DTG"],
                "status": status
            })
    return [book for book in books if book["status"] == "Out"]