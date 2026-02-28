import os
from dotenv import load_dotenv
import streamlit as st
from groq import Groq

# Load environment variables from .env file
env_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(env_path)
groq_api_key = os.getenv("GROQ_API_KEY")

st.title('🚀 Groq LLM Chat Demo')

# Check if API key is configured
if not groq_api_key or groq_api_key == "your_groq_api_key_here":
    st.error("❌ Groq API key not configured!")
    st.info("📋 Please:")
    st.info("1. Get your free API key from https://console.groq.com")
    st.info("2. Add it to the .env file: `GROQ_API_KEY=your_key`")
    st.stop()

try:
    client = Groq(api_key=groq_api_key)
except Exception as e:
    st.error(f"❌ Failed to initialize Groq client: {e}")
    st.stop()

st.write("💡 Ask me anything! Powered by Groq's Lightning-Fast LLMs")

input_text = st.text_input("Enter your question:")

if input_text:
    try:
        with st.spinner("⚡ Generating response..."):
            message = client.chat.completions.create(
                messages=[
                    {
                        "role":"system", "content": "You are a helpful AI assistant.",
                    },
                    {
                        "role":"user", "content": input_text,
                    }
                ],
                model="llama-3.1-8b-instant",
            )
            response = message.choices[0].message.content
        st.write("**Response:**")
        st.write(response)
    except Exception as e:
        st.error(f"❌ Error: {e}")
