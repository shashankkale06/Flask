from flask import Flask, request, render_template, request
from datetime import datetime
import requests

BACKEND_URL = 'http://127.0.0.1:5000'

app = Flask(__name__)

@app.route('/')
def home():

    day_of_week = datetime.today().strftime('%A')
    current_time = datetime.now().strftime('%H:%M:%S')

    return render_template('index.html', day_of_week=day_of_week, current_time=current_time )

@app.route('/submit', methods=['POST'])
def submit():

    form_data = dict(request.form)
    requests.post(BACKEND_URL + '/submit', json=form_data)
    return 'Data submitted successfully!'

@app.route('/get_data')
def get_data():
    response = requests.get(BACKEND_URL + '/view')
    data =  response.json()
    data['hello']='world'
    return data

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=9000,debug=True)  