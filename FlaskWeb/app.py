from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/about.html')
def about_us():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
