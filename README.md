GenAI-Powered Legal Assistant for Indian SMEs

demo viedo:https://drive.google.com/file/d/1QWiedE3C8BeSUJKLDnUAmiTUizqZx-5Q/view?usp=sharing

deployement:https://legal-ai-assistant-fentcnowr4dnburumwxmhw.streamlit.app/

A sophisticated GenAI-powered legal assistant designed to help small and medium business owners in India understand complex contracts, identify legal risks, and receive actionable advice in plain business language.

This platform simplifies contract analysis without replacing lawyers, acting as a first line of legal understanding for SMEs.

🚀 Problem Statement

Indian SMEs frequently deal with contracts such as employment agreements, vendor contracts, lease agreements, and service contracts. These documents are often:

Legally complex

Difficult to interpret without legal expertise

Risky due to hidden or unfavorable clauses

Hiring legal experts for every contract is expensive and time-consuming.
This solution bridges that gap using GenAI + NLP, enabling SMEs to make informed decisions before signing contracts.

🎯 Solution Overview

The GenAI Legal Assistant:

Analyzes multiple types of business contracts

Explains clauses in simple business English

Identifies unfavorable and risky terms

Suggests safer alternatives

Generates summary reports for legal consultation

Maintains confidentiality and audit trails

The platform works entirely offline/local, without external APIs or legal databases.

📄 Supported Contract Types

Employment Agreements

Vendor / Supplier Contracts

Lease Agreements

Partnership Deeds

Service Contracts

🧩 Key Features
🔍 Core Legal NLP Capabilities

Contract Type Classification

Clause & Sub-Clause Extraction

Named Entity Recognition (NER):

Parties

Dates

Jurisdiction

Financial Amounts

Liabilities

Obligation vs Right vs Prohibition Identification

Risk & Compliance Detection

Ambiguity Detection & Flagging

Clause Similarity Matching with Standard Templates

⚠️ Risk Assessment Engine

Clause-level Risk Scoring: Low / Medium / High

Contract-level Composite Risk Score

Automatically detects:

Penalty Clauses

Indemnity Clauses

Unilateral Termination Rights

Arbitration & Jurisdiction Terms

Auto-Renewal & Lock-in Periods

Non-compete Clauses

Intellectual Property (IP) Transfer Clauses

👨‍💼 User-Facing Outputs

Simplified contract summary

Clause-by-clause explanation in plain language

Highlighting of unfavorable clauses

Suggested renegotiation-friendly alternatives

Risk mitigation strategies

SME-friendly standardized contract templates

PDF export for legal consultation

🌐 Multilingual Support

Supports English and Hindi contracts

Hindi contracts are internally normalized to English for NLP processing

Final outputs are provided in simple business English

📥 Input File Formats

PDF (text-based)

DOC / DOCX

Plain Text (.txt)

📊 Data Extracted from Contracts

Parties involved

Financial amounts

Obligations & liabilities

Deliverables & performance metrics

Contract duration & timelines

Termination conditions

Governing law & jurisdiction

Rights & ownership (especially IP)

Confidentiality & NDA clauses

🛠️ Tech Stack (As Per Restrictions)
✅ Allowed Tooling

LLM: GPT-4 or Claude 3 (legal reasoning only)

NLP: Python, spaCy, NLTK

UI: Streamlit / Gradio

Storage: Local file system, JSON-based audit logs

❌ Not Used

External legal databases

Case law APIs

Statutes or third-party integrations

🔐 Privacy, Security & Auditability

All contract files are processed locally

No data is sent to external services

Confidentiality is strictly maintained

JSON-based audit logs record:

Upload timestamps

Analysis actions

Risk evaluations

📤 Export & Reporting

Downloadable PDF summary reports

Suitable for:

Legal consultation

Internal review

Compliance documentation

🧠 Knowledge Base

The system continuously builds a local knowledge base of:

Common contract issues faced by Indian SMEs

Frequently occurring risky clauses

Typical negotiation points

This improves analysis consistency and risk detection over time.

🧪 How to Run Locally
# Clone repository
git clone https://github.com/your-repo/genai-legal-assistant.git
cd genai-legal-assistant

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py

📌 Disclaimer

This tool does not replace legal professionals.
It is intended to assist SMEs with initial understanding and risk awareness before consulting qualified legal experts.

🏁 Conclusion

The GenAI Legal Assistant empowers Indian SMEs by:

Simplifying complex legal contracts

Identifying hidden risks early

Improving negotiation confidence

Saving time and legal costs

Contracts made simple. Decisions made smarter.
