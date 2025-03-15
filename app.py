import streamlit as st
import ollama
import pyperclip

def generate_cold_email(job_description):
    """Generates a cold email using local LLaMA 3.2 inference."""
    prompt = f"""
        You are a professional email writer. Your task is to generate a well-structured, engaging, and concise cold email for the following job description:
        
        {job_description}
        
        ### **Instructions:**
        - Address the hiring manager professionally.
        - Mention key skills relevant to the role.
        - Be polite, confident, and not too lengthy.
        - **Do not include any extra explanations, formatting, or JSON output.**
        - Only return the email in plain text format.
        
        ### **Email Structure:**
        Subject: [Your Subject Line]
        
        Dear Hiring Manager,
        [Start with a brief introduction, mentioning interest in the role.]
        [Highlight key skills and experiences relevant to the job.]
        [Express enthusiasm for the company's mission and culture.]
        [Politely request an opportunity to discuss further.]
        Keep the body short
        Best regards,
        [Your Name]
    """
    
    response = ollama.chat(
        model="llama3.2",
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": 0}
    )
    
    # Just return the raw text output
    return response["message"]["content"]

# Streamlit UI
st.title("📩 Cold Email Generator")
st.write("Paste the job description text below, and we'll generate a compelling cold email for you.")

# Text area for job description input
job_desc = st.text_area("Paste Job Description Text:")

# Session state to store the email
if 'email_text' not in st.session_state:
    st.session_state.email_text = ""

# Generate button
if st.button("Generate Email") and job_desc:
    with st.spinner("Generating email..."):
        st.session_state.email_text = generate_cold_email(job_desc)

# Display the email if we have one
if st.session_state.email_text:
    st.subheader("✉️ Your Cold Email:")
    st.text_area("", st.session_state.email_text, height=300)
    
    # Copy to clipboard button
    if st.button("📋 Copy to Clipboard"):
        pyperclip.copy(st.session_state.email_text)
        st.success("Copied to clipboard!")