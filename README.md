# 📚 AI AudioBook Generator

## 🎯 Objective
AudioBook Generator is a web application that allows users to upload text documents (PDF, DOCX, TXT) and automatically converts them into high-quality audiobooks.It leverages Large Language Models (LLMs) to rewrite extracted text in an engaging, listener-friendly style before using Text-to-Speech (TTS) technology to produce downloadable audio files.

## 🛠️ Technology Stack
* **Programming Language:** Python 3.x
* **Frontend:** Streamlit
* **Backend:** FastAPI
* **Text Extraction:** PyPDF2, pdfplumber, python-docx
* **LLM Integration:** Gemini API
* **Text-to-Speech (TTS):** pyttsx3, gTTS, or Tortoise TTS 

## ⚙️ Methodology & Workflow
1. **Document Upload:** Users upload documents via the Streamlit interface.
2. **Text Extraction:** Backend parses files (PDF, DOCX, TXT) and extracts raw text
3. **LLM Enrichment:** The extracted text is processed by an LLM to rewrite it for better narration
4. **TTS Conversion:** Enriched text is fed into a TTS library to generate a high-quality .mp3 or .wav file
5. **Audio Download:** The final audio file is available for immediate download in the UI

## 🚀 How to Run the Project

**1. Clone the repository and navigate to the project folder:**
```bash
git clone <your-repo-link>
cd AudioBook_Project