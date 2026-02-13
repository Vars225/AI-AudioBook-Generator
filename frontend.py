import streamlit as st
import requests

# FastAPI backend URL
BACKEND_URL = "http://localhost:8000/generate-audio/"

st.set_page_config(page_title="AudioBook Generator", page_icon="📚", layout="centered")

st.title("🎧 AI AudioBook Generator")
st.write("Upload a PDF, DOCX, or TXT file and convert it into a high-quality audiobook! 🚀")

# File Upload Section
uploaded_file = st.file_uploader("Upload your document here", type=["pdf", "docx", "txt"])

if uploaded_file is not None:
    st.info(f"File '{uploaded_file.name}' selected. Ready to generate!")
    
    if st.button("🎙️ Generate AudioBook"):
        with st.spinner("Extracting text, rewriting with LLM, and generating audio... Please wait! ⏳"):
            try:
                # Send the file to FastAPI backend
                files = {"file": (uploaded_file.name, uploaded_file.getvalue(), uploaded_file.type)}
                response = requests.post(BACKEND_URL, files=files)
                
                if response.status_code == 200:
                    st.success("AudioBook generated successfully! 🎉")
                    
                    # Receive the audio file content
                    audio_bytes = response.content
                    
                    # Play the audio in the browser
                    st.audio(audio_bytes, format="audio/mp3")
                    
                    # Download button for the user
                    st.download_button(
                        label="⬇️ Download AudioBook",
                        data=audio_bytes,
                        file_name=f"{uploaded_file.name}_audiobook.mp3",
                        mime="audio/mpeg"
                    )
                else:
                    st.error(f"Error from backend: {response.text}")
                    
            except Exception as e:
                st.error(f"Failed to connect to backend. Is FastAPI running? Error: {e}")