import streamlit as st
import ollama
import pyperclip
import json
import os
from datetime import datetime

# Constants
AVAILABLE_MODELS = ["llama3.2", "mistral", "gemma"]
EMAIL_TONES = ["Professional", "Friendly", "Enthusiastic", "Formal", "Creative"]
DEFAULT_TEMPLATES_FILE = "email_templates.json"

def load_templates():
    """Load saved email templates from JSON file."""
    if os.path.exists(DEFAULT_TEMPLATES_FILE):
        with open(DEFAULT_TEMPLATES_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_template(name, job_desc, email_text):
    """Save an email template to JSON file."""
    templates = load_templates()
    templates[name] = {
        "job_description": job_desc,
        "email_text": email_text,
        "date_created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    with open(DEFAULT_TEMPLATES_FILE, 'w') as f:
        json.dump(templates, f, indent=4)

def research_company(company_name):
    """Generate company research using LLM."""
    prompt = f"""
    Provide a brief research summary about {company_name}. Focus on:
    1. Main products/services
    2. Company culture and values
    3. Recent achievements or news
    Keep it concise and relevant for a cold email.
    """
    
    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": 0.7}
    )
    return response["message"]["content"]

def generate_cold_email(job_description, tone, model, company_name=None, company_research=None):
    """Generates a cold email using selected LLM model and tone."""
    
    company_context = ""
    if company_name and company_research:
        company_context = f"\nCompany Context:\n{company_research}"
    
    prompt = f"""
        You are a professional email writer. Your task is to generate a well-structured, engaging, and concise cold email for the following job description:
        
        {job_description}
        
        {company_context}
        
        ### **Instructions:**
        - Use a {tone.lower()} tone in the writing
        - Address the hiring manager professionally
        - Mention key skills relevant to the role
        - Be polite, confident, and not too lengthy
        - If company research is provided, incorporate relevant details naturally
        - **Do not include any extra explanations, formatting, or JSON output**
        - Only return the email in plain text format
        
        ### **Email Structure:**
        Subject: [Your Subject Line]
        
        Dear Hiring Manager,
        [Start with a brief introduction, mentioning interest in the role]
        [Highlight key skills and experiences relevant to the job]
        [Express enthusiasm for the company's mission and culture]
        [Politely request an opportunity to discuss further]
        Keep the body short
        Best regards,
        [Your Name]
    """
    
    response = ollama.chat(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": 0.7}
    )
    
    return response["message"]["content"]

# Streamlit UI
st.set_page_config(page_title="Enhanced Cold Email Generator", layout="wide")
st.title("📩 Advanced Cold Email Generator")
st.write("Generate compelling cold emails with customizable options and company research integration.")

# Create two columns for the layout
col1, col2 = st.columns([2, 1])

with col1:
    # Main input section
    job_desc = st.text_area("Paste Job Description Text:", height=200)
    
    # Company research section
    company_name = st.text_input("Company Name (Optional):")
    if company_name:
        if st.button("Research Company"):
            with st.spinner("Researching company..."):
                company_research = research_company(company_name)
                st.session_state.company_research = company_research
                st.info("Company Research Results:")
                st.write(company_research)

with col2:
    # Configuration options
    st.subheader("Email Settings")
    selected_tone = st.selectbox("Select Email Tone:", EMAIL_TONES)
    selected_model = st.selectbox("Select AI Model:", AVAILABLE_MODELS)
    
    # Template management
    st.subheader("Template Management")
    template_name = st.text_input("Template Name (to save):")
    
    # Load saved templates
    templates = load_templates()
    if templates:
        selected_template = st.selectbox(
            "Load Saved Template:",
            ["None"] + list(templates.keys())
        )
        if selected_template != "None":
            if st.button("Load Template"):
                job_desc = templates[selected_template]["job_description"]
                st.session_state.email_text = templates[selected_template]["email_text"]

# Initialize session state
if 'email_text' not in st.session_state:
    st.session_state.email_text = ""
if 'company_research' not in st.session_state:
    st.session_state.company_research = ""

# Generate button
if st.button("Generate Email") and job_desc:
    with st.spinner("Generating email..."):
        company_research = st.session_state.company_research if company_name else None
        st.session_state.email_text = generate_cold_email(
            job_desc,
            selected_tone,
            selected_model,
            company_name,
            company_research
        )

# Display the email if we have one
if st.session_state.email_text:
    st.subheader("✉️ Your Cold Email:")
    email_text = st.text_area("", st.session_state.email_text, height=300)
    
    # Email statistics
    char_count = len(email_text)
    word_count = len(email_text.split())
    st.info(f"📊 Statistics: {char_count} characters | {word_count} words")
    
    col3, col4 = st.columns(2)
    with col3:
        # Copy to clipboard button
        if st.button("📋 Copy to Clipboard"):
            pyperclip.copy(email_text)
            st.success("Copied to clipboard!")
    
    with col4:
        # Save template button
        if template_name and st.button("💾 Save as Template"):
            save_template(template_name, job_desc, email_text)
            st.success(f"Template '{template_name}' saved successfully!")