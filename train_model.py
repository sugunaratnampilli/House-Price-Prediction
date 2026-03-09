import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
import os

# Load dataset
data = pd.read_csv("data/housing.csv")

# Convert yes/no columns to 1 and 0
binary_columns = [
    "mainroad",
    "guestroom",
    "basement",
    "hotwaterheating",
    "airconditioning",
    "prefarea"
]

for col in binary_columns:
    data[col] = data[col].map({"yes":1, "no":0})

# Convert furnishingstatus to numbers
data["furnishingstatus"] = data["furnishingstatus"].map({
    "furnished":2,
    "semi-furnished":1,
    "unfurnished":0
})

# Features and target
X = data.drop("price", axis=1)
y = data["price"]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Create models folder if not exists
os.makedirs("models", exist_ok=True)

# Save model
joblib.dump(model, "models/model.pkl")

print("Model trained successfully!")