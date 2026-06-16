
import streamlit as st
import pandas as pd
import pickle

# Load Model
model = pickle.load(open("laptop_price_model_final.pkl", "rb"))

# Page Config
st.set_page_config(
    page_title="Laptop Price Predictor",
    page_icon="💻",
    layout="wide"
)

# Header
st.title("💻 Laptop Price Predictor")
st.markdown("### Machine Learning Based Laptop Price Prediction System")

st.info("Random Forest Regression Model")

# Layout
col1, col2 = st.columns(2)

with col1:

    company = st.selectbox(
        "Brand",
        [
            "Acer",
            "Apple",
            "Asus",
            "Dell",
            "HP",
            "Lenovo",
            "MSI",
            "Toshiba",
            "Other"
        ]
    )

    laptop_type = st.selectbox(
        "Laptop Type",
        [
            "Notebook",
            "Gaming",
            "Ultrabook",
            "2 in 1 Convertible",
            "Netbook",
            "Workstation"
        ]
    )

    os_name = st.selectbox(
        "Operating System",
        [
            "Windows",
            "Mac",
            "Linux",
            "Other"
        ]
    )

    cpu = st.selectbox(
        "Processor",
        [
            "Intel Core i3",
            "Intel Core i5",
            "Intel Core i7",
            "AMD",
            "Other"
        ]
    )

with col2:

    gpu = st.selectbox(
        "Graphics Card",
        [
            "Intel",
            "AMD",
            "Nvidia"
        ]
    )

    ram = st.slider(
        "RAM (GB)",
        2,
        64,
        8
    )

    screen_size = st.slider(
        "Screen Size (Inches)",
        10.0,
        20.0,
        15.6
    )

    weight = st.slider(
        "Weight (kg)",
        0.5,
        5.0,
        2.0
    )

    touchscreen = st.selectbox(
        "Touchscreen",
        ["No", "Yes"]
    )

    ips = st.selectbox(
        "IPS Display",
        ["No", "Yes"]
    )

# Prediction
if st.button("🔮 Predict Price"):

    data = {
        'Inches': screen_size,
        'Ram': ram,
        'Weight': weight,
        'Touchscreen': 1 if touchscreen == "Yes" else 0,
        'Ips': 1 if ips == "Yes" else 0,

        'Company_Acer': 0,
        'Company_Apple': 0,
        'Company_Asus': 0,
        'Company_Dell': 0,
        'Company_HP': 0,
        'Company_Lenovo': 0,
        'Company_MSI': 0,
        'Company_Other': 0,
        'Company_Toshiba': 0,

        'TypeName_2 in 1 Convertible': 0,
        'TypeName_Gaming': 0,
        'TypeName_Netbook': 0,
        'TypeName_Notebook': 0,
        'TypeName_Ultrabook': 0,
        'TypeName_Workstation': 0,

        'OpSys_Linux': 0,
        'OpSys_Mac': 0,
        'OpSys_Other': 0,
        'OpSys_Windows': 0,

        'cpu_name_AMD': 0,
        'cpu_name_Intel Core i3': 0,
        'cpu_name_Intel Core i5': 0,
        'cpu_name_Intel Core i7': 0,
        'cpu_name_Other': 0,

        'gpu_name_AMD': 0,
        'gpu_name_Intel': 0,
        'gpu_name_Nvidia': 0
    }

    data[f'Company_{company}'] = 1
    data[f'TypeName_{laptop_type}'] = 1
    data[f'OpSys_{os_name}'] = 1
    data[f'cpu_name_{cpu}'] = 1
    data[f'gpu_name_{gpu}'] = 1

    input_df = pd.DataFrame([data])

    prediction = float(model.predict(input_df)[0])

    st.markdown("---")

    st.metric(
        label="💰 Estimated Laptop Price (LKR)",
        value=f"Rs. {prediction:,.0f}"
    )

    st.success("Prediction completed successfully!")

# Footer
st.markdown("---")
st.caption(
    "Built using Python, Scikit-Learn, Random Forest Regressor and Streamlit"
)