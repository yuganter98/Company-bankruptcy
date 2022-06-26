from flask import Flask, render_template,request
import sklearn
from sklearn.linear_model import LogisticRegression
import pickle

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods = ['POST'])

def predict():

    if request.method =='POST':


        FF = request.form['FF']
        CR = request.form['CR']
        COM =request.form['COM']

        data = [[float(FF),float(CR),float(COM)]]

        lr = pickle.load(open('df.pkl','rb'))
        prediction = lr.predict(data)[0]
        final_pred= "Bankruptcy" if prediction==0 else "Non-Bankruptcy"
    return render_template('index.html',prediction=final_pred)    
    


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)