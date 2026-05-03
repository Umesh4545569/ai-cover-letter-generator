import streamlit as st
from google import genai

# Company Branding
st.set_page_config(page_title="Nexus AI Agents", page_icon="⚡", layout="wide")
st.sidebar.title("⚡ Nexus AI Workspace")
st.sidebar.write("Your on-demand AI workforce.")

# API Key Setup
api_key = st.sidebar.text_input("Enter your Google Gemini API Key:", type="password")

# Select Your Agent
agent_choice = st.sidebar.radio(
    "Select an AI Agent to hire:",["📈 The Sales Agent", "✍️ The SEO Blog Agent", "📱 The Social Media Agent"]
)

st.sidebar.markdown("---")
st.sidebar.write("Built by Umesh")

# ---------------------------------------------------------
# AGENT 1: THE SALES AGENT (Cold Email Writer)
# ---------------------------------------------------------
if agent_choice == "📈 The Sales Agent":
    st.title("📈 The Sales Agent")
    st.write("Generates high-converting cold emails to get B2B clients.")
    
    product_name = st.text_input("What are you selling?")
    target_audience = st.text_input("Who are you emailing? (e.g., Real Estate CEOs)")
    
    if st.button("Generate Cold Email 🚀"):
        if not api_key:
            st.error("⚠️ Please enter your API Key in the sidebar.")
        else:
            with st.spinner("Writing the perfect sales pitch..."):
                client = genai.Client(api_key=api_key)
                prompt = f"Write a short, punchy, and highly persuasive cold email selling '{product_name}' to '{target_audience}'. Keep it under 150 words. Focus on solving a specific problem for them. Include a strong Call to Action."
                response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
                st.success("Email Ready!")
                st.write(response.text)

# ---------------------------------------------------------
# AGENT 2: THE SEO BLOG AGENT
# ---------------------------------------------------------
elif agent_choice == "✍️ The SEO Blog Agent":
    st.title("✍️ The SEO Blog Agent")
    st.write("Writes Google-ranking blog posts for your company website.")
    
    blog_topic = st.text_input("What is the blog post about?")
    keywords = st.text_input("Enter 3 SEO Keywords:")
    
    if st.button("Write Blog Post 📝"):
        if not api_key:
            st.error("⚠️ Please enter your API Key in the sidebar.")
        else:
            with st.spinner("Researching and writing..."):
                client = genai.Client(api_key=api_key)
                prompt = f"Write a professional, 400-word SEO blog post about '{blog_topic}'. You must naturally include these keywords: {keywords}. Format it with nice headings and bullet points."
                response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
                st.success("Blog Post Ready!")
                st.write(response.text)

# ---------------------------------------------------------
# AGENT 3: THE SOCIAL MEDIA AGENT
# ---------------------------------------------------------
elif agent_choice == "📱 The Social Media Agent":
    st.title("📱 The Social Media Agent")
    st.write("Turns any topic into a viral Twitter/X Thread and LinkedIn Post.")
    
    topic = st.text_area("Paste your ideas, an article, or a topic here:")
    
    if st.button("Create Social Content 📲"):
        if not api_key:
            st.error("⚠️ Please enter your API Key in the sidebar.")
        else:
            with st.spinner("Creating viral content..."):
                client = genai.Client(api_key=api_key)
                prompt = f"Act as an expert social media manager. Take this topic: '{topic}'. First, write a highly engaging LinkedIn post. Then, below that, write a viral 3-part Twitter thread about it. Use appropriate emojis."
                response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
                st.success("Social Content Ready!")
                st.write(response.text)
