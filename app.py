import streamlit as st
import pandas as pd
import joblib
import numpy as np



APP_ICON_URL = "download.jpeg"
# Setup web page
st.set_page_config(
     page_title="CUSTOMER LOAN RISK PREDICTION APP",
     page_icon=APP_ICON_URL,
     layout="wide",
     )

st.markdown("""
    <style type="text/css">
    blockquote {
        margin: 1em 0px 1em -1px;
        padding: 0px 0px 0px 1.2em;
        font-size: 20px;
        border-left: 5px solid rgb(230, 234, 241);
        # background-color: rgb(129, 164, 182);  
    }
    blockquote p {
        font-size: 30px;
        color: #FFFFFF;
    }
    [data-testid=stSidebar] {
        background-color: rgb(91, 173, 101);
        color: #FFFFFF;
    }
    [aria-selected="true"] {
         color: #000000;
    }
    </style>
""", unsafe_allow_html=True)

with st.container():
    col1,col2,_,_ = st.columns([1,14,1,1],gap="large")
    with col1:
        st.image(APP_ICON_URL, width=80)
    with col2:
        st.header(f"Customer Loan Risk Prediction App")
st.caption(f"App developed by Rifqi Julian Hasyari")
st.markdown("___")

@st.cache_data
def fetch_data():
    df = pd.read_csv('data.csv')
    return df

df = fetch_data()

st.sidebar.title("Prediction App 📋")
st.sidebar.write('Please choose the page')

#make two pages for EDA and Prediction
page = st.sidebar.selectbox('Choose a page', ['EDA', 'Prediction Form📋'])
if page == 'EDA':
    
  
    st.subheader('Business Insight EDA')

        
    col1, col2 = st.columns(2)
    col3, = st.columns(1)  # Menggunakan koma untuk menunjukkan bahwa ini hanya satu kolom
    col4, = st.columns(1)
    col5, = st.columns(1)
    # Memasukkan gambar ke setiap bagian
    with col1:
        st.image('target.png', use_column_width=True)
    with col2:
        st.image('risk flag.png', use_column_width=True)
    with col3:
        st.image('top5.png', use_column_width=True)
    with col4:
        st.image('state.png', use_column_width=True)
    with col5:
        st.image('city.png', use_column_width=True)
   
    
    
else:
   
    st.sidebar.title("Customer's Data")
    def user_input_features():
        # income
        income = st.number_input('income', 0.0, 1e9)
        # Subscriber Age
        age = st.number_input("Age",0,150,step=1)
        #Experience
        experience = st.number_input('experience', 0, 100, step=1)
        #married
        married = st.selectbox('married',('single', 'married'))  
        # house_ownership
        house_ownership = st.selectbox('house_ownership',df['house_ownership'].unique())
        # car_ownership
        car_ownership = st.selectbox('car_ownership',df['car_ownership'].unique())
        # Profession_Group
        Profession_Group = st.selectbox('Profession_Group',df['Profession_Group'].unique())
        # state
        state = st.selectbox('state',df['state'].unique())
        # current_job_years
        current_job_years = st.number_input('current_job_years', min_value=0, max_value=100, step=1)
        # current_house_years 
        current_house_years = st.number_input('current_house_years', min_value=0, max_value=100, step=1)
        
        
        data = {'age':age, 
        'income':income, 
        'experience': experience,
        'married':married,
        'house_ownership':house_ownership,
        'car_ownership':car_ownership,
        'Profession_Group':Profession_Group, 
        'state':state, 
        'current_job_years':current_job_years,
        'current_house_years':current_house_years}
        
        features = pd.DataFrame(data,index=[0])
        return features

    input_df = user_input_features()

    st.subheader('Customer Data📋')

    load_model = joblib.load("FinalProject.pkl")

    if st.button('Predict'):
        prediction = load_model.predict(input_df)

        if prediction == 0:  # Membandingkan dengan nilai numerik
            prediction_label = 'Aman'
        else:
            prediction_label = 'Beresiko Tinggi'

        st.write('Berdasarkan Data customer, peminjaman akan : ')
        st.write(prediction_label)
