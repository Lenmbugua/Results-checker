from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

# Build URL dynamically
@app.route('/success/<int:score>')
def success(score):
    res = 'PASS' if score >= 50 else 'FAIL'
    exp = {'score': score, 'res': res}
    return render_template('results.html', result=exp)

@app.route('/fail/<int:score>')
def fail(score):
    # Changed to pass a dictionary like in the success route
    exp = {'score': score, 'res': 'FAIL'}
    return render_template('results.html', result=exp)

# Results checker
@app.route('/results/<int:score>')
def results(score):
    result = 'success' if score >= 50 else 'fail'
    return redirect(url_for(result, score=score))

### Result checker HTML
@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])
        total_score = (science + maths + c + datascience) / 4
    res = "success" if total_score >= 50 else "fail"
    return redirect(url_for(res, score=total_score))

if __name__ == '__main__':
    app.run(debug=True)
