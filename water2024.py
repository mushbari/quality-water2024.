import streamlit as st
import pandas as pd
import pickle
import os
import numpy as np

# Load the data
data_path = "water.csv"  # Update the path to the correct location
df = pd.read_csv(data_path)

# Load the trained model
model_path ="RandomForestClassifier_model1.sav"  # Update the path to the correct location
def load_model():
    try:
        if os.path.exists(model_path):
            with open(model_path, 'rb') as file:
                model = pickle.load(file)
            print("Model loaded successfully!")
            return model
        else:
            print(f"Model file not found at: {model_path}")
            return None
    except Exception as e:
        print(f"Error loading the model: {e}")
        return None

def main():
    st.title("Water quality prediction Web App")
    st.info('Easy Application For Water quality prediction Diseases')
    
    model = load_model()

    st.sidebar.write("")
    st.sidebar.header("Feature Selection")

    ph = st.text_input("ph")
    Hardness = st.text_input("Hardness")
    Solids = st.text_input("Solids")
    Chloramines = st.text_input("Chloramines")
    Sulfate = st.text_input("Sulfate")
    Conductivity = st.text_input("Conductivity")
    Organic_carbon = st.text_input("Organic_carbon")
    Trihalomethanes = st.text_input("Trihalomethanes")
    Turbidity = st.text_input("Turbidity")

    data = {
        'ph': [float(ph) if ph else np.nan],
        'Hardness': [float(Hardness) if Hardness else np.nan],
        'Solids': [float(Solids) if Solids else np.nan],
        'Chloramines': [float(Chloramines) if Chloramines else np.nan],
        'Sulfate': [float(Sulfate) if Sulfate else np.nan],
        'Conductivity': [float(Conductivity) if Conductivity else np.nan],
        'Organic_carbon': [float(Organic_carbon) if Organic_carbon else np.nan],
        'Trihalomethanes': [float(Trihalomethanes) if Trihalomethanes else np.nan],
        'Turbidity': [float(Turbidity) if Turbidity else np.nan]
    }
    input_df = pd.DataFrame(data)

    # Check if the inputs are valid before predicting
    if input_df.isnull().values.any():
        st.write('Please fill in all the fields.')
    else:
        # Create a button to execute the prediction
        if st.button('Predict Potability'):
            if model is not None:
                # Handle missing values
                input_df = input_df.fillna(input_df.mean())
                prediction = model.predict(input_df)
                if prediction[0] == 0:
                    st.write('The water is not potable.')
                else:
                    st.write('The water is potable.')

if __name__ == "__main__":
    main()
