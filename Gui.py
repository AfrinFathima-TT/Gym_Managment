import streamlit as st
from Gym_views import GymMemberManagement

member_instance = GymMemberManagement()

tab1 , tab2 = st.tabs(["Add","View"])
with tab1 :
    st.title("Add new member")
    Name = st.text_input("Enter your name")
    Place = st.text_input("Enter your place")
    Mobile_number = st.text_input("Enter your mobile number")
    Plan = st.text_input("Enter your gym plan")
    Fee = st.text_input("Enter Fees")
    Joined_date = st.text_input("Enter joining date")
    if st.button("Add new member"):
        member_instance.post(Name = Name,Place = Place,Mobile = Mobile_number,Plan = Plan,Fee = Fee,Joined_date = Joined_date)
        st.success("New member added successfully")

with tab2:
    st.title("View member details")