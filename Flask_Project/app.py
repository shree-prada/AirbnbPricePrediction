import pickle
from sklearn.preprocessing import StandardScaler
from flask import Flask,render_template,request,url_for, jsonify

model = pickle.load(open('fore.pkl','rb'))
app = Flask(__name__,static_url_path='/static')

def predict_price(input_data):
    # # Extract features from input data
    # features = [
    #     input_data['accommodates'],
    #     input_data['bedrooms'],
    #     input_data['bathrooms'],
    #     input_data['room_type'] == 'Entire home/apt',
    #     input_data['room_type'] == 'Private room',
    #     input_data['room_type'] == 'Shared room'
    # ]

    # # Predict the price using the loaded model
    # predicted_price = model.predict([features])[0]
    # return f"${predicted_price:.2f}"

    return "$200"

@app.route('/')
def first():
    return render_template("first.html")
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Get user input from the form
    accommodates = int(request.form['accommodates'])
    bedrooms = int(request.form['bedrooms'])
    bathrooms = int(request.form['bathrooms'])
    room_type = request.form['room_type']
    neighborhood = request.form['neighborhood']

    # Prepare input data for prediction
    input_data = {
        'accommodates': accommodates,
        'bedrooms': bedrooms,
        'bathrooms': bathrooms,
        'room_type': room_type,
        'neighborhood': neighborhood
    }

    # Get the price prediction
    predicted_price = predict_price(input_data)

    return render_template('index.html', prediction=predicted_price)

if __name__ == '__main__':
    app.run(debug=True)