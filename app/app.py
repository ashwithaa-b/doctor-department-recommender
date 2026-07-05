import streamlit as st
import requests
from urllib.parse import quote

st.set_page_config(
    page_title="Doctor Recommendation System",
    page_icon="🩺",
    layout="wide"
)

st.markdown("""
<style>
header {
    display: none !important;
}

[data-testid="stHeader"] {
    display: none !important;
}

.block-container {
    padding-top: 2rem !important;
    max-width: 1250px;
}

.stApp {
    background: linear-gradient(135deg, #0F3A40 0%, #071B1C 60%, #020808 100%);
    color: white;
}

.hero {
    background: #0B2426;
    padding: 35px 45px;
    border-radius: 25px;
    border: 1px solid rgba(168,255,240,0.18);
    margin-bottom: 30px;
}

.hero h1 {
    color: #B6FF2E;
    font-size: 46px;
    font-weight: 800;
    margin: 0;
}

.hero p {
    color: #C7D5D6;
    font-size: 20px;
    margin-top: 15px;
}

.metric-card {
    background: #0B2426;
    padding: 30px;
    border-radius: 22px;
    border: 1px solid rgba(168,255,240,0.15);
    min-height: 155px;
}

.metric-icon {
    color: #A8FFF0;
    font-size: 30px;
    margin-bottom: 15px;
}

.metric-title {
    color: #C7D5D6;
    font-size: 17px;
    margin-bottom: 12px;
}

.metric-value {
    color: white;
    font-size: 34px;
    font-weight: 800;
}

.example-card {
    background: #0B2426;
    padding: 28px;
    border-radius: 22px;
    border: 1px solid rgba(182,255,46,0.25);
}

.example-title {
    color: #B6FF2E;
    font-size: 27px;
    font-weight: 800;
    margin-bottom: 22px;
}

.example-item {
    background: rgba(255,255,255,0.06);
    padding: 15px 20px;
    border-radius: 14px;
    color: white;
    margin-bottom: 14px;
    font-size: 19px;
    border-left: 5px solid #B6FF2E;
}

.result-box {
    background: rgba(11,36,38,0.96);
    padding: 35px;
    border-radius: 25px;
    text-align: center;
    margin-top: 35px;
    border: 1px solid rgba(182,255,46,0.35);
}

.result-title {
    font-size: 22px;
    color: #C7D5D6;
    font-weight: 600;
}

.result-dept {
    font-size: 44px;
    color: #B6FF2E;
    font-weight: 900;
    margin-top: 10px;
}

.quote-box {
    background: rgba(182,255,46,0.08);
    border: 1px solid rgba(182,255,46,0.25);
    border-radius: 20px;
    padding: 25px;
    margin-top: 25px;
    text-align: center;
}

.quote-box p {
    color: white;
    font-size: 27px;
    font-weight: 700;
    margin: 0;
}

.stTextInput label,
.stRadio label {
    color: white !important;
    font-size: 18px !important;
    font-weight: 700 !important;
}

.stTextInput input {
    background-color: white;
    color: #071B1C;
    font-size: 20px;
    border-radius: 14px;
    padding: 14px;
}

.stButton>button {
    background: linear-gradient(135deg, #B6FF2E, #A8FFF0);
    color: #071B1C;
    font-size: 20px;
    font-weight: 800;
    border-radius: 16px;
    height: 58px;
    width: 100%;
    border: none;
    margin-top: 8px;
}

.stDownloadButton>button {
    background: #7B5CFF;
    color: white;
    font-size: 18px;
    font-weight: 700;
    border-radius: 14px;
    height: 52px;
    border: none;
}

.footer {
    text-align: center;
    color: #A7B3B5;
    margin-top: 45px;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <h1>⚕ Doctor Recommendation System</h1>
    <p>AI-powered healthcare recommendation dashboard for quick department guidance.</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-icon">▣</div>
        <div class="metric-title">Model Accuracy</div>
        <div class="metric-value">92%</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-icon">⚡</div>
        <div class="metric-title">Response Type</div>
        <div class="metric-value">Instant</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-icon">▦</div>
        <div class="metric-title">System Category</div>
        <div class="metric-value">Healthcare</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

left, right = st.columns([1.35, 1])

with left:
    symptom = st.text_input(
        "Enter your symptoms",
        placeholder="Example: fever cough, chest pain, skin rash"
    )

    recommend = st.button("Get Recommendation →")

with right:
    st.markdown("""
    <div class="example-card">
        <div class="example-title">⚕ Example Symptoms</div>
        <div class="example-item">Fever and cough</div>
        <div class="example-item">Chest pain</div>
        <div class="example-item">Skin rash</div>
        <div class="example-item">Stomach pain</div>
    </div>
    """, unsafe_allow_html=True)

if recommend:
    if not symptom.strip():
        st.warning("Please enter symptoms before getting a recommendation.")
    else:
        with st.spinner("Analyzing symptoms..."):
            try:
                encoded_symptom = quote(symptom)

                response = requests.get(
                    f"http://127.0.0.1:8000/predict?symptom={encoded_symptom}",
                    timeout=10
                )

                response.raise_for_status()
                result = response.json()

                department = result.get("recommended_department", "Not available")

                st.markdown(
                    f"""
                    <div class="result-box">
                        <div style="font-size:56px;color:#A8FFF0;">⚕</div>
                        <div class="result-title">Recommended Department</div>
                        <div class="result-dept">{department}</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.markdown("""
                <div class="quote-box">
                    <p>Healing begins with the right guidance.</p>
                </div>
                """, unsafe_allow_html=True)

                report = f"""
Doctor Recommendation Report

Symptoms:
{symptom}

Recommended Department:
{department}
"""

                st.download_button(
                    label="Download Report",
                    data=report,
                    file_name="medical_report.txt",
                    mime="text/plain"
                )

                feedback = st.radio(
                    "Was this recommendation useful?",
                    ["Yes", "No"],
                    horizontal=True
                )

                st.success(f"Feedback received: {feedback}")

            except requests.exceptions.RequestException:
                st.error(
                    "Unable to connect to the prediction API. Please check whether FastAPI is running on port 8000."
                )

st.markdown(
    "<div class='footer'>Developed for AI Healthcare Project</div>",
    unsafe_allow_html=True
)