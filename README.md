# 🩺 Medical Assistance Application
An intelligent medical assistant built using Streamlit and Google's Gemini Pro & Gemini Pro Vision models. This application helps users analyze medical queries, interpret medical images (like X-rays or MRIs), track symptoms, upload medical history, and even set medication reminders using text-to-speech.

🚀 Features
🔍 Medical Query + Image Analysis
Input your medical question (e.g., symptoms, diagnosis, etc.)

Upload medical images (X-ray, MRI, CT scan)

Gemini Vision model processes the query and image

Response is filtered to ensure it's medically relevant

🤒 Symptom Checker
A symptom-focused mode that analyzes your text input using the Gemini Pro text model

Helps understand likely causes or suggested actions based on symptoms

📁 Medical History Upload
Upload your medical history file in .pdf, .docx, .txt, or .jpeg format

Placeholder currently (can be extended to extract and summarize content)

💊 Medication Reminder (Text-to-Speech)
Set medication reminders with a name and time

Uses pyttsx3 to audibly remind you when it's time to take medication

Background thread keeps track of the schedule

🧠 Powered By
Google Generative AI

gemini-pro-vision for multimodal (text + image) analysis

gemini-pro for text-only tasks like symptom checking

Streamlit for fast web UI development

pyttsx3 for offline speech synthesis

threading and datetime to handle reminders

🛠️ Installation & Run
1. Clone the repository

git clone https://github.com/your-username/medical-assistance-app.git

cd medical-assistance-app

2. Install dependencies

pip install -r requirements.txt

3. Set up environment variables

Create a .env file in the root directory with: GOOGLE_API_KEY=your_gemini_api_key

4. Run the Streamlit app

streamlit run app.py
📦 Dependencies
streamlit

google-generativeai

Pillow

python-dotenv

pyttsx3

You can generate a requirements.txt using: pip freeze > requirements.txt
📸 Screenshots
Query + Image	Symptom Checker	Reminder

✅ TODOs & Enhancements
 Add PDF/Docx summarization for medical records

 Integrate vitals tracker (BP, sugar, etc.)

 Export chat/diagnosis to PDF

 Convert to mobile-friendly UI

 Add voice-to-text for symptom input

🧑‍⚕️ Disclaimer
This application is for informational and educational purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult your doctor before making health decisions.

📬 Contact
For queries or collaboration:

Vedant Atri
📧 vedant@example.com
🔗 LinkedIn
💻 GitHub

