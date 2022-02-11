from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', cols = 8, rows = 8)

@app.route('/4')
def eight_by_four():
    return render_template('index.html', cols = 8, rows = 4)

@app.route('/<int:x>')
def by_x(x):
    return render_template('index.html', cols = 1, rows = x)

@app.route('/<int:x>/<int:y>')
def x_by_y(x, y):
    return render_template('index.html', cols = x, rows = y)

@app.route('/<int:x>/<int:y>/<string:color1>/<string:color2>')
def dims_and_colors(color1, color2, x, y):
    return render_template('index.html', color1 = color1, color2 = color2, cols = x, rows = y)

if __name__ == '__main__':
    app.run(debug=True)
