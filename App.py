import streamlit as st
import openai

# --- 1. PAGE CONFIGURATION ---
st.set_page_config(page_title="Lumina Core | Business Suite", page_icon="🌟", layout="centered")

# --- 2. SECURE API CONNECTION ---
# This looks for the key in your Streamlit dashboard settings, not in the code!
try:
    client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
except Exception as e:
    st.error("Lumina Engine Offline: Please check the API Key in Streamlit Secrets.")

# --- 3. THE LUMINA BRAINS (PROMPTS) ---
prompts = {
    "Creative Director": """You are the Lumina Creative Director. Tone: Visionary, elegant, and strategic. 
    Help the user build a high-end consumer brand. Provide aesthetic direction, brand voice, and image prompts.""",
    
    "Accounting Assistant": """You are the Lumina Accounting Lead. Tone: Meticulous and professional. 
    Expert in SARS (South African Revenue Service) tax categories, VAT logic, and business expense tracking.""",
    
    "Productivity Lead": """You are the Lumina Productivity Lead. Tone: Sharp and encouraging. 
    Expert in 'Deep Work' systems, time-blocking for executives, and optimizing daily business output."""
}

# --- 4. SIDEBAR & PAYWALL ---
st.sidebar.title("Lumina Core")
st.sidebar.markdown("---")
st.sidebar.write("### Gigazone Dynamics")
st.sidebar.info("Elevating retail and business through AI.")

# Stripe Link (Replace with your actual link from Stripe)
stripe_url = "https://buy.stripe.com/your_link_here"
st.sidebar.markdown(f'''
    <a href="{stripe_url}" target="_blank">
        <button style="width:100%; background-color:#1E1E1E; color:white; border:none; padding:12px; border-radius:8px; cursor:pointer; font-weight:bold;">
            Get Pro Access - R350
        </button>
    </a>
''', unsafe_allow_html=True)

# Navigation Menu
menu = ["Creative Director (Free)", "Accounting Assistant (Pro)", "Productivity Lead (Pro)"]
choice = st.sidebar.selectbox("Choose Your Assistant", menu)

# --- 5. MAIN INTERFACE ---
st.title(f"Lumina Core | {choice.split(' (')[0]}")

# Pro Feature Protection
if "(Pro)" in choice:
    password_input = st.text_input("Enter your Pro Access Code:", type="password")
    # This also looks for the password in Secrets for safety
    if password_input != st.secrets["PRO_ACCESS_CODE"]: 
        st.warning("Access Restricted. Please purchase a code via the sidebar.")
        st.stop()

# --- 6. EXECUTION ---
user_input = st.text_area("What is your current business challenge?", placeholder="e.g., 'Help me categorize these retail expenses...'")

if st.button("Generate Lumina Insights"):
    if user_input:
        key = choice.split(" (")[0]
        selected_system_prompt = prompts[key]
        
        with st.spinner("Processing through the Lumina Engine..."):
            try:
                response = client.chat.completions.create(
                    model="gpt-4o",
                    messages=[
                        {"role": "system", "content": selected_system_prompt},
                        {"role": "user", "content": user_input}
                    ]
                )
                st.markdown("---")
                st.markdown("### Professional Guidance")
                st.write(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Engine Error: {e}")
    else:
        st.error("Please enter your query first.")
