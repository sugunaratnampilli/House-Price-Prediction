from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("models/model.pkl")

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():

    area = float(request.form['area'])
    bedrooms = float(request.form['bedrooms'])
    bathrooms = float(request.form['bathrooms'])
    stories = float(request.form['stories'])
    parking = float(request.form['parking'])

    mainroad = int(request.form['mainroad'])
    guestroom = int(request.form['guestroom'])
    basement = int(request.form['basement'])
    hotwaterheating = int(request.form['hotwaterheating'])
    airconditioning = int(request.form['airconditioning'])
    prefarea = int(request.form['prefarea'])
    furnishingstatus = int(request.form['furnishingstatus'])

    features = [[area, bedrooms, bathrooms, stories,
                 mainroad, guestroom, basement,
                 hotwaterheating, airconditioning,
                 parking, prefarea, furnishingstatus]]

    prediction = model.predict(features)

    return render_template(
        "index.html",
        prediction_text=f"Estimated Price: ₹{prediction[0]:,.2f}"
    )

if __name__ == "__main__":
    app.run(debug=True)