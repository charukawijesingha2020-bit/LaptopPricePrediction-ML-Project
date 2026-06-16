# 💻 Laptop Price Prediction using Machine Learning

A machine learning project developed to predict laptop prices based on hardware specifications such as CPU, RAM, Storage, GPU, Screen Resolution, Operating System, and Brand.


## 📌 Project Overview

Laptop prices vary significantly depending on their specifications and intended usage. This project applies Machine Learning techniques to estimate laptop prices accurately using historical laptop data.

The project includes data preprocessing, feature engineering, exploratory data analysis (EDA), model training, evaluation, and comparison of multiple machine learning algorithms.

---

## 🎯 Objectives

- Clean and preprocess laptop specification data
- Perform exploratory data analysis (EDA)
- Engineer meaningful features
- Train and compare multiple machine learning models
- Evaluate model performance using standard regression metrics
- Analyze ethical considerations and bias in AI-based pricing systems

---

## 📊 Dataset

**Source:** Kaggle Laptop Price Dataset

### Features

| Feature | Description |
|-----------|-------------|
| Company | Laptop Brand |
| TypeName | Laptop Category |
| Inches | Screen Size |
| ScreenResolution | Display Resolution |
| CPU | Processor Details |
| RAM | Memory Capacity |
| Memory | HDD / SSD Storage |
| GPU | Graphics Processor |
| OpSys | Operating System |
| Price | Target Variable |

---

## ⚙️ Data Preprocessing

### Data Cleaning
- Removed unnecessary units from RAM and Weight
- Handled missing values
- Removed outliers using IQR method

### Feature Engineering
- Extracted CPU brand information
- Created Touchscreen feature
- Created IPS feature
- Calculated PPI (Pixels Per Inch)
- Extracted SSD and HDD capacities

### Encoding
- One-Hot Encoding
- Label Encoding

### Scaling
- StandardScaler
- MinMaxScaler

---

## 🤖 Machine Learning Models

### Regression Models

- Linear Regression
- Ridge Regression
- Lasso Regression
- Decision Tree Regressor
- Random Forest Regressor
- Support Vector Regression (SVR)
- Multi-Layer Perceptron (MLP)

### Clustering

- DBSCAN

### Classification

- Logistic Regression

---

## 📈 Evaluation Metrics

The following metrics were used to evaluate model performance:

- R² Score
- MAE (Mean Absolute Error)
- RMSE (Root Mean Squared Error)
- Accuracy
- Precision
- Recall
- F1 Score
- Silhouette Score
- Davies-Bouldin Score

---


## 🏆 Best Performing Model

| Model | R² Score |
|---------|---------|
| Tuned Random Forest | 0.8140 |

### Why Random Forest?

- Highest prediction accuracy
- Handles complex feature relationships
- Robust against overfitting
- Suitable for real-world datasets

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- TensorFlow / Keras
- Google Colab
---

## 📂 Project Structure

```text
Laptop-Price-Prediction-AI/
│
├── dataset/
│   ├── laptop_price.csv
│   └── preprocessed_laptopPrice.csv
│
├── notebooks/
│   ├── EDA.ipynb
│   ├── LinearRegression.ipynb
│   ├── DecisionTree.ipynb
│   ├── RandomForest.ipynb
│   ├── SVR.ipynb
│   └── MLP.ipynb
│
├── models/
│   └── trained_models
│
├── reports/
│   └── Final_Report.pdf
│
├── requirements.txt
└── README.md
