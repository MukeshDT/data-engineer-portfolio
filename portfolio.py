# portfolio.py
import streamlit as st

st.set_page_config(page_title="My Data Engineer Portfolio", layout="wide")

st.title("Hi, I'm [Your Name] 👋")
st.subheader("AWS Data Engineer | SQL & Python Expert")

st.markdown("""
Welcome to my portfolio! I'm a passionate Data Engineer with 9+ years of experience.
""")

st.header("Projects")

with st.expander("1. HSBC Open Banking ETL Project"):
    st.markdown("""
    - Transformed flat schema to star schema using AWS Glue and Redshift
    - Improved performance and enabled better analytics
    """)

with st.expander("2. YouTube Analytics Pipeline"):
    st.markdown("""
    - Pulled data using YouTube API, stored in S3, and visualized in QuickSight
    """)

st.header("Contact")
st.markdown("""
**Email:** mail2mukesh92@gmail.com  
**LinkedIn:** [linkedin.com/in/mukeshDT](https://www.linkedin.com/public-profile/settings?trk=d_flagship3_profile_self_view_public_profile)  
**GitHub:** [github.com/mukeshDT](https://github.com/MukeshDT)  
""")