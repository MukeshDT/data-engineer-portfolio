import streamlit as st
from PIL import Image

st.set_page_config(page_title="My Data Engineer Portfolio", layout="wide")

# --- Custom Header ---
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
    }
    .title {
        font-size:40px;
        color:#4B8BBE;
    }
    .subhead {
        font-size:22px;
        color:#306998;
    }
    </style>
""", unsafe_allow_html=True)

menu = st.sidebar.radio("🌐 Navigate", ["🏠 Home", "👤 About", "💼 Projects", "📄 Resume", "📬 Contact"])

# HOME
if menu.startswith("🏠"):
    st.markdown('<div class="title">Hi, I\'m <span style="color:#FF6F61;">Mukesh DT</span> 👋</div>', unsafe_allow_html=True)
    st.markdown('<div class="subhead">AWS Data Engineer | SQL & Python Expert | Cloud Lover ☁️</div>', unsafe_allow_html=True)
    st.write("Welcome to my interactive portfolio! 🚀")

# ABOUT
elif menu.startswith("👤"):
    st.markdown('<div class="title">About Me</div>', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 3])
    with col1:
        image = Image.open("my_photo.JPG")  # Replace with your image
        st.image(image, caption='Mukesh DT', width=200)
    with col2:
        st.markdown("""
        <span style="font-size:18px">
        🎯 **9+ years** of IT experience  
        🔧 **SQL/PLSQL Expert** and **3+ years in AWS Data Engineering**  
        🛠️ Skilled in **Redshift**, **Glue**, **S3**, and **CloudWatch**
        🌍 Based in **Bengaluru, India**
        </span>
        """, unsafe_allow_html=True)

# PROJECTS
elif menu.startswith("💼"):
    st.markdown('<div class="title">Projects</div>', unsafe_allow_html=True)

    with st.expander("🚀 HSBC Open Banking ETL"):
        st.markdown("""
        - ✅ Converted flat schema to star schema  
        - 🧪 Tools: **AWS S3**, **Glue**, **Redshift**, **CloudWatch**  
        - 📈 Improved performance by 60%  
        """)

    with st.expander("📊 YouTube Analytics Pipeline"):
        st.markdown("""
        - 📡 Pulled data using **YouTube API**  
        - 🧺 Stored in **S3**, queried with **Athena**  
        - 📊 Visualized with **QuickSight**  
        """)

    with st.expander("💬 Real-Time Twitter Sentiment"):
        st.markdown("""
        - 🐍 Built pipeline with **Kafka + Spark Streaming**  
        - 🧠 Performed sentiment analysis  
        - 📍 Stored results in **Redshift**, visualized in **QuickSight**
        """)

# RESUME
elif menu.startswith("📄"):
    st.markdown('<div class="title">Resume</div>', unsafe_allow_html=True)
    st.markdown("[📥 Download Resume (PDF)](https://your-resume-link.com)", unsafe_allow_html=True)
    st.success("Tip: Keep your resume updated every 3–6 months.")

# CONTACT
elif menu.startswith("📬"):
    st.markdown('<div class="title">Contact</div>', unsafe_allow_html=True)

    st.markdown("""
    📧 **Email:** mail2mukesh92@gmail.com  
    🔗 **LinkedIn:** [linkedin.com/in/MukeshDT](https://www.linkedin.com/public-profile/settings?trk=d_flagship3_profile_self_view_public_profile)  
    💻 **GitHub:** [github.com/MukeshDT](https://github.com/MukeshDT)  
    """)

    st.write("📨 Drop me a message:")
    with st.form(key="contact_form"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit = st.form_submit_button("Send")
        if submit:
            st.success("✅ Thanks for your message! I’ll reply soon.")
