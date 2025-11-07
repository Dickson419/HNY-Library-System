import csv, os, datetime
from flask import Flask, render_template, request

app = Flask(__name__)

book_data = "data/student_books_in_out.csv"

#render the template to view the content page - see the index.html!
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    student = request.form.get("Student")
    title = request.form.get("Book-title")
    take_out = request.form.get("Take-out")
    return_book = request.form.get("Return")

    #convert the on/off from checkboxes to be boolean values
    #take_out = bool(request.form.get("Take-out"))
    #return_book = bool(request.form.get("Return"))

    #check if file exists
    file_exists = os.path.isfile(book_data)

    #write this information to a csv file
    with open(book_data, 'a', newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["DTG", "Student", "Title", "Check Out", "Return"])

        writer.writerow([datetime.datetime.now().strftime("%m/%d/%Y/%H%M"), student.title(), title.title(), bool(take_out), bool(return_book)])

    return render_template("index.html", message="Entry Saved!")


if __name__ == "__main__":
    app.run(debug=True)


