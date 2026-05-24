import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load security environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)
else:
    st.error("⚠️ Security Error: AI API Key not found in .env file!")

# Streamlit Page Configuration
st.set_page_config(page_title="Mohamed | Cybersecurity Portfolio", page_icon="🛡️", layout="wide")

# SECTION 1: DIGITAL PORTFOLIO
st.title("🛡️ Mohamed | IT Specialist & Cyber Security Portfolio")
st.markdown("Welcome to my official website. I am an *IT Specialist* passionate about *Ethical Hacking, defensive security, and **Forex Trading* analytics.")

col1, col2 = st.columns(2)
with col1:
    st.subheader("👨‍💻 Tech Expertise")
    st.write("• Network Security & Monitoring")
    st.write("• AI-Powered Application Development (Python)")
    st.write("• Risk Management & Forex Market Analysis")

with col2:
    st.subheader("🎯 My Mission")
    st.write("To build resilient digital systems, analyze financial market anomalies, and protect organizational infrastructures from cyber threats and exploitation.")

st.markdown("---")

# SECTION 2: AI CYBER SECURITY AUDITOR APP
st.header("🤖 AI CyberShield Auditor")
st.markdown("Input any suspicious data below (e.g., emails, URLs, or network logs) for the AI to perform an automated vulnerability assessment.")

user_input = st.text_area("Paste the cyber logs or text to analyze here:", placeholder="Example: Paste a phishing email or server log snippet...")

if st.button("Analyze Security Risks 🔍"):
    if user_input:
        # Input Sanitization for Web Security
        clean_input = str(user_input).replace("<script>", "").replace("</script>", "")
        
        with st.spinner("AI is auditing the system vulnerabilities..."):
            try:
                model = genai.GenerativeModel("gemini-1.5-flash")
                
                prompt = f"""
                You are a Senior Ethical Hacker and Defensive Cybersecurity Expert.
                Analyze the following data for any security threats, ransomware patterns, phishing attempts, or malicious payloads.
                Provide clear, actionable recommendations on how an organization or individual can mitigate this risk.
                
                DATA TO AUDIT: {clean_input}
                """
                
                response = model.generate_content(prompt)
                st.success("Security audit completed successfully!")
                st.subheader("AI Vulnerability Report:")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"An error occurred during analysis: {e}")
    else:
        st.warning("Please input some text or logs first to run the audit!")