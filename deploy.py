# import joblib
import streamlit as st
import pandas as pd
# import pickle
import xgboost as xgb


# Data=pickle.load(open('RandomForestRegressor_model.pkl','rb'))
# C:/Users/MOHMMED/Downloads/prediction project/
# Data=joblib.load('model.joblib')
def main():
    model=xgb.XGBRegressor()
    model.load_model('xg_models.json')
    st.title(" Calories Burnt Prediction Web App")
    st.info('Easy Application For Calories Burnt Prediction')
    # st.sidebar.header('Feature Selection')
    #  'Gender', 'Age', 'Height', 'Weight', 'Duration',
    #        'Heart_Rate', 'Body_Temp', 'Calories'],
    #       dtype='object'
    gender=st.selectbox("Gender",('male','female'))
    if gender=='male':
        p1=1
    elif gender =='female':
        p1=0
    age=st.number_input('Age')
    height=st.number_input('Height')
    weight=st.number_input('Weight')
    duration=st.number_input('Duration')
    heart_rate=st.number_input('Heart_Rate')
    body_temp=st.number_input('Body_Temp')

    df=pd.DataFrame({'Gender':[p1],'Age':[age],'Height':[height],'Weight':[weight],
                'Duration':[duration],'Heart_Rate':[heart_rate],'Body_Temp':[body_temp]},index=[0])
    try:
        con=st.button('Predict')
        if con:
            pred=model.predict(df)
            if pred>0:
                st.success(f"you burn {pred} calories")
            else:
                st. Warning('NO Calories Burned')
    except:
        st.Warning('Something Went Wrong please try again')
if __name__=='__main__':
    main()        