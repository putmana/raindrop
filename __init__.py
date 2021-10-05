from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def search():
    return render_template('search.html', title="Word")

@app.route('/results')
def results():
    return render_template('results.html', title="Word")

if __name__ == "__main__":
    app.run()