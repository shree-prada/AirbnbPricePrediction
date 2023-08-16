# AirbnbPricePrediction
# Airbnb Pricing Predictions

A Statistical Model to predict the optimal Airbnb Listing price in given listing information (e.g. bedrooms, type of bed, location, ratings) and taking into account seasonality data.

## Data Sources
http://insideairbnb.com/get-the-data/


## Technologies Used
- [Scikit learn](http://scikit-learn.org/stable)
- [Pandas](http://pandas.pydata.org/)
- [Numpy](http://www.numpy.org/)
- [Matplotlib](http://matplotlib.org/)
- [Seaborn](http://seaborn.pydata.org/)
- [Scipy](https://www.scipy.org/)
- Models
	+ Linear Regression
        + Elastic Net
        + Gradient Boosting REgression
        + Random Forest Classifier
        + Ridge

########################################
In order to run the code make sure you pre-instal all the dependecies such as LIME, Flask etc.

DOWNLOAD THE DATASET:

Create a directory called "Data", and download the datasets from this link into the directory:
https://drive.google.com/drive/folders/12TfxELKDHTCIpMYSbWPaMxTF8zhzRpAv?usp=drive_link

To run the project:
1. Run the file AirBnbFinalDemo_v8.ipynb
2. Specify the folder path where the CSV files are located
   path1 = "I:/class/Term2/BDM 3014/Project/CSVs/Batch1"
3. At last the code will generate a .pkl file
4. Run the app.py to view the UI
5. Access the webpage at http: //127.0.0.1:5000

Warning: certain models take a while to train and run!
