import streamlit as st
from PIL import Image

# Page setup
st.set_page_config(page_title="My Portfolio", layout="wide")

# --- Background and Styling ---
st.markdown("""
    <style>
    /* Full-page background fix */
    .stApp {
        background: linear-gradient(to right, #f2f2f2, #dcdcdc);
        background-attachment: fixed;
        background-size: cover;
    }
    .title {
        font-size:40px; 
        color:#4B8BBE; 
        font-weight: bold;
    }
    .subhead {
        font-size:24px; 
        color:#306998; 
        margin-bottom: 30px;
    }
    .section-header {
        font-size:28px; 
        color:#FF6F61; 
        margin-top: 50px;
    }
    </style>
""", unsafe_allow_html=True)

# --- HOME ---
st.markdown('<div class="title">Hi, I\'m <span style="color:#FF6F61;">Mukesh DT</span> </div>', unsafe_allow_html=True)
st.markdown('<div class="subhead">AWS Data Engineer | SQL & Python Expert | Cloud Enthusiast ☁️</div>', unsafe_allow_html=True)
st.write("Welcome to my interactive portfolio! I'm passionate about building scalable data solutions and working with cloud-native tools.")

# --- ABOUT ---
st.markdown('<div class="section-header"> About Me</div>', unsafe_allow_html=True)
col1, col2 = st.columns([1, 3])
with col1:
    image = Image.open("my_photo.JPG")  # Replace with your image
    st.image(image, caption='Mukesh DT', width=200)
with col2:
    st.markdown("""
    - 🎓 9+ years of IT experience  
    - 💻 6+ years in SQL/PLSQL, 3+ years in AWS Data Engineering  
    - ☁️ Skilled in **AWS Glue**, **Redshift**, **S3**, **CloudWatch**  
    - 📊 Strong in data modeling, performance tuning & ETL workflows  
    - 📍 Based in [Bengaluru, India]
    """)

# --- PROJECTS ---
st.markdown('<div class="section-header">💼 Projects</div>', unsafe_allow_html=True)

with st.expander("🚀 HSBC Open Banking ETL"):
    st.markdown("""
    - Converted flat schema to star schema  
    - Used **AWS Glue**, **S3**, and **Redshift**  
    - Enabled efficient reporting and better performance  
    """)

with st.expander("📊 YouTube Analytics Pipeline"):
    st.markdown("""
    - Used **YouTube API** to extract video data  
    - Stored in **S3**, queried with **Athena**, visualized in **QuickSight**  
    """)

with st.expander("💬 Twitter Sentiment Analysis"):
    st.markdown("""
    - Real-time processing using **Kafka** + **Spark Streaming**  
    - Sentiment analysis with NLP  
    - Stored in **Redshift**, dashboards in **QuickSight**
    """)

# --- RESUME ---
st.markdown('<div class="section-header">📄 Resume</div>', unsafe_allow_html=True)
st.markdown("[📥 Download Resume](https://your-resume-link.com)", unsafe_allow_html=True)

# --- CONTACT ---
st.markdown('<div class="section-header">📬 Contact Me</div>', unsafe_allow_html=True)
st.markdown("""
- 📧 **Email:** mail2mukesh92@gmail.com  
- 🔗 **LinkedIn:** [linkedin.com/in/MukeshDT](https://www.linkedin.com/public-profile/settings?trk=d_flagship3_profile_self_view_public_profile)  
- 💻 **GitHub:** [github.com/MukeshDT](https://github.com/MukeshDT)
""")

with st.form("contact_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submitted = st.form_submit_button("Send")
    if submitted:
        st.success("Thanks for reaching out! I'll get back to you soon 😊")
