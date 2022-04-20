from flask import Flask,render_template,request
import pickle
import numpy as np

app= Flask(__name__)
model = pickle.load(open('pickle.sav','rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods = ['POST','GET'])
def predict():
    numbers = [float(x) for x in request.form.values()]
    array = [np.array(numbers)]
    prediction = model.predict(array)[0]
    return render_template("index.html", Answer = prediction)

if (__name__)== '__main__':
    app.run(debug = True)
