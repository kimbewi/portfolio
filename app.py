from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html') 


@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works', methods=['GET', 'POST'])
def works():
    return render_template('works.html')

@app.route('/to-upper-case', methods=['GET', 'POST'])
def touppercase():
    result = None
    if request.method == 'POST':
        input_string = request.form.get('inputString', '')
        result = input_string.upper()
    return render_template('touppercase.html', result=result)

@app.route('/area-of-circle', methods=['GET', 'POST'])
def areaOfcircle():
    result = None
    if request.method == 'POST':
        input_num = request.form.get('inputNum','')
        result = 3.14 * int(input_num) ** 2 
    return render_template('area-of-a-circle.html', result=result)

@app.route('/area-of-triangle', methods=['GET', 'POST'])
def areaOfTriangle():
    result = None
    if request.method == 'POST':
        input_Base = request.form.get('inputBase','')
        input_Height = request.form.get('inputHeight','')
        result = int(input_Base) * int(input_Height) / 2
    return render_template('area-of-triangle.html', result=result)
    

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
