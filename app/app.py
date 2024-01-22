from flask import Flask, render_template, request, send_from_directory
import os
import sys
import urllib.parse


#adding folder to file path
sys.path.insert(1, 'C:\\Coding\\Github\\bodyBuild_Companion')
from scripts.dallie3 import imgGen
import scripts.user_info as info

app = Flask(__name__, template_folder= 'templates', static_folder='static')

def generatePhoto(input):
    photo_path = imgGen(input,info.PAT, info.USER_ID, info.APP_ID )

    print ("this is the photo path")
    print(photo_path)
    return photo_path





@app.route('/')
def index():
        return render_template('index.html')

@app.route('/generatedImages/<filename>')
def generatedImages(filename):
    return send_from_directory('images', filename)


@app.route('/generate', methods=['POST'])
def generate():
    input_data = request.form.get('input_data')
    generated_photo = generatePhoto(input_data)
    modified_input_data = input_data + '.jpg'
    return render_template('companion.html', generated_photo=modified_input_data)


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