# 🧠 Mental Tiredness Score Prediction

A machine learning project that predicts a person's mental tiredness score based on daily work activity, lifestyle, sleep, workload and environmental factors.

## 🚀 Live Demo

🔗 Streamlit App: https://mental-tiredness-score-predict-ml-project.streamlit.app

---

## 📌 Project Overview

Mental tiredness can be influenced by several factors such as workload, screen time, number of decisions made, task switching, sleep, hydration, caffeine intake and environmental conditions.

This project uses machine learning to predict a continuous Mental Tiredness Score from these factors.

The project was developed using Python and several regression algorithms, with XGBoost selected as the final model based on its evaluation performance.

---

## 🎯 Objective

The main objective of this project is to:

- Predict mental tiredness score using machine learning.
- Identify important factors associated with mental tiredness.
- Compare different regression models.
- Select the best-performing model based on evaluation metrics.
- Deploy the final model using Streamlit.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Matplotlib
- Streamlit
- Jupyter Notebook
- GitHub

---

## 📊 Features Used

The model uses the following features:

- Number of Decisions Made
- Context Switch Count
- Notifications Received
- Screen Time
- Deep Work Time
- Average Task Complexity
- Caffeine Intake
- Break Frequency
- Deep Sleep Percentage
- Hydration
- Mood
- Work Type
- Noise Level
- Workload Score
- Deep Sleep Hours
- Interruption Load

---

## 🤖 Machine Learning Models

Several regression algorithms were evaluated:

- Linear Regression
- Ridge Regression
- Decision Tree
- Random Forest
- K-Nearest Neighbors (KNN)
- Support Vector Regression (SVR)
- XGBoost

---

## 📈 Model Evaluation

The models were evaluated using:

- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)
- R² Score
- MSE (Mean Squared Error)

### Model Comparison

| Model | RMSE | MAE | R² Score | MSE |
|---|---:|---:|---:|---:|
| XGBoost | 6.1653 | 4.9232 | 0.7449 | 38.0106 |
| SVR | 6.1961 | 4.9295 | 0.7424 | 38.3912 |
| Ridge | 6.6082 | 5.3015 | 0.7070 | 43.6680 |
| Linear Regression | 6.6084 | 5.3017 | 0.7069 | 43.6707 |
| Random Forest | 7.2746 | 5.8242 | 0.6449 | 52.9192 |
| KNN | 7.9405 | 6.3223 | 0.5769 | 63.0521 |
| Decision Tree | 9.3956 | 7.5221 | 0.4077 | 88.2751 |

### 🏆 Selected Model

XGBoost was selected as the final model because it achieved the lowest RMSE and MSE among the evaluated models while also achieving the highest R² score.

### Final XGBoost Performance

- RMSE: **6.1653**
- MAE: **4.9232**
- R² Score: **0.7449**
- MSE: **38.0106**

---

## 📊 Model Visualization

### Actual vs Predicted

The Actual vs Predicted plot shows how closely the predicted mental tiredness scores follow the actual scores.

![Actual vs Predicted](Screenshots/Actual vs Predicted.png)
Screenshots/Actual vs Predicted.png


### Residual Plot

The residual plot helps examine the prediction errors of the XGBoost model.

![Residual Plot](Screenshots/residual_plot.png)

---

## 🌐 Streamlit Application

The trained XGBoost model was deployed using Streamlit.

Users can enter:

- Daily work activity
- Screen time
- Deep work duration
- Sleep information
- Mood
- Workload
- Hydration
- Caffeine intake
- Work environment

The application then predicts the expected Mental Tiredness Score.

---

## 📂 Project Structure

```text
Mental-Tiredness-Score-Prediction/
│
├── app.py
├── model_pipe.pkl
├── requirements.txt
├── README.md
├── mental_tiredness_prediction.ipynb
├── .gitignore
│
└── screenshots/
    ├── home_page.png
    ├── prediction_result.png
    ├── actual_vs_predicted.png
    └── residual_plot.png
