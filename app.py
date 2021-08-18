import streamlit as st
import pickle
import joblib
from sklearn.ensemble import RandomForestClassifier
clf_rf = RandomForestClassifier(max_depth=60 , min_samples_leaf=3 , min_samples_split=8 , n_estimators=300)
# model = joblib.load(r'C:\Users\Harshpreet Singh\Desktop\PVT STUFF\Projects\CreditCardDefaultApp\venv\RandomForest_tuned_final.pkl')
st.title('Credit Card Default Predictor')
bal = st.number_input(' Enter LIMIT_BAL: Amount of given credit in NT dollars (includes individual and family/supplementary credit)')
sex = st.number_input('Enter SEX: Gender (1=male, 2=female)')
education = st.number_input('EDUCATION: (1=graduate school, 2=university, 3=high school, 4=others, 5=unknown, 6=unknown')
married = st.number_input('MARRIAGE: Marital status (1=married, 2=single, 3=others')
age = st.number_input('AGE: Age in years')
pay1 = st.number_input('PAY_0: Repayment status in September, 2005 (-1=pay duly, 1=payment delay for one month, 2=payment delay for two months, … 8=payment delay for eight months, 9=payment delay for nine months and above)')
# • PAY_2: Repayment status in August, 2005 (scale same as above)
# • PAY_3: Repayment status in July, 2005 (scale same as above)
# • PAY_4: Repayment status in June, 2005 (scale same as above)
# • PAY_5: Repayment status in May, 2005 (scale same as above)
# • PAY_6: Repayment status in April, 2005 (scale same as above)
pay2 = pay3 = pay4 = pay5 = pay6 = -1
bill_amt1 = st.number_input('BILL_AMT1: Amount of bill statement in September, 2005 (NT dollar)')
# • BILL_AMT2: Amount of bill statement in August, 2005 (NT dollar)
# • BILL_AMT3: Amount of bill statement in July, 2005 (NT dollar)
# • BILL_AMT4: Amount of bill statement in June, 2005 (NT dollar)
# • BILL_AMT5: Amount of bill statement in May, 2005 (NT dollar)
# • BILL_AMT6: Amount of bill statement in April, 2005 (NT dollar)
bill_amt2 = bill_amt3 = bill_amt4 = bill_amt5 =bill_amt6 = 0
pay_amt1 = st.number_input('PAY_AMT1: Amount of previous payment in September, 2005 (NT dollar)')
# • PAY_AMT2: Amount of previous payment in August, 2005 (NT dollar)
# • PAY_AMT3: Amount of previous payment in July, 2005 (NT dollar)
# • PAY_AMT4: Amount of previous payment in June, 2005 (NT dollar)
# • PAY_AMT5: Amount of previous payment in May, 2005 (NT dollar)
# • PAY_AMT6: Amount of previous payment in April, 2005 (NT dollar)
pay_amt2 = pay_amt3 = pay_amt4 = pay_amt5 = pay_amt6 = 0
# • default.payment.next.month: Default payment (1=yes, 0=no)
y_pred = clf_rf.predict([[bal , sex , education , married , age , pay1 , pay2 , pay3 , pay4 , pay5 , pay6 , bill_amt1 , bill_amt2 , bill_amt3 , bill_amt4 , bill_amt5 , \
    bill_amt6 , pay_amt1 , pay_amt2 , pay_amt3 , pay_amt4 , pay_amt5 , pay_amt6]])

if st.button('predict'):
    if y_pred == 1:
        st.header('Defaulter')
    elif y_pred == 0:
        st.header('Non-Defaulter')
