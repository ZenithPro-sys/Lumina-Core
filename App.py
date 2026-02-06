import streamlit as st
import google.generativeai as genai

# Setup Google Key from Secrets
# Ensure you have GOOGLE_API_KEY in your Streamlit Secrets!
if "GOOGLE_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
else:
    st.error("Missing Google API Key in Secrets!")

# Sidebar for Expert Selection
with st.sidebar:
    st.title("Lumina Settings")
    expert_type = st.selectbox(
        "Choose your Consultant:",
        ("Creative Director", "Financial Analyst", "Marketing Strategist")
    )

# Expert Logic
if expert_type == "Creative Director":
    persona = "You are the Lumina Creative Director. Focus on branding and vision."
elif expert_type == "Financial Analyst":
    persona = "You are the Lumina Financial Analyst. Focus on tax and bookkeeping."
else:
    persona = "You are the Lumina Marketing Strategist. Focus on business growth."

st.title(f"Lumina Core | {expert_type}")

challenge = st.text_area("What is your current business challenge?")

if st.button(f"Generate {expert_type} Insights"):
    if challenge:
        model = genai.GenerativeModel('gemini-pro')
        with st.spinner("Lumina is thinking..."):
            response = model.generate_content(f"{persona}\n\nUser: {challenge}")
            st.markdown("### Lumina Insights")
            st.write(response.text)

