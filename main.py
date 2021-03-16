from flask import Flask, render_template, request


app = Flask('ConvertNumber')
Flask.jinja_options = {'line_statement_prefix': '#'}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/decimal', methods=["GET", "POST"])
def decimal():
    if request.method == 'POST':
        in_decimal = request.form['number_in_decimal']
        in_binary = bin(int(in_decimal))[2:]
        in_hexa = hex(int(in_decimal))[2:]
        return render_template('decimal.html',
                               in_binary=in_binary,
                               in_decimal=in_decimal,
                               in_hexa=in_hexa.upper())
    return render_template('decimal.html')


@app.route('/binary', methods=["GET", "POST"])
def binary():
    if request.method == 'POST':
        in_binary = request.form['number_in_binary']
        in_decimal = int(in_binary, base=2)
        in_hexa = hex(in_decimal)[2:]
        return render_template('binary.html',
                               in_binary=in_binary,
                               in_decimal=in_decimal,
                               in_hexa=in_hexa.upper())
    return render_template('binary.html')


@app.route('/hexadecimal', methods=["GET", "POST"])
def hexadecimal():
    if request.method == 'POST':
        in_hexa = request.form['number_in_hexa']
        in_decimal = int(in_hexa, base=16)
        in_binary = bin(in_decimal)[2:]
        return render_template('hexadecimal.html',
                               in_binary=in_binary,
                               in_decimal=in_decimal,
                               in_hexa=in_hexa.upper())
    return render_template('hexadecimal.html')


if __name__ == '__main__':
    app.run()
