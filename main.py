from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return f"<html><body><h1>The result is passed with a score of {score}</h1></body></html>"

@app.route('/fail/<int:score>')
def fail(score):
    return f"The person has failed, and the marks are {score}"

# This route will handle the form submission
@app.route('/submit', methods=['POST'])
def submit():
    # Extract data from form fields
    science = int(request.form['science'])
    maths = int(request.form['maths'])
    c = int(request.form['c'])
    datascience = int(request.form['datascience'])

    # Calculate total score
    total_score = (science + maths + c + datascience) / 4

    # Redirect based on score
    if total_score >= 50:
        return redirect(url_for('success', score=total_score))
    else:
        return redirect(url_for('fail', score=total_score))

if __name__ == '__main__':
    app.run(debug=True)

