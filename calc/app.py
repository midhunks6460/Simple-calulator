from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        expression = request.form['expression']
        result = str(eval(expression))
    except Exception as e:
        result = 'Error'

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
