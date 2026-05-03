import streamlit as st
from google import genai
import PyPDF2

st.set_page_config(page_title="DocuMind AI", page_icon="📄", layout="wide")

st.title("📄 DocuMind AI")
st.write("Upload any PDF document (Textbooks, Contracts, Financial Reports) and instantly ask questions about it.")
st.markdown("---")

with st.sidebar:
    st.header("⚙️ Setup")
    api_key = st.text_input("Enter Google Gemini API Key:", type="password")
    st.write("---")
    st.write("Built by Umesh | Long-Term AI SaaS")

uploaded_file = st.file_uploader("Upload your PDF document here:", type="pdf")

pdf_text = ""
if uploaded_file is not None:
    with st.spinner("Reading document..."):
        try:
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            for page in pdf_reader.pages:
                pdf_text += page.extract_text()
            st.success("✅ Document uploaded and read successfully!")
            
            with st.expander("Show Document Preview"):
                st.write(pdf_text[:1000] + "...")
                
        except Exception as e:
            st.error(f"Error reading PDF: {e}")

st.markdown("### Ask Questions about the Document")
user_question = st.text_input("What do you want to know about this document?")

if st.button("Ask AI 🧠"):
    if not api_key:
        st.error("⚠️ Please enter your API Key in the sidebar.")
    elif not uploaded_file:
        st.error("⚠️ Please upload a PDF first.")
    elif not user_question:
        st.error("⚠️ Please ask a question.")
    else:
        with st.spinner("Analyzing document to find your answer..."):
            try:
                client = genai.Client(api_key=api_key)
                prompt = f"""
                You are a highly intelligent document analysis AI.
                Read the following document text carefully.
                
                DOCUMENT TEXT:
                {pdf_text}
                
                USER QUESTION:
                {user_question}
                
                INSTRUCTIONS:
                Answer the user's question based strictly on the document provided. 
                If the answer is not in the document, say "I cannot find the answer in the provided document."
                Be highly accurate and professional.
                """
                
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )
                
                st.info("💡 **Answer:**")
                st.write(response.text)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
