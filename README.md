# Delivery-time-prediction
This project is a machine learning model designed to predict the estimated delivery time for food orders based on multiple real-world factors such as distance, traffic, weather, order type, and more. It aims to help restaurants, delivery services, and customers get a more accurate expectation of when their food will arrive.
# ■ Food Delivery Time Prediction
**Predict accurate food delivery times based on real-world factors like distance, weather, traffic, and
order details.**
This project combines **machine learning** with a simple **Streamlit web app** to provide quick,
real-time predictions.
## ■ Features
- ■ Data Preprocessing – Handles missing values, encodes categorical data, and scales numeric
features
- ■ Feature Engineering – Calculates delivery distances and extracts important predictors
- ■ Machine Learning Model – Uses Random Forest Regressor for robust predictions
- ■ Performance Evaluation – MAE, RMSE, and R² score for model accuracy
- ■ Streamlit Web App – Interactive interface for making predictions
- ■ Model Persistence – Trained model saved via joblib for reuse without retraining
## ■ Dataset Overview
The dataset contains features like:
- Delivery_person_Ratings
- distance_km
- Weatherconditions
- Road_traffic_density
- Type_of_order
- Festival
- City
- multiple_deliveries
- Time_taken(min) (Target)
## ■ Tech Stack
- Python 3.x
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Streamlit
- Joblib
## ■■ Project Workflow
1. Load & Explore Data
2. Data Cleaning – Handle missing values & incorrect data types
3. Feature Engineering – Calculate distances & encode categories
4. Model Training – Train Random Forest model
5. Evaluation – Compare predictions to actual delivery times
6. Deployment – Build and run Streamlit app
## ■ Running the App
```bash
git clone https://github.com/yourusername/food-delivery-time-prediction.git
cd food-delivery-time-prediction
pip install -r requirements.txt
streamlit run app.py
```
## ■ Future Enhancements
- Live GPS-based distance calculation
- Integration with live traffic & weather APIs
- Try Gradient Boosting, XGBoost, and LightGBM

