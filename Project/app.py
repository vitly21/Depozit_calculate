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