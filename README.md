📩 Cold Email Generator
=======================

This is a **Streamlit web application** that generates professional cold emails based on a given job description. It uses **local LLaMA 3.2 inference** via `ollama` to create well-structured and concise emails tailored to the job posting.

🚀 Features
-----------

*   **Generates cold emails** based on a provided job description.
*   **Uses local LLaMA 3.2 model** for AI-driven email generation.
*   **Simple and interactive UI** built with Streamlit.
*   **Copy to clipboard** functionality for easy email usage.

🛠️ Installation
----------------

### 1\. Install dependencies

Make sure you have **Python 3.8+** installed. Then, install the required Python packages:

`pip install streamlit ollama pyperclip` 

### 2\. Install and Run `ollama`

If you haven't already, install `ollama` for local LLaMA inference:

`curl -fsSL https://ollama.ai/install.sh | sh` 

Then, pull the **LLaMA 3.2** model:

`ollama pull llama3.2` 

### 3\. Run the Streamlit app

Once dependencies are installed, launch the app using:

`streamlit run app.py` 

📜 Usage
--------

1.  **Paste the job description** in the provided text area.
2.  Click **"Generate Email"** to generate a cold email.
3.  The generated email will appear in a text box.
4.  Click **"📋 Copy to Clipboard"** to easily copy and use the email.

📷 Screenshot
---------
![image](https://github.com/user-attachments/assets/d9689d2a-ab5b-4563-99db-472872b99f44)


📌 Notes
--------

*   Ensure `ollama` is running in the background before using the app.
*   The generated emails follow a professional structure with key elements like an introduction, skills, enthusiasm, and a call to action.

📝 License
----------

This project is **open-source** and free to use under the MIT License.

