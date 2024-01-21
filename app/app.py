from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__, template_folder= 'templates')


@app.route('/')
def index():
        return render_template('index.html')

@app.route('/about')
def about():
        return render_template('about.html')
@app.route('/contact')
def contact():
        return render_template('contact.html')


@app.route('/companion')
def companion():
        return render_template('companion.html')

@app.route('/stats')
def stats():
        return render_template('stats.html')

@app.route('/workout')
def workout():
        return render_template('workout.html')




if __name__ == '__main__':
        app.run(debug=True)