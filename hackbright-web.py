from flask import Flask, request, render_template, redirect

import hackbright

app = Flask(__name__)


@app.route("/student")
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    return render_template("student_info.html",
                            first=first,
                            last=last,
                            github=github)


@app.route("/student-search")
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")


@app.route("/student-form")
def get_add_form():
    """Show form for adding a student."""

    return render_template("student_add.html")


@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""

    github = request.form.get('github', 'jhacks')
    first = request.form.get('firstname', 'Jane')
    last = request.form.get('lastname', 'Hacker')
    hackbright.make_new_student(first, last, github)
    return render_template("student_added.html", 
                            first=first,
                            last=last,
                            github=github)
                  
   

if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
