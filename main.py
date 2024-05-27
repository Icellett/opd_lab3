import math
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/paral")
def paral():
    return render_template('paral.html')

@app.route("/sphere")
def sphere():
    return render_template('sphere.html')

@app.route("/cone")
def cone():
    return render_template('cone.html')

@app.route("/cylinder")
def cylinder():
    return render_template('cylinder.html')
@app.route('/', methods=['post', 'get'])
def toPage():
    button_index = int(request.form['button_index'])
    if button_index == 0:
        return redirect(url_for("paral"), 301)
    elif button_index == 1:
        return redirect(url_for("sphere"), 301)
    elif button_index == 2:
        return redirect(url_for("cone"), 301)
    elif button_index == 3:
        return redirect(url_for("cylinder"), 301)

@app.route('/paral', methods=['post', 'get'])
def paralVolume():
    num_1 = int(request.form.get('num_1'))
    num_2 = int(request.form.get('num_2'))
    num_3 = int(request.form.get('num_3'))
    e = int(request.form.get('e'))
    res = round((num_1*num_2*num_3), e)
    return render_template('paral.html', res=res)

@app.route('/sphere', methods=['post', 'get'])
def sphereVolume():
    num_1 = int(request.form.get('num_1'))
    e = int(request.form.get('e'))
    res = round((4 / 3) * math.pi * (num_1 ** 3), e)
    return render_template('sphere.html', res=res)

@app.route('/cone', methods=['post', 'get'])
def coneVolume():
    num_1 = int(request.form.get('num_1'))
    num_2 = int(request.form.get('num_2'))
    e = int(request.form.get('e'))
    res = round((1 / 3) * math.pi * (num_1 ** 2), e)
    return render_template('cone.html', res=res)

@app.route('/cylinder', methods=['post', 'get'])
def cylinderVolume():
    num_1 = int(request.form.get('num_1'))
    num_2 = int(request.form.get('num_2'))
    e = int(request.form.get('e'))
    res = round(math.pi * (num_1 ** 2), e)
    return render_template('cylinder.html', res=res)

if __name__ == "__main__":
    app.run(debug=True)