import streamlit as st
import genai

# 1. Setup your Free Google Key from Secrets
# Make sure you add "GOOGLE_API_KEY" to your Streamlit Secrets!
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# 2. Sidebar for Expert Selection
with st.sidebar:
    st.title("Lumina Settings")
    expert_type = st.selectbox(
        "Choose your Consultant:",
        ("Creative Director", "Financial Analyst", "Marketing Strategist")
    )
    st.info(f"Currently acting as: {expert_type}")

# 3. Expert Logic (The "System Prompt")
if expert_type == "Creative Director":
    persona = "You are the Lumina Creative Director. Focus on branding, vision, and high-end design advice."
elif expert_type == "Financial Analyst":
    persona = "You are the Lumina Financial Analyst. Focus on tax categorization, retail ROI, and business bookkeeping."
else:
    persona = "You are the Lumina Marketing Strategist. Focus on customer growth and digital sales."

st.title(f"Lumina Core | {expert_type}")

# 4. User Input
challenge = st.text_area("What is your current business challenge?", 
                         placeholder="e.g., 'Categorize my retail stock expenses...'")

# 5. Execution
if st.button(f"Generate {expert_type} Insights"):
    if challenge:
        model = genai.GenerativeModel('gemini-pro')
        # We combine the persona and the challenge for the free model
        full_prompt = f"{persona}\n\nUser Challenge: {challenge}"
        
        with st.spinner("Lumina is thinking..."):
            response = model.generate_content(full_prompt)
            st.markdown("### Lumina Insights")
            st.write(response.text)
    else:
        st.warning("Please enter a challenge first!")
