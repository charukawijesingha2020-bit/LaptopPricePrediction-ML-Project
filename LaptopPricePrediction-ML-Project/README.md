## Laptop Price Prediction System

📌 Overview of the Project

The aim of this project is to build a predictive model that can estimate the price of laptops based on their specifications and features. The dataset contains various attributes of laptops such as brand, processor, RAM, storage, GPU, and display features. By applying preprocessing techniques and feature engineering, we prepare the dataset for training machine learning models that predict laptop prices with high accuracy.

## The workflow involves:

    - Data preprocessing and cleaning
    - Handling missing values, encoding categorical variables, outlier removal
    - Normalization, scaling, dimensionality reduction, and feature selection
    - Building an integrated preprocessing pipeline
    - Preparing the dataset for machine learning model training

📊 Dataset Details

- Dataset Name: Laptop Price Dataset
- Source: Kaggle – Laptop Price Dataset
- Type: Tabular (structured)
- Location in Repo: data/raw/

👥 Group Members and Roles

| Name                   | IT Number  | Preprocessing Technique                                  |
| ---------------------- | ---------- | -------------------------------------------------------- |
| B.G.S.L. Liyanasooriya | IT24103186 | Feature Engineering: Dimensionality Reduction            |
| A.P.D.O.C. Wijesinghe  | IT24103639 | Encoding Categorical Variables                           |
| K.V.U. Jayananda       | IT24103206 | Encoding Categorical Variables                           |
| A.M.N. Aluthgoda       | IT24103132 | Handling Missing Data                                    |
| T.L.D. Sathsarani      | IT24103155 | Normalization / Scaling                                  |
| E.M.N.A. Ekanayake     | IT24100221 | Outlier Removal & Feature Engineering: Feature Selection |


⚙️ How to Run the Code

✅ Prerequisites

- Python 3.8+
- Install dependencies:pip install -r requirements.txt
- Required Libraries:
    - pandas
    - numpy
    - scikit-learn
    - matplotlib
    - seaborn
    - jupyter

🚀 Setup Instructions

1. Clone this repository

2. Navigate to the project directory

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

📓 Running the Notebooks

1. Launch Jupyter Notebook: jupyter notebook

   2. Navigate to the notebooks/ folder

      3. Run the member-wise preprocessing notebooks in order:

               IT24103132_Missing_value_handling.ipynb
               IT24103639_Encoding_categorical_variables.ipynb
               IT24103206_Encoding_categorical_variables.ipynb
               IT24100221_Outlier_removal.ipynb
               IT24100221_Feature_Selection.ipynb
               IT24103155_Normalization_Scaling.ipynb
               IT24103186_Dimensionality_Reduction.ipynb

       ** Finally, run group_pipeline.ipynb to integrate all preprocessing steps.**

📈 Results

    - EDA Visualizations: Available in results/eda_visualizations/
    - Final Processed Dataset: Stored in results/outputs/
    - Execution Logs (if available): Found in results/logs/