from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def raindrop():
    return render_template('hello.html', title="Word")

if __name__ == "__main__":
    app.run()