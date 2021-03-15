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
        in_binary = bin(int(request.form['number_in_decimal']))[2:]
        in_hexa = hex(int(request.form['number_in_decimal']))[2:]
        return render_template('decimal.html',
                               in_binary=in_binary,
                               in_decimal=in_decimal,
                               in_hexa=in_hexa)
    return render_template('decimal.html')


@app.route('/binary')
def binary():
    return render_template('binary.html')


@app.route('/hexadecimal')
def hexadecimal():
    return render_template('hexadecimal.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
