import streamlit as st
import numpy as np
import pickle


model = pickle.load(open('svc_p.pkl',('rb')))
df = pickle.load(open('df.pkl',('rb')))
description = pickle.load(open('description.pkl',('rb')))
diet = pickle.load(open('diet.pkl',('rb')))
medications = pickle.load(open('medications.pkl',('rb')))
precautions = pickle.load(open('precautions.pkl',('rb')))
workouts = pickle.load(open('workouts.pkl',('rb')))
symptoms = pickle.load(open('symptoms.pkl',('rb')))
disease_name = pickle.load(open('disease_name.pkl',('rb')))



st.image("logo.webp", width=60)


st.markdown("## Disease Pridiction Model") 


col1, col2 = st.columns(2)
with col1:
    symptom_1 = st.selectbox("Symptom 1",symptoms['symptoms'].unique())
    symptom_3 = st.selectbox("Symptom 3",symptoms['symptoms'].unique())
    

with col2:
    symptom_2 = st.selectbox("Symptom 2",symptoms['symptoms'].unique())
    symptom_4 = st.selectbox("Symptom 4",symptoms['symptoms'].unique())
    

column_dict = {df.columns[i]: i for i in range(132)}

symptom_list = [symptom_1,symptom_2,symptom_3,symptom_4]

def prediction(user_symptoms):

    input_vector = np.zeros(len(column_dict))
    
    for item in user_symptoms:
        
        input_vector[column_dict[item]] = 1

    result = model.predict_proba([input_vector])[0]
    result = np.argsort(result)[::-1][:2]
    classes_1 = model.classes_[result[0]]
    classes_2 = model.classes_[result[1]]

    disease_1 =  disease_name[disease_name['encoded']==classes_1]['prognosis'].values[0]
    disease_2 =  disease_name[disease_name['encoded']==classes_2]['prognosis'].values[0]

    return disease_1, disease_2

def helper(predicted_dis):

    pre = precautions[precautions['Disease']==predicted_dis][['Precaution_1','Precaution_2','Precaution_3','Precaution_4']].values[0]

    des = description[description['Disease']==predicted_dis]['Description'].values[0]

    diets = diet[diet['Disease']==predicted_dis]['Diet'].values[0]

    workout = workouts[workouts['disease']==predicted_dis]['workout'].values

    med = medications[medications['Disease']==predicted_dis]['Medication'].values[0]

    
    return pre, des, diets, workout, med

if st.button('Predict Disease'):

    disease_1, disease_2 = prediction(symptom_list)
    st.write('You Could Have ',disease_1,' or ',disease_2,'.')

if st.button('Description for Disease 1'):
    
    disease_1, disease_2 = prediction(symptom_list)
    pre, des, diets, workout, med = helper(disease_1)


    st.title("Description")
    st.markdown(
    f"""
    <div style="border: 2px solid #2196F3; padding: 10px; border-radius: 10px; background-color: #f9f9f9;">
        {des}
    </div>
    """,
    unsafe_allow_html=True
    )
  
    
    st.title("Precautions")
    content = ""
    for item in pre:
        content += f"- {item}<br>"

    st.markdown(
    f"""
    <div style="border: 2px solid #2196F3; padding: 10px; border-radius: 10px; background-color: #f9f9f9;">
        {content}
    </div>
    """,
    unsafe_allow_html=True
    )

    
        
    st.title("Diets")
    content = ""
    for item in diets:
        content += f"- {item}<br>"

    st.markdown(
    f"""
    <div style="border: 2px solid #2196F3; padding: 10px; border-radius: 10px; background-color: #f9f9f9;">
        {content}
    </div>
    """,
    unsafe_allow_html=True
    )
    

    st.title("Medication")  
    content = ""
    for item in med:
        content += f"- {item}<br>"

    st.markdown(
    f"""
    <div style="border: 2px solid #2196F3; padding: 10px; border-radius: 10px; background-color: #f9f9f9;">
        {content}
    </div>
    """,
    unsafe_allow_html=True
    )


    st.title("Workout")  
    content = ""
    for item in workout:
        content += f"- {item}<br>"

    st.markdown(
    f"""
    <div style="border: 2px solid #2196F3; padding: 10px; border-radius: 10px; background-color: #f9f9f9;">
        {content}
    </div>
    """,
    unsafe_allow_html=True
    )

if st.button('Description for Disease 2'):
    
    disease_1, disease_2 = prediction(symptom_list)
    pre, des, diets, workout, med = helper(disease_2)


    st.title("Description")
    st.markdown(
    f"""
    <div style="border: 2px solid #2196F3; padding: 10px; border-radius: 10px; background-color: #f9f9f9;">
        {des}
    </div>
    """,
    unsafe_allow_html=True
    )
  
    
    st.title("Precautions")
    content = ""
    for item in pre:
        content += f"- {item}<br>"

    st.markdown(
    f"""
    <div style="border: 2px solid #2196F3; padding: 10px; border-radius: 10px; background-color: #f9f9f9;">
        {content}
    </div>
    """,
    unsafe_allow_html=True
    )

    
        
    st.title("Diets")
    content = ""
    for item in diets:
        content += f"- {item}<br>"

    st.markdown(
    f"""
    <div style="border: 2px solid #2196F3; padding: 10px; border-radius: 10px; background-color: #f9f9f9;">
        {content}
    </div>
    """,
    unsafe_allow_html=True
    )
    

    st.title("Medication")  
    content = ""
    for item in med:
        content += f"- {item}<br>"

    st.markdown(
    f"""
    <div style="border: 2px solid #2196F3; padding: 10px; border-radius: 10px; background-color: #f9f9f9;">
        {content}
    </div>
    """,
    unsafe_allow_html=True
    )


    st.title("Workout")  
    content = ""
    for item in workout:
        content += f"- {item}<br>"

    st.markdown(
    f"""
    <div style="border: 2px solid #2196F3; padding: 10px; border-radius: 10px; background-color: #f9f9f9;">
        {content}
    </div>
    """,
    unsafe_allow_html=True
    )



