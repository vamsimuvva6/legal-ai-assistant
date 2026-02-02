st.markdown("""
<style>
#MainMenu, footer, header {visibility: hidden;}

/* =========================
   BACKGROUND
========================= */
.stApp {
    background-color: #E8F6F8;
}

/* =========================
   HEADER
========================= */
.app-title {
    font-size: 2.3rem;
    font-weight: 700;
    color: #0F4C81;
}

.app-subtitle {
    color: #486581;
    margin-bottom: 1.8rem;
    font-size: 1rem;
}

/* =========================
   CARDS
========================= */
.card {
    background: #FFFFFF;
    border-radius: 16px;
    padding: 1.4rem 1.6rem;
    margin-bottom: 1.2rem;
    box-shadow: 0 10px 24px rgba(15, 76, 129, 0.08);
    border: 1px solid #D9EAF2;
}

/* =========================
   SECTION TITLES
========================= */
.section-title {
    font-size: 1.15rem;
    font-weight: 600;
    color: #0F4C81;
    margin-bottom: 0.9rem;
}

/* =========================
   RISK BADGES
========================= */
.badge-low {
    background: #E6F4EA;
    color: #166534;
    padding: 0.45rem 1rem;
    border-radius: 999px;
    font-weight: 600;
    font-size: 0.85rem;
}

.badge-medium {
    background: #FFF7ED;
    color: #9A3412;
    padding: 0.45rem 1rem;
    border-radius: 999px;
    font-weight: 600;
    font-size: 0.85rem;
}

.badge-high {
    background: #FEE2E2;
    color: #7F1D1D;
    padding: 0.45rem 1rem;
    border-radius: 999px;
    font-weight: 600;
    font-size: 0.85rem;
}

/* =========================
   MUTED TEXT
========================= */
.small-muted {
    color: #486581;
    font-size: 0.85rem;
}

/* =========================
   BUTTONS
========================= */
.stButton > button {
    background: linear-gradient(135deg, #FF5A5F, #E11D48);
    color: #FFFFFF;
    border-radius: 12px;
    padding: 0.55rem 1.2rem;
    font-weight: 600;
    border: none;
    transition: all 0.25s ease;
}

.stButton > button:hover {
    transform: translateY(-1px);
    box-shadow: 0 8px 18px rgba(225, 29, 72, 0.35);
}

/* =========================
   EXPANDERS
========================= */
.streamlit-expanderHeader {
    font-weight: 600;
    color: #0F4C81;
}

/* =========================
   ALERT COLORS REFINED
========================= */
.stAlert {
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)
