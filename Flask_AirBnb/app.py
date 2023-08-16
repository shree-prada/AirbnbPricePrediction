import pickle
from sklearn.preprocessing import StandardScaler
from flask import Flask,render_template,request,url_for, jsonify

model = pickle.load(open('fore.pkl','rb'))
app = Flask(__name__,static_url_path='/static')

def predict_price(input_data):
     #Extract features from input data
     features = [input_data['host_listings_count'],
                 input_data['host_total_listings_count'],
                 input_data['accommodates'],
                 input_data['bedrooms'],
                 input_data['beds'],
                 input_data['review_scores_location'],
                 input_data['calculated_host_listings_count'],
                 input_data['calculated_host_listings_count_entire_homes'],
                 input_data['calculated_host_listings_count_private_rooms']
                 ]
    #Predict the price using the loaded model
    predicted_price = model.predict([features])[0]
    return f"${predicted_price:.2f}"
    



@app.route('/')
def first():
    return render_template("first.html")
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get user input from the form
    host_listings_count = int(request.form['host_listings_count'])
    host_total_listings_count = int(request.form['host_total_listings_count'])
    accommodates = int(request.form['accommodates'])
    bedrooms = int(request.form['bedrooms'])
    beds = int(request.form['beds'])
    review_scores_location = int(request.form['review_scores_location'])
    calculated_host_listings_count = int(request.form['calculated_host_listings_count'])
    calculated_host_listings_count_entire_homes = int(request.form['calculated_host_listings_count_entire_homes'])
    calculated_host_listings_count_private_rooms = int(request.form['calculated_host_listings_count_private_rooms'])

    # Prepare input data for prediction
    input_data = {
        'host_listings_count':host_listings_count,
        'host_total_listings_count':host_total_listings_count,
        'accommodates': accommodates,
        'bedrooms': bedrooms,
        'beds':beds,
        'review_scores_location':review_scores_location,
        'calculated_host_listings_count':calculated_host_listings_count,
        'calculated_host_listings_count_entire_homes':calculated_host_listings_count_entire_homes,
        'calculated_host_listings_count_private_rooms':calculated_host_listings_count_private_rooms
    }

    # Get the price prediction
    predicted_price = predict_price(input_data)

    return render_template('index.html', prediction=predicted_price)

if __name__ == '__main__':
    app.run(debug=True)
