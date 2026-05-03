import streamlit as st
from google import genai

st.set_page_config(page_title="AI Cover Letter Generator", page_icon="🚀")
st.title("🚀 Free AI Cover Letter Generator")
st.write("Stop wasting hours writing cover letters. Paste your details below and let AI do the work for you!")

with st.sidebar:
    st.header("Setup")
    api_key = st.text_input("Enter your Google Gemini API Key:", type="password")

st.subheader("1. About You")
user_experience = st.text_area("List your skills and experience:", height=100)

st.subheader("2. The Job")
job_description = st.text_area("Paste the Job Description you are applying for:", height=200)

if st.button("Generate Cover Letter ✨"):
    if not api_key:
        st.error("⚠️ Please enter your Gemini API Key in the sidebar first.")
    elif not user_experience or not job_description:
        st.error("⚠️ Please fill in both your experience and the job description.")
    else:
        with st.spinner("Writing your perfect cover letter..."):
            try:
                # Using the brand new Google GenAI SDK!
                client = genai.Client(api_key=api_key)
                
                prompt = f"""
                You are an expert career coach. Write a highly professional cover letter.
                Candidate's Experience/Skills: {user_experience}
                Job Description: {job_description}
                Keep it under 350 words and highlight how the skills match the job.
                """
                
                # Using the latest Gemini 2.5 Flash model!
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )
                
                st.success("Done! Here is your cover letter:")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
