import os
import streamlit as st
import pandas as pd
import json
import openai
from transformers import pipeline
from io import StringIO
from dotenv import load_dotenv

load_dotenv()

openai_api_key = os.getenv('OPENAI_API_KEY')
openai.api_key = openai_api_key

gpt2_generator = pipeline('text-generation', model='gpt2')

def generate_email_openai(lead):
    prompt = f"""
    Generate a personalized outreach email for the following lead:
    Name: {lead['Name']}
    Email: {lead['Email']}
    Company: {lead['Company']}
    Job Title: {lead['Job Title']}
    Industry: {lead['Industry']}
    
    The email should be concise, professional, and tailored to their role and company.
    """
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

def generate_email_gpt2(lead):
    prompt = f"""
    Write a personalized outreach email for:
    Name: {lead['Name']}
    Email: {lead['Email']}
    Company: {lead['Company']}
    Job Title: {lead['Job Title']}
    Industry: {lead['Industry']}

    Email:
    """
    response = gpt2_generator(prompt, max_length=200, num_return_sequences=1)
    return response[0]['generated_text']

def compare_emails(email1, email2):
    # This is a very simplistic comparison, hence GPT-2 would be favored most of the time
    return "OAI" if len(email1) < len(email2) else "GPT-2 opensource"

def process_lead(lead):
    email1 = generate_email_openai(lead)
    email2 = generate_email_gpt2(lead)
    selected_email = compare_emails(email1, email2)
    
    return {
        "name": lead["Name"],
        "email": lead["Email"],
        "company": lead["Company"],
        "job_title": lead["Job Title"],
        "industry": lead["Industry"],
        "email_llm_1": email1,
        "email_llm_2": email2,
        "selected_email": selected_email
    }

def save_to_json(data, filename="output.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

st.title("Lead Email Generator")

uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)
    
    results = []
    progress_bar = st.progress(0)
    for index, row in df.iterrows():
        lead = row.to_dict()
        result = process_lead(lead)
        results.append(result)
        progress_bar.progress((index + 1) / len(df))
    
    save_to_json(results)
    st.success("Processing complete! Results saved to output.json")
    
    st.subheader("Sample Results")
    st.json(results[:3])