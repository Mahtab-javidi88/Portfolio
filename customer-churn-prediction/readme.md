# Customer Churn Prediction

## 📜 Project Overview

In this project, we predict customer churn for a telecommunications company based on historical customer data. The project includes multiple phases, such as data cleaning, feature engineering, machine learning model building, and evaluation. We utilize **Logistic Regression** and **Random Forest** models to predict churn rates and uncover significant factors contributing to customer retention.

## 🔧 Key Technologies Used:
- **Python** (Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn)
- **Machine Learning**: Logistic Regression, Random Forest Classifier
- **Data Cleaning & Feature Engineering**
- **Data Visualization**

## Objective:
The goal of this project is to predict whether a customer will leave (churn) or stay based on several attributes like account information, demographic features, and usage data. The model will help businesses identify customers at high risk of leaving and take proactive measures to retain them.

## Project Workflow:
1. **Data Collection**: The dataset was provided in CSV format, containing customer information.
2. **Data Preprocessing**: Cleaning and transforming the data (handling missing values, encoding categorical features).
3. **Exploratory Data Analysis (EDA)**: Visualizing data distributions and correlations.
4. **Model Building**: Logistic Regression and Random Forest to predict churn.
5. **Model Evaluation**: Evaluating performance using accuracy, precision, recall, confusion matrix, and ROC curve.

## Visualizations and Insights:

- **Churn Distribution**: The imbalance between churned vs non-churned customers.
- **Feature Importance**: Identifying which features (e.g., monthly charges, tenure) have the most influence on the churn prediction.
- **Model Evaluation**: Visual representation of confusion matrix and ROC curve for model performance.

## Results:

- **Best Model**: Random Forest Classifier with 90% accuracy.
    
## Key Findings:
- Tenure and Monthly Charges are the most influential features in predicting churn.
- Customers with high monthly charges are more likely to churn.
