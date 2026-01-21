import streamlit as st
import pdfplumber
import os
import tempfile
import io
from datetime import datetime

st.set_page_config(page_title="Resume Scorer", page_icon="🔍", layout="wide")

# Helper functions
def load_skills(filepath="roles.txt"):
    skills = []
    if not os.path.exists(filepath):
        st.error("❌ roles.txt not found!")
        return ["python", "html", "css", "javascript", "java", "sql"]
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip().lower()
                if line and not line.startswith('==='):
                    skills.append(line)
        return skills
    except Exception as e:
        st.error(f"Error: {e}")
        return ["python", "html", "css"]

def extract_text_from_pdf(pdf_file):
    try:
        text = ""
        with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp_file:
            tmp_file.write(pdf_file.getbuffer())
            tmp_path = tmp_file.name
        
        try:
            with pdfplumber.open(tmp_path) as pdf:
                for page_num, page in enumerate(pdf.pages, 1):
                    page_text = page.extract_text()
                    if page_text:
                        text += page_text + "\n\n"
        finally:
            try:
                os.unlink(tmp_path)
            except:
                pass
        
        return text.lower() if text else ""
    except Exception as e:
        st.error(f"PDF extraction error: {e}")
        return ""

def analyze_resume(text, skills):
    found_skills = [s for s in skills if s in text]
    missing_skills = [s for s in skills if s not in found_skills]
    score = (len(found_skills) / len(skills)) * 100 if skills else 0
    return score, found_skills, missing_skills

def create_analysis_report(score, found_skills, missing_skills, skills, filename):
    """Generate downloadable analysis report"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    report = f"""RESUME ANALYSIS REPORT
Generated: {timestamp}
Filename: {filename}

OVERALL SCORE: {score:.1f}% ({len(found_skills)}/{len(skills)} skills found)

FOUND SKILLS ({len(found_skills)}):
"""
    for skill in sorted(found_skills):
        report += f"✓ {skill}\n"
    
    report += f"\nMISSING SKILLS ({len(missing_skills)}):\n"
    for skill in sorted(missing_skills):
        report += f"✗ {skill}\n"
    
    report += f"\n\nTotal Skills in Database: {len(skills)}"
    return report

# UI
st.title("📄 Resume Scorer")

# Load skills
skills = load_skills()
if skills:
    st.success(f"✅ Loaded {len(skills)} skills")

st.markdown("---")

# File upload
uploaded = st.file_uploader("Upload PDF Resume", type="pdf")

if uploaded:
    st.info(f"**File:** {uploaded.name} | **Size:** {uploaded.size/1024:.1f} KB")
    
    if st.button("🚀 Process Resume", type="primary"):
        with st.spinner("Extracting text..."):
            text = extract_text_from_pdf(uploaded)
        
        if not text or len(text.strip()) < 20:
            st.error("❌ Could not extract text. Use text-based PDF (Word/Google Docs)")
            st.stop()
        
        # Store extracted text for download
        st.session_state.extracted_text = text
        st.session_state.filename = uploaded.name
        
        # Show preview
        with st.expander("📝 Preview extracted text"):
            preview = text[:2000]
            if len(text) > 2000:
                preview += f"\n\n... (showing first 2000 chars of {len(text)} total)"
            st.text_area("Extracted Text Preview", preview, height=300)
        
        # Analyze
        with st.spinner("Analyzing skills..."):
            score, found, missing = analyze_resume(text, skills)
        
        # Store analysis for download
        st.session_state.score = score
        st.session_state.found_skills = found
        st.session_state.missing_skills = missing
        
        # Results
        st.markdown("### 📊 Results")
        col1, col2, col3 = st.columns(3)
        col1.metric("Score", f"{score:.1f}%")
        col2.metric("Found", len(found))
        col3.metric("Missing", len(missing))
        
        # Skills
        tab1, tab2 = st.tabs(["✅ Found", "❌ Missing"])
        with tab1:
            if found:
                for skill in sorted(found):
                    st.success(f"✓ {skill}")
            else:
                st.info("No skills found")
        with tab2:
            if missing:
                for skill in sorted(missing):
                    st.warning(f"✗ {skill}")
            else:
                st.success("All skills found!")
        
        # DOWNLOAD BUTTONS
        st.markdown("---")
        st.markdown("### 💾 Downloads")
        col1, col2 = st.columns(2)
        
        with col1:
            # Download extracted text
            if 'extracted_text' in st.session_state:
                text_buffer = io.StringIO(st.session_state.extracted_text)
                st.download_button(
                    label="📥 Download Extracted Text (.txt)",
                    data=text_buffer.getvalue(),
                    file_name=f"{st.session_state.filename}_extracted.txt",
                    mime="text/plain"
                )
        
        with col2:
            # Download analysis report
            if 'score' in st.session_state:
                report = create_analysis_report(
                    st.session_state.score, 
                    st.session_state.found_skills, 
                    st.session_state.missing_skills, 
                    skills,
                    st.session_state.filename
                )
                st.download_button(
                    label="📊 Download Analysis Report (.txt)",
                    data=report,
                    file_name=f"{st.session_state.filename}_analysis.txt",
                    mime="text/plain"
                )

else:
    st.info("👆 Upload a PDF resume")

st.markdown("---")
