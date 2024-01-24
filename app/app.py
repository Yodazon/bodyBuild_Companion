from flask import Flask, render_template, request, send_from_directory
import os
import sys
import urllib.parse


#adding folder to file path
sys.path.insert(1, 'C:\\Coding\\Github\\bodyBuild_Companion')
from scripts.dallie3 import imgGen
import scripts.user_info as info
import scripts.statistics as stat
from scripts.workoutPlan import workoutGen

app = Flask(__name__, template_folder= 'templates', static_folder='static')

def generatePhoto(input):
        photo_path = imgGen(input,info.PAT, info.USER_ID, info.APP_ID )
        return photo_path

def generateWorkout(input):
        workout_path = workoutGen(input,info.PAT, info.USER_ID, info.APP_ID )
        print ("this is the workout path")
        print(workout_path)
        return workout_path





@app.route('/')
def index():
        return render_template('index.html')


#
# To generate photo companion
#
@app.route('/generatedImages/<filename>')
def generatedImages(filename):
    print (f"The filname is {filename}")
    return send_from_directory('generatedImages', filename)


@app.route('/generatePhoto', methods=['POST'])
def generatePhoto():
    input_data = request.form.get('input_data')
    generatePhoto(input_data)
    modified_input_data = input_data + '.jpg'
    return render_template('companion.html', generated_photo=modified_input_data)


#
# To generate workoutplan
#

@app.route('/generatedWorkout/<filename>')
def generatedWorkout (filename):
    print (f"The filname is {filename}")
    return send_from_directory('generatedWorkout', filename)


@app.route('/generateWorkout', methods=['POST'])
def generateWorkout():
    input_data = request.form.get('input_data')
    generateWorkout(input_data)
    modified_input_data = input_data + '.jpg'
    return render_template('workout.html', generated_photo=modified_input_data)





#
# To generate Stats
#
@app.route('/generatedStats/<filename>')
def generatedStats(filename):
    print (f"The filname is {filename}")
    return send_from_directory('generatedStats', filename)

@app.route('/postStats', methods = ['POST'])
def postStats():
        selected_button = request.form.get('stat_clicked')

        print (f'The selected stat is {selected_button}')
        stat_to_be_shown = None
        if selected_button == 'activity':
                stat_to_be_shown = stat.plotStat(0)
                pass

        elif selected_button == 'sleep':
                stat_to_be_shown = stat.plotStat(1)
                pass

        elif selected_button == 'weight':
                stat_to_be_shown = stat.plotStat(2)
                pass

        else:
                #suck my balls Mr Garrison
                pass
        
        print(stat_to_be_shown)
        return render_template('stats.html', generated_stats = 'figure.jpg')




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