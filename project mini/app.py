
from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('songspopularity.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods = ['GET', 'POST'])
def predict():

    int_features = [x for x in request.form.values()]
    final_features = [np.array(int_features)]
    for feature in final_features:
        print(feature)
    prediction = model.predict(final_features)

    output = prediction[0]

    if output == 0:
        return render_template('output.html', prediction_text='IT WILL NOT FEATURE ON BILIBOARD TOP 100')
    else:
        return render_template('output.html', prediction_text='IT WILL FEATURE ON BILIBOARD TOP 100')


if __name__ == "__main__":
    app.run(debug=True)