import streamlit as st
from google import genai

# 1. App Configuration & Branding
st.set_page_config(page_title="HyperLead AI", page_icon="🎯", layout="wide")

st.title("🎯 HyperLead AI")
st.markdown("**Your Elite B2B Sales & Outreach Agent**")
st.write("Generic cold emails go to spam. Paste your prospect's details below, and let AI write a hyper-personalized outreach campaign that guarantees replies.")
st.markdown("---")

# 2. Sidebar Setup
with st.sidebar:
    st.header("⚙️ System Setup")
    api_key = st.text_input("Enter Google Gemini API Key:", type="password")
    st.write("---")
    st.write("Built by[Your Name] | CEO of HyperLead AI")

# 3. The UI Layout (Using Columns for a professional look)
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏢 1. Your Company")
    my_company = st.text_input("Your Company Name (e.g., Nexus AI)")
    my_product = st.text_area("What do you sell? (e.g., We build custom AI software for businesses to automate tasks)", height=100)

with col2:
    st.subheader("👤 2. Your Target Prospect")
    prospect_name = st.text_input("Prospect's Name (e.g., John Doe)")
    prospect_company = st.text_input("Prospect's Company Name")
    prospect_context = st.text_area("Paste their LinkedIn Bio, recent company news, or a post they made:", height=100)

# 4. Generate Button
st.markdown("---")
if st.button("Generate Personal Outreach Campaign 🚀", use_container_width=True):
    
    if not api_key:
        st.error("⚠️ Please enter your API Key in the sidebar.")
    elif not my_company or not my_product or not prospect_name or not prospect_context:
        st.error("⚠️ Please fill out all the fields so the AI can do its research.")
    else:
        with st.spinner("Analyzing prospect and generating campaign..."):
            try:
                # Initialize Google Gemini 2.5
                client = genai.Client(api_key=api_key)
                
                # The Master Prompt
                prompt = f"""
                You are an elite B2B Sales Executive. Your goal is to write outreach messages that get replies.
                
                My Company: {my_company}
                What we sell: {my_product}
                
                Target Prospect: {prospect_name} at {prospect_company}
                Prospect Context/Research: {prospect_context}
                
                Task: 
                Write a highly personalized outreach campaign. Do NOT sound like a robot. Sound like a friendly, high-status professional. 
                Use the Prospect Context to make the first line highly personalized.
                
                Format your response EXACTLY like this:
                
                **📧 Subject Line Ideas:**
                (Give 3 catchy, short subject lines)
                
                **✉️ The Cold Email:**
                (Write a short, 4-sentence email. 1. Personalized hook, 2. The problem they might face, 3. How we fix it, 4. Low-friction Call to Action)
                
                **🔗 LinkedIn Connection Message:**
                (Write a 300-character max connection request based on their context)
                """
                
                # Get the response
                response = client.models.generate_content(
                    model="gemini-2.5-flash",
                    contents=prompt
                )
                
                # Display results beautifully in Tabs
                st.success("Campaign Generated Successfully!")
                
                tab1, tab2 = st.tabs(["📄 Campaign Results", "🧠 AI Thought Process"])
                
                with tab1:
                    st.write(response.text)
                
                with tab2:
                    st.info("The AI analyzed the prospect's background and tied it directly to your product's value proposition to ensure maximum relevance.")
                    
            except Exception as e:
                st.error(f"An error occurred: {e}") 
