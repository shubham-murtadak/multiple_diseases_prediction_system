# -*- coding: utf-8 -*-
import pickle
import streamlit as st 
from streamlit_option_menu import option_menu 

#loading save model

diabetes_model=pickle.load(open('diabeties_model.sav','rb'))
heart_disease_model=pickle.load(open('heart_disease_model.sav','rb'))
perkinsons_model=pickle.load(open('perkinsons_model.sav','rb'))


#multiple pages creating

with st.sidebar:
    selected=option_menu('Multiple Disease Prediction System', 
                         ['Diabetes Prediction',
                          'Heart Disease Prediction',
                          'Parkinsons Prediction'],
                         icons=['activity','heart','person'],
                         default_index=0)

# prediction page

if(selected =='Diabetes Prediction'):
    #page title 
    st.title('Diabetes Predictor')
    
    #making input coloumn wise
    col1,col2,col3=st.columns(3)
    
    with col1:
        Pregnancies=st.text_input('Number of Pregnancies')
    with col2:
        Glucose=st.text_input('Glucose level')
    with col3:
        BloodPressure=st.text_input('BLoodpressure value')
    with col1:
        SkinThickness=st.text_input('SkinThickness value')
    with col2:
        Insulin=st.text_input('Insulin level')
    with col3:
        BMI=st.text_input('BMI VALUE')
    with col1:
        DibetesPedigreeFunction=st.text_input('Dibetes Pedigree Function value')
    with col2:
        Age=st.text_input('AGE of the person')
    
    
    diabetes_diagnosis=''
    
    #creating a butoon for prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DibetesPedigreeFunction,Age]])
        
        if(diab_prediction[0]==1):
            diabetes_diagnosis='The person is Diabetic'
            
        else:
            diabetes_diagnosis='The person is not Diabetic'
    st.success(diabetes_diagnosis)
        

if(selected =='Heart Disease Prediction'):
    st.title('Heart Disease Predictor ')
    #taking input colwise
    col1,col2,col3=st.columns(3)
    
    #age  sex  cp  trestbps  chol  fbs  restecg  thalach  exang  oldpeak  slope  ca  thal 
    
    with col1:
        age=st.text_input('Age')
    with col2:
        sex=st.text_input('Sex')
    with col3:
        cp=st.text_input('cp')
    with col1:
        trestbps=st.text_input('trestbps')
    with col2:
        chol=st.text_input('chol')
    with col3:
        fbs=st.text_input('fbs')
    with col1:
        restecg=st.text_input('restecg')
    with col2:
        thalach=st.text_input('thalach')
    with col3:
        exang=st.text_input('exang')
    with col1:
        oldpeak=st.text_input('oldpeak')
    with col2:
        slope=st.text_input('slope')
    with col3:
        ca=st.text_input('ca')
    with col1:
        thal=st.text_input('thal')
        
    heart_diagnosis=''
     
     #creating a butoon for prediction
     
    if st.button('Heart_Diesease Test Result'):
         heart_prediction=heart_disease_model.predict([[age,sex, cp,  trestbps , chol,  fbs , restecg , thalach , exang,  oldpeak,  slope , ca , thal ]])
         
         if(heart_prediction[0]==1):
             diabetes_diagnosis='The person is Heart Dieseas patient'
             
         else:
             diabetes_diagnosis='The person is not Heart Dieseas patient'
    st.success(heart_diagnosis)
    
    
    
if(selected =='Parkinsons Prediction'):
    
    st.title('Parkinsons Predictor ')
    
    #taking input colwise
    col1,col2,col3,col4,col5=st.columns(5)
    
    
  
    
    with col1:
        MDVPFo=st.text_input('MDVP:Fo(Hz)')
    with col2:
        MDVPFh=st.text_input('MDVP:Fhi(Hz)')
    with col3:
        MDVPFl=st.text_input('MDVP:Flo(Hz)')
    with col4:
        MDVPJ1=st.text_input('MDVP:Jitter(%)')
    with col5:
        MDVPJ2=st.text_input('MDVP:Jitter(Abs)')
    with col1:
        MDVPRAP=st.text_input('MDVP:RAP')
    with col2:
        MDVPPPQ=st.text_input('MDVP:PPQ')
    with col3:
        JitterDDP=st.text_input('Jitter:DDP')
    with col4:
        MDVPShimmer=st.text_input('MDVP:Shimmer')
    with col5:
        MDVPShimmer2=st.text_input('MDVP:Shimmer(dB)')
    with col1:
        ShimmerAPQ3=st.text_input('Shimmer:APQ3')
    with col2:
        ShimmerAPQ5=st.text_input('Shimmer:APQ5')
    with col3:
        MDVPAPQ=st.text_input('MDVP:APQ')
    with col4:
        ShimmerDDA=st.text_input('Shimmer:DDA')
    with col5:
        NHR=st.text_input('NHR')   
    with col1:
        HNR=st.text_input('HNR')
    with col2:
        RPDE=st.text_input('RPDE')
    with col3:
        D2=st.text_input('D2')
    with col4:
        DFA=st.text_input('DFA')
    with col5:
        spread1=st.text_input('spread1')
    with col1:
        spread2=st.text_input('spread2')
    with col2:
        PPE=st.text_input('PPE')
    perkinsons_diagnosis=''
      
      #creating a butoon for prediction
      
    if st.button('Perkinsons_Diesease Test Result'):
          perkinsons_prediction=perkinsons_model.predict([[MDVPFo, MDVPFh, MDVPFl, MDVPJ1, MDVPJ2,MDVPRAP,MDVPPPQ, MDVPPPQ,JitterDDP,MDVPShimmer, MDVPShimmer2,ShimmerAPQ3,ShimmerAPQ5,MDVPAPQ,ShimmerDDA,NHR, HNR,RPDE,D2,DFA,spread1,spread2,PPE]])
          
          if(perkinsons_prediction[0]==1):
              diabetes_diagnosis='The person is Perkinsons Dieseas patient'
              
          else:
              diabetes_diagnosis='The person is not Perkinsons Dieseas patient'
    st.success(perkinsons_diagnosis)
