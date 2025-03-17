# 📩 Advanced Cold Email Generator

This project is a **Streamlit web application** that generates compelling **cold emails** based on job descriptions, using **local LLaMA 3.2 inference** and other AI models like Mistral and Gemma. It provides an intuitive UI for users to generate, customize, and save email templates while integrating **company research** to enhance personalization.

---

## 🚀 Features

- **Cold Email Generation**: Uses AI to generate professional, engaging emails.
- **Company Research**: Automatically fetches key insights about a company.
- **Multiple AI Models**: Supports LLaMA 3.2, Mistral, and Gemma.
- **Customizable Email Tones**: Choose from Professional, Friendly, Enthusiastic, Formal, or Creative.
- **Template Management**: Save and load email templates for reuse.
- **Clipboard Copy**: Quickly copy the generated email for use.
- **Email Statistics**: Displays word and character count for easy optimization.

---

## 📦 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Kalpanil/Cold_email_generator
cd cold-email-generator
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Run the Streamlit App
```bash
streamlit run app.py
```

---

## 🔧 Dependencies

Ensure you have **Python 3.8+** installed. The project requires the following dependencies:

```bash
pip install streamlit ollama pyperclip
```

Additional dependencies:
- **Ollama** (for AI inference)
- **Streamlit** (for UI development)
- **Pyperclip** (for clipboard functionality)

---

## 🛠 Usage

1. **Enter a Job Description**: Paste the job details into the text area.
2. *(Optional)* **Research the Company**: Enter a company name and click `Research Company`.
3. **Select Email Tone & AI Model**: Customize the email output.
4. **Generate Email**: Click `Generate Email` to create a well-crafted cold email.
5. **Save or Copy**: Save the template or copy the email to your clipboard.

---

## 📂 Project Structure

```
📦 cold-email-generator
│-- app.py                # Main Streamlit app
│-- email_templates.json   # Stores saved email templates
│-- README.md              # Project documentation
│-- requirements.txt       # Python dependencies
```

---

## ✨ Future Enhancements

- 🔍 **Integration with LinkedIn API** for personalized research.
- 📧 **Email Sending Feature** using SMTP integration.
- 🤖 **Fine-tuned AI Model** for better email personalization.

---
## Screenshots
![image](https://github.com/user-attachments/assets/eedee296-8d78-43b1-b5ef-836afb3c86a5)

----
![image](https://github.com/user-attachments/assets/c8ef2364-8422-4f33-bcc5-7dfb091fc100)


---
## 📝 License
This project is licensed under the **MIT License**.

---

## 💬 Contact
For any inquiries or contributions, feel free to reach out!

📧 Email: kalpanil22kanbarkar@gmail.com 

