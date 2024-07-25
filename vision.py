import datetime
from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
import logging
import pyttsx3
import threading
import time
from datetime import datetime, timedelta

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)

# Configure the generative AI model with the API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize the Gemini model
model = genai.GenerativeModel("gemini-pro-vision")
symp_model = genai.GenerativeModel("gemini-pro")

# Define a list of medical keywords for filtering
medical_keywords = ["medicine", "health", "doctor", "nurse", "treatment", "symptoms", "diagnosis", "X-ray", "MRI", "CT scan", "surgery", "prescription", "disease", "condition", "therapy"]

# Function to check if the input is medical-related
def is_medical_query(input):
    return any(keyword.lower() in input.lower() for keyword in medical_keywords)







def get_gemini_response_symptoms(symp_input):
        symp_response = symp_model.generate_content(symp_input)
        return symp_response.text
        
        
   










# Function to get Gemini response with error handling
def get_gemini_response(input, image):
    try:
        response = model.generate_content([input, image])
        return response.text
    except Exception as e:
        logging.error(f"Error generating content: {e}")
        return "An error occurred while processing your request. Please try again later."
    
    
    

# Set up the Streamlit app configuration
st.set_page_config(page_title="Medical Assistance Application")

# Application header
st.header('Medical Assistance Application')

# User input for medical query
input = st.text_input("Enter your medical query:", key="input")

# Image uploader for medical images (e.g., X-rays, MRI scans)
uploaded_file = st.file_uploader("Upload a medical image (e.g., X-ray, MRI, CT scan)...", type=["jpg", "jpeg", "png"])

image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Medical Image", use_column_width=True)

# Submit button to get medical assistance
submit = st.button("Analyze Medical Image and Query")

if submit:
    if input == "" or is_medical_query(input):
        response = get_gemini_response(input, image)
        st.subheader("The Response is:")
        st.write(response)
    else:
        st.subheader("The Response is:")
        st.write("Sorry, it's not my job. Please enter a medical-related query.")
        
        

# Additional features can be added here

if st.checkbox("Use Symptom Checker"):
    symp_input = st.text_input("Enter your symptoms", key="symp_input")
    submit=st.button("Check Symptoms")
    if submit:
        symptom_response = get_gemini_response_symptoms(symp_input)  # Pass symp_input directly
        st.subheader("The Response is:")
        st.write(symptom_response)
        st.write(f"Analyzing symptoms: {symp_input}")
        








# Medical History Integration (Example)
if st.checkbox("Upload Medical History"):
    medical_history_file = st.file_uploader("Upload your medical history file...", type=["pdf", "docx", "txt","jpeg"])
    if medical_history_file is not None:
        # Logic to handle medical history file
        st.write("Medical history file uploaded.")
# Function to speak the reminder
def speak_reminder(reminder):
    engine = pyttsx3.init()
    engine.say(reminder)
    engine.runAndWait()

# Function to set a reminder
def set_reminder(reminder, delay):
    def reminder_task():
        time.sleep(delay)
        speak_reminder(reminder)

    threading.Thread(target=reminder_task).start()

# Medication Reminder (Example)
if st.checkbox("Set Medication Reminder"):
    medication_name = st.text_input("Enter medication name:")
    reminder_time = st.time_input("Set reminder time:")
    if st.button("Set Reminder"):
        if medication_name and reminder_time:
            # Calculate the delay in seconds from now until the reminder time
            now = datetime.now()
            reminder_datetime = datetime.combine(now.date(), reminder_time)
            if reminder_datetime < now:
                # If the reminder time is earlier in the day, set it for the next day
                reminder_datetime += timedelta(days=1)
            delay_in_seconds = (reminder_datetime - now).total_seconds()

            # Example usage
            reminder_text = f"Time to take your medicine: {medication_name}."
            set_reminder(reminder_text, delay_in_seconds)

            # Keep the main thread alive to allow the reminder to trigger
            while threading.active_count() > 1:
                time.sleep(1)
            st.write(f"Reminder set for {medication_name} at {reminder_time}.")