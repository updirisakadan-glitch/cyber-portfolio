import streamlit as st
import google.generativeai as genai
import os

# Dejinta API Key-ga oo laga soo qaadanayo Streamlit Secrets
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Magaca iyo hordhaca bogga
st.title("🛡️ CyberShield Auditor")
st.subheader("Abdirisak Adem | IT Specialist & Cyber Security Portfolio")
st.write("Ku soo dhowow website-kayga rasmiga ah. Waxaan xiiseeyaa Ethical Hacking, Security, iyo Forex Trading.")

# Qaybta 1: AI CyberShield Auditor (Phishing/Logs)
st.markdown("---")
st.subheader("🤖 AI Threat Analyzer")
st.write("Paste the cyber logs or text to analyze here:")
user_input = st.text_area("Example: Paste a phishing email or server log snippet...")

if st.button("Analyze Security Risks"):
    if user_input:
        try:
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(f"Analyze this for cybersecurity threats: {user_input}")
            st.write("### Natiijada Falanqaynta:")
            st.info(response.text)
        except Exception as e:
            st.error(f"Khalad ayaa dhacay: {e}")