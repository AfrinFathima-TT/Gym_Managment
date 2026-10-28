import streamlit as st
from Gym_views import GymMemberManagement

member_instance = GymMemberManagement()

tab1 , tab2 = st.tabs(["Add","View"])
with tab1 :
    st.title("Add new member")
    Name = st.text_input("Enter your name")
    Place = st.text_input("Enter your place")
    Mobile_number = st.text_input("Enter your mobile number")
    Plan = st.selectbox("Please select your gym plan",["1 Month","3 Month","6 Month","9 Month","12 Month"])
    Fee = st.text_input("Enter Fees")
    Joined_date = st.date_input("Enter joining date (yyyy/mm/dd)")
    if st.button("Add new member"):
        member_instance.post(Name = Name,Place = Place,Mobile = Mobile_number,Plan = Plan,Fee = Fee,Joined_date = Joined_date)
        st.success("New member added successfully")

with tab2:
    st.title("View member details")
    records = member_instance.get()
    if records:
        st.table(records)
    else:
        st.warning("No records found...!")
