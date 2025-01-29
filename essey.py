import streamlit as st
from PIL import Image

# Set up the page
st.set_page_config(page_title="Youcef Abdellaoui - Portfolio", page_icon="🎯", layout="wide")

# Load profile image
#profile_pic = Image.open("profile.jpg")  # Replace with your image file

# Sidebar
with st.sidebar:
    #st.image(profile_pic, width=200)
    st.title("Youcef Abdellaoui")
    st.write("### Data Scientist | AI Engineer")
    st.write("📍 Bab Ezzouar, Alger")
    st.write("📧 abdellaouiyoucef04@gmail.com")
    st.write("📞 0771418087 / 0554551685")
    st.write("[LinkedIn](https://linkedin.com/in/youcef) | [GitHub](https://github.com/youcef)")

# Main section
st.header("Welcome to My Portfolio! 👋")
st.write(
    "I am Youcef Abdellaoui, a passionate Data Scientist specializing in AI and NLP.\n"
    "Explore my projects, skills, and experience below!"
)

# Projects Section
st.subheader("🚀 Projects")
st.write("Here are some of my recent works:")

projects = {
    "Spam Email Detection": "Developed a classification model using Naïve Bayes and SVM to filter spam emails.",
    "Churn Prediction at Djezzy": "Built predictive models to improve customer retention strategies.",
    "Computer Vision for Image Recognition": "Worked on CNN models to enhance image classification accuracy.",
}

for title, desc in projects.items():
    st.markdown(f"**{title}**")
    st.write(desc)
    st.divider()

# Skills & Experience
st.subheader("💡 Skills & Experience")
skills = [
    "✅ Machine Learning: Supervised & Unsupervised Learning",
    "✅ Deep Learning: Neural Networks, CNN, RNN",
    "✅ NLP: Sentiment Analysis, Chatbots",
    "✅ Computer Vision: Image Recognition, Video Processing",
    "✅ Big Data: Hadoop, Spark",
    "✅ Programming: Python, Java, Flutter, JavaScript, C, C++",
    "✅ Databases: SQL, NoSQL",
    "✅ Cloud Computing: AWS, Azure, GCP"
]
st.write("\n".join(skills))

st.subheader("📌 Work Experience")
st.write("- **Intern Data Scientist at Djezzy**")
st.write("  - Developed churn prediction models to identify customer risks.")
st.write("  - Analyzed data trends to optimize retention strategies.")
st.write("  - Worked closely with the data science team for insights.")

# Education
st.subheader("🎓 Education")
st.write("- **Master's Degree in Artificial Intelligence** (USTHB, 2024)")
st.write("- **Bachelor's Degree in Computer Science** (USTHB, 2022)")

# Contact Form
st.subheader("📬 Get in Touch")
contact_form = """
<form action="https://formsubmit.co/your_email" method="POST">
    <input type="text" name="name" placeholder="Your Name" required>
    <input type="email" name="email" placeholder="Your Email" required>
    <textarea name="message" placeholder="Your Message" required></textarea>
    <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)
