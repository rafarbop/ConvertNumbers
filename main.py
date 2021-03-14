from flask import Flask, render_template

app = Flask('ConvertNumber')
Flask.jinja_options = {'line_statement_prefix': '#'}


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/decimal')
def decimal():
    return render_template('decimal.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
