import pickle
from sklearn.preprocessing import StandardScaler
from flask import Flask,render_template,request,url_for, jsonify

model=pickle.load(open('fore.pkl','rb'))
app=Flask(__name__,static_url_path='/static')

@app.route('/')

#first page
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])

def predict():
    data = request.json 
    prediction = model.predict([data['features']])
    return jsonify({'prediction': prediction.tolist()})

if __name__=='__main__':
    app.run(debug=True)