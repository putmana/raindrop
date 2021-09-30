from flask import Flask, render_template
import api_fetch as api
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html', title="Word")

@app.route('/api', methods=['GET'])
def api_fetch():
    return api.json_test()

if __name__ == "__main__":
    app.run()