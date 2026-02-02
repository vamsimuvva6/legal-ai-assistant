import streamlit as st
import time
import os
import tempfile
import re

from pypdf import PdfReader
from docx import Document
from utils.pdf_export import generate_pdf, build_summary

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="GenAI Legal Assistant",
    layout="centered"
)

# -------------------------------------------------
# UI STYLING (PROFESSIONAL LEGAL AI THEME)
# -------------------------------------------------
st.markdown("""
<style>
#MainMenu, footer, header {visibility: hidden;}

/* Background */
.stApp {
    background-color: #E8F6F8;
}

/* Header */
.app-title {
    font-size: 2.3rem;
    font-weight: 700;
    color: #0F4C81;
}

.app-subtitle {
    color: #486581;
    margin-bottom: 1.6rem;
}

/* Card */
.card {
    background: #FFFFFF;
    border-radius: 16px;
    padding: 1.4rem 1.6rem;
    margin-bottom: 1.2rem;
    border: 1px solid #D9EAF2;
    box-shadow: 0 8px 20px rgba(15, 76, 129, 0.08);
}

/* Section titles */
.section-title {
    font-size: 1.15rem;
    font-weight: 600;
    color: #0F4C81;
    margin-bottom: 0.8rem;
}

/* Risk badges */
.badge-low {
    background: #DCFCE7;
    color: #166534;
    padding: 0.4rem 0.9rem;
    border-radius: 999px;
    font-weight: 600;
}

.badge-medium {
    background: #FEF3C7;
    color: #92400E;
    padding: 0.4rem 0.9rem;
    border-radius: 999px;
    font-weight: 600;
}

.badge-high {
    background: #FEE2E2;
    color: #7F1D1D;
    padding: 0.4rem 0.9rem;
    border-radius: 999px;
    font-weight: 600;
}

/* Muted text */
.small-muted {
    color: #486581;
    font-size: 0.85rem;
}

/* Button */
.stButton > button {
    background: linear-gradient(135deg, #FF5A5F, #E11D48);
    color: white;
    border-radius: 12px;
    font-weight: 600;
    border: none;
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------
# Utility Functions (UNCHANGED)
# -------------------------------------------------
def extract_text(uploaded_file):
    suffix = os.path.splitext(uploaded_file.name)[1]

    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded_file.getvalue())
        tmp_path = tmp.name

    text = ""

    if suffix == ".pdf":
        reader = PdfReader(tmp_path)
        for page in reader.pages[:5]:
            text += page.extract_text() or ""

    elif suffix == ".docx":
        doc = Document(tmp_path)
        text = " ".join(p.text for p in doc.paragraphs)

    elif suffix == ".txt":
        text = uploaded_file.getvalue().decode("utf-8")

    os.remove(tmp_path)
    return text.lower()


def analyze_contract(text):
    high_risk, medium_risk = [], []

    if "terminate" in text and "without notice" in text:
        high_risk.append("Termination allowed without notice")

    if "indemnify" in text or "indemnity" in text:
        high_risk.append("Unlimited indemnity obligation")

    if "auto-renew" in text or "automatically renew" in text:
        medium_risk.append("Auto-renewal clause present")

    if not high_risk and not medium_risk:
        return "LOW", [], []

    if high_risk:
        return "HIGH", high_risk, medium_risk

    return "MEDIUM", high_risk, medium_risk


def detect_contract_type(text):
    if "employment" in text or "employee" in text:
        return "Employment Agreement"
    if "vendor" in text or "supplier" in text:
        return "Vendor Agreement"
    if "lease" in text or "rent" in text:
        return "Lease Agreement"
    if "service" in text or "scope of work" in text:
        return "Service Contract"
    if "partnership" in text:
        return "Partnership Deed"
    return "General / Unknown Contract"


def extract_clauses(text):
    raw = re.split(r'\n\s*\d+[\.\)]|\n[A-Z][A-Za-z ]{3,}:', text)
    return [c.strip() for c in raw if len(c.strip()) > 80][:15]


def explain_clause_plainly(clause):
    clause = clause.lower()
    if "terminate" in clause:
        return "Explains how and when the contract can be ended."
    if "indemnify" in clause:
        return "Transfers legal and financial liability to one party."
    if "payment" in clause:
        return "Describes payment obligations and timelines."
    if "confidential" in clause:
        return "Restricts sharing of sensitive information."
    if "jurisdiction" in clause:
        return "Specifies which country’s laws apply."
    return "Defines general rights and responsibilities."

# -------------------------------------------------
# HEADER
# -------------------------------------------------
st.markdown('<div class="app-title">GenAI Legal Assistant</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="app-subtitle">AI-powered contract risk analysis for SMEs</div>',
    unsafe_allow_html=True
)

# -------------------------------------------------
# FILE UPLOAD
# -------------------------------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "Upload Contract (PDF / DOCX / TXT)",
    type=["pdf", "docx", "txt"]
)

st.markdown(
    '<div class="small-muted">Files are processed locally. No data is stored.</div>',
    unsafe_allow_html=True
)

st.markdown('</div>', unsafe_allow_html=True)

# -------------------------------------------------
# PROCESSING
# -------------------------------------------------
if uploaded_file:
    st.session_state.clear()

    with st.spinner("Extracting contract text..."):
        text = extract_text(uploaded_file)
        time.sleep(0.4)

    contract_type = detect_contract_type(text)
    clauses = extract_clauses(text)

    with st.spinner("Analyzing legal risks..."):
        contract_risk_level, high_risk_clauses, medium_risk_clauses = analyze_contract(text)
        time.sleep(0.4)

    st.session_state["analysis_result"] = {
        "overall_risk": contract_risk_level,
        "high_risk_clauses": high_risk_clauses,
        "medium_risk_clauses": medium_risk_clauses,
        "entities": {"FILE": [uploaded_file.name]}
    }

    # -------------------------------------------------
    # OVERVIEW
    # -------------------------------------------------
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Contract Overview</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.write("**Contract Type**")
        st.write(contract_type)

    with col2:
        st.write("**Overall Risk**")
        if contract_risk_level == "LOW":
            st.markdown('<span class="badge-low">LOW</span>', unsafe_allow_html=True)
        elif contract_risk_level == "MEDIUM":
            st.markdown('<span class="badge-medium">MEDIUM</span>', unsafe_allow_html=True)
        else:
            st.markdown('<span class="badge-high">HIGH</span>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # -------------------------------------------------
    # PDF EXPORT (DOWNLOAD)
    # -------------------------------------------------
    st.markdown('<div class="card">', unsafe_allow_html=True)

    summary_text = build_summary(st.session_state["analysis_result"])
    pdf_bytes = generate_pdf(summary_text)

    st.download_button(
        label="📄 Download Legal Summary (PDF)",
        data=pdf_bytes,
        file_name="legal_summary.pdf",
        mime="application/pdf"
    )

    st.markdown('</div>', unsafe_allow_html=True)
