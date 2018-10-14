from flask import Flask, render_template, request
from util import testing2, math, number
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api')
def api():
    problem = request.args.get("problem")
    return math.solve(problem)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
