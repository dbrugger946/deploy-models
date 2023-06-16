import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
from pathlib import Path

pickle_path = '/model.pkl'
alt_pickle_path = 'model.pkl'

app = Flask(__name__)

default_path = Path(pickle_path)

if default_path.is_file():
    model = pickle.load(open(pickle_path, 'rb'))
else:
    model = pickle.load(open(alt_pickle_path, 'rb'))

# model = pickle.load(open('/model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():

    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Sales should be $ {}'.format(output))

@app.route('/results',methods=['POST'])
def results():

    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = round(prediction[0], 2)
    return jsonify(
        prediction=output*1.4,
        message="From Version 1.4")

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
