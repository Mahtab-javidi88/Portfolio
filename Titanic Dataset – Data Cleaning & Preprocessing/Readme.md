# 🚢 Titanic Dataset – Data Cleaning & Preprocessing

Predicting survival on the Titanic using machine learning.

## 📌 Overview

This project is a comprehensive exploration of the Titanic dataset from Kaggle. Our goal is to predict which passengers survived the Titanic shipwreck. Along the way, we clean and explore the data, engineer features, build models, and interpret the results.

This notebook is not just about modeling – it's about storytelling, analysis, and understanding what features truly mattered for survival.

---

## 🧠 Problem Statement

> Can we predict survival on the Titanic using passenger characteristics?

We approach this binary classification problem using the Random Forest classifier as a baseline, and include room for future improvement with model tuning and explainable AI.

---

## 📁 Dataset

The dataset is sourced from the [Titanic - Machine Learning from Disaster](https://www.kaggle.com/c/titanic) competition on Kaggle. It includes:

- `train.csv` – labeled training data
- `test.csv` – test data for prediction
- `gender_submission.csv` – a sample submission format

---

## 🔍 Process

### 1. Exploratory Data Analysis (EDA)

- Survival distributions by class, sex, and age
- Missing value analysis
- Distribution visualizations

### 2. Feature Engineering

- Imputed missing age/fare values based on groups
- Encoded categorical variables (`Sex`, `Embarked`)
- Dropped uninformative or high-missing features (`Cabin`, `Ticket`)

### 3. Modeling

- Used RandomForestClassifier as the initial model
- Evaluated performance with accuracy and classification report
- Plotted feature importances

### 4. Submission

- Generated predictions on the test set
- Created a `submission.csv` ready for upload to Kaggle

---

## 📊 Model Performance

- **Model**: Random Forest Classifier
- **Validation Accuracy**: ~83%
- **Top Features**:
  - Sex
  - Age
  - Pclass

---

## 📌 Future Improvements

- Hyperparameter tuning using GridSearchCV or Optuna
- Try gradient boosting models (e.g. XGBoost, LightGBM)
- Use SHAP or LIME for explainability
- Build an interactive app with Streamlit

---

## 📂 Folder Structure

```bash
Titanic-Survival-Prediction/
├── Titanic_Notebook.ipynb
├── submission.csv
├── README.md
├── train.csv
├── test.csv
└── gender_submission.csv
