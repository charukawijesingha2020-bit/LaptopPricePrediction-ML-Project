# 💻 Laptop Price Prediction System

A Machine Learning-powered web application that predicts laptop prices in Sri Lankan Rupees (LKR) based on hardware specifications such as processor, RAM, graphics card, operating system, screen size, and laptop type.

Built using **Python, Scikit-Learn, Random Forest Regression, and Streamlit**.

---

## 🚀 Live Features

* Predict laptop prices instantly
* Interactive Streamlit web interface
* Real-time price estimation in LKR
* Machine Learning-based predictions
* User-friendly design
* Supports multiple laptop brands and configurations

---

## 📸 Application Preview

### Input Parameters

* Laptop Brand
* Laptop Type
* Operating System
* Processor
* Graphics Card
* RAM
* Screen Size
* Weight
* Touchscreen Support
* IPS Display Support

### Output

```text
Estimated Laptop Price (LKR)

Rs. 425,000
```

---

## 📊 Dataset

Source: Kaggle Laptop Price Dataset

The dataset contains laptop specifications including:

* Company
* TypeName
* Inches
* Screen Resolution
* CPU
* RAM
* Storage
* GPU
* Operating System
* Price

Original prices in Euros were converted to Sri Lankan Rupees (LKR) during preprocessing.

---

## ⚙️ Data Preprocessing

### Data Cleaning

* Removed irrelevant features
* Removed Laptop ID column
* Handled missing values
* Removed outliers using IQR

### Feature Engineering

* Extracted CPU categories
* Extracted GPU categories
* Created Touchscreen feature
* Created IPS feature
* Simplified Operating System categories
* Grouped rare laptop brands into "Other"

### Encoding

One-Hot Encoding applied to:

* Company
* TypeName
* Operating System
* CPU Category
* GPU Category

### Scaling

* MinMaxScaler

---

 
