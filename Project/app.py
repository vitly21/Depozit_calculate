from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        principal = float(request.form['principal'])
        rate = float(request.form['rate']) / 100
        years = int(request.form['years'])
        frequency = int(request.form['frequency'])

        final_amount = principal * (1 + rate / frequency) ** (frequency * years)
        result = f"Итоговая сумма: {final_amount:.2f} руб."

    except:
        result = "Ошибка: Введите корректные числовые значения!"

    return render_template('index.html', result=result)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)