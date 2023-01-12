from flask import Flask,render_template,request
import cloudpickle as cp
from urllib.request import urlopen

app=Flask(__name__)

model=cp.load(urlopen('https://raw.githubusercontent.com/steve-cse/Spam-Filtering-BN/master/SFBN.pkl'))
cv=cp.load(urlopen('https://raw.githubusercontent.com/steve-cse/Spam-Filtering-BN/master/vectorizer.pkl'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST','GET'])
def predict():
    new_email = request.form['email_input']
    new_features = cv.transform([new_email])
    prediction = model.predict(new_features)
    if prediction[0]==1:
        result="Spam Detected"
    else:
        result= "Ham Detected"
    return render_template('index.html', **locals())

if __name__=='__main__':
    app.run(debug=True)