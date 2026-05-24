import streamlit as st
import google.generativeai as genai
import os
from fpdf import FPDF

# --- PAGE CONFIG ---
st.set_page_config(page_title="CyberShield Auditor", layout="wide", page_icon="🛡️")

# --- CUSTOM CSS (NEON HACKER STYLE) ---
st.markdown("""
    <style>
    .stApp { background-color: #0A0F1C; color: #00FFAA; font-family: 'Courier New', monospace; }
    .sidebar .sidebar-content { background-color: #111827; }
    h1, h2, h3 { color: #00FFFF; text-shadow: 0 0 10px #00FFFF; }
    .stButton>button { 
        border: 1px solid #00FFFF; background: transparent; color: #00FFFF; 
        transition: 0.3s; border-radius: 5px; width: 100%;
    }
    .stButton>button:hover { background: #00FFFF; color: #0A0F1C; box-shadow: 0 0 20px #00FFFF; }
    .stTextInput>div>div>input { background: #0A0F1C; color: #00FFAA; border: 1px solid #00FFFF; }
    .stTextArea>div>div>textarea { background: #0A0F1C; color: #00FFAA; border: 1px solid #00FFFF; }
    </style>
""", unsafe_allow_html=True)

# --- API CONFIG ---
# Hubi inaad ku darto API Key-gaaga Streamlit Secrets
api_key = st.secrets.get("GEMINI_API_KEY") 
genai.configure(api_key=api_key)

# --- FUNCTIONS ---
def create_pdf(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="CYBERSHIELD ANALYSIS REPORT", ln=True, align='C')
    pdf.multi_cell(0, 10, txt=text)
    return pdf.output(dest='S').encode('latin-1')

# --- SIDEBAR ---
st.sidebar.title("💀 CYBERSHIELD")
menu = st.sidebar.radio("SYSTEM MODULES", ["Dashboard", "AI Threat Analyzer", "Security Tools", "About Me"])

# --- SIDEBAR CONTACT ---
st.sidebar.markdown("---")
st.sidebar.subheader("📩 CONTACT ME")
with st.sidebar.form("contact_form"):
    name = st.text_input("Name")
    msg = st.text_area("Message")
    submit = st.form_submit_button("Send")
    if submit:
        st.sidebar.success("Message sent to Admin!")

# --- CONTENT ---
if menu == "Dashboard":
    st.title("🌐 LIVE SECURITY DASHBOARD")
    col1, col2, col3 = st.columns(3)
    col1.metric("Threats", "0", "Stable")
    col2.metric("System", "Online", "Secure")
    col3.metric("Uptime", "99.9%", "Steady")
    st.markdown("---")
    st.info("System operational. Waiting for input...")

elif menu == "AI Threat Analyzer":
    st.title("🤖 AI THREAT ANALYZER")
    user_input = st.text_area("PASTE CYBER LOGS / SUSPICIOUS DATA:", height=150)
    if st.button("RUN AI AUDIT"):
        if user_input:
            try:
                model = genai.GenerativeModel('gemini-1.5-flash')
                response = model.generate_content(f"Analyze this for threats: {user_input}")
                st.success(response.text)
                
                # PDF Download
                pdf_data = create_pdf(response.text)
                st.download_button("📥 Download Report", data=pdf_data, file_name="report.pdf", mime="application/pdf")
            except Exception as e:
                st.error(f"Error: {e}")
        else:
            st.warning("SYSTEM ERROR: No input detected.")

elif menu == "Security Tools":
    st.title("🛠️ HACKER TOOLKIT")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🔑 Password Scanner")
        pwd = st.text_input("Test Password", type="password")
        if st.button("Check Strength"):
            if len(pwd) >= 8: st.success("STRONG")
            else: st.error("WEAK")
    with col2:
        st.subheader("🌐 URL Scanner")
        url = st.text_input("Test URL")
        if st.button("Verify URL"):
            st.info(f"Scanning: {url}...")

elif menu == "About Me":
    st.title("👤 ABOUT ME")
    st.write("### Abdirisak Adem | IT Specialist & Cyber Security Researcher")
    st.write("Passionate about Ethical Hacking, AI, and defensive security.")
    st.write("Skills: Python, Kali Linux, Burp Suite, Network Monitoring.")

# --- FOOTER ---
st.sidebar.markdown("---")
st.sidebar.write("⚡ Secured by AI Engine")