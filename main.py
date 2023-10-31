import streamlit as st

# HACOR calculation function
def hacor_score(heart_rate, pH, GCS, PaO2_FiO2, respiration_rate):
    # Scoring system for each parameter (this is a mock scoring, the real system may vary)
    score = 0
    
    # Heart rate
    if 70 <= heart_rate <= 109:
        score += 0
    elif 110 <= heart_rate <= 119:
        score += 2
    else:
        score += 4
    
    # Acidosis
    if pH > 7.35:
        score += 0
    else:
        score += 4
    
    # Consciousness
    if GCS == 15:
        score += 0
    elif 9 <= GCS <= 14:
        score += 1
    else:
        score += 5

    # Oxygenation
    if PaO2_FiO2 > 200:
        score += 0
    elif 150 <= PaO2_FiO2 <= 200:
        score += 2
    else:
        score += 4

    # Respiration rate
    if 12 <= respiration_rate <= 23:
        score += 0
    elif 24 <= respiration_rate <= 30:
        score += 1
    else:
        score += 2
    
    return score

st.title('HACOR Score Calculator')
st.write('This tool calculates the HACOR Score to predict the failure of noninvasive ventilation (NIV) in hypoxemic patients.')

# Input values
heart_rate = st.number_input('Enter heart rate (bpm)', min_value=0)
pH = st.slider('Enter pH value', min_value=6.8, max_value=7.8, step=0.01)
GCS = st.slider('Enter Glasgow Coma Scale (GCS) value', min_value=3, max_value=15, step=1)
PaO2_FiO2 = st.number_input('Enter PaO2/FiO2 ratio', min_value=0)
respiration_rate = st.number_input('Enter respiration rate (breaths/min)', min_value=0)

# Calculate and display the HACOR score
if st.button('Calculate HACOR Score'):
    score = hacor_score(heart_rate, pH, GCS, PaO2_FiO2, respiration_rate)
    st.write(f'Your HACOR Score is: **{score}**')
