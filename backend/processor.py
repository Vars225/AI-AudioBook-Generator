import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API if key is present
if GEMINI_API_KEY:
    try:
        genai.configure(api_key=GEMINI_API_KEY)
    except Exception:
        pass

def rewrite_text_for_audio(raw_text: str) -> str:
    """
    Rewrite extracted raw text for audiobook narration using a conversational style.
    Falls back to raw_text if LLM call fails or key is missing.
    """
    if not raw_text or not raw_text.strip():
        return "No text found to process."

    # If API key is missing, return the original text as a fallback
    if not GEMINI_API_KEY:
        return raw_text

    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        prompt = f"""
        You are a professional audiobook script editor.
        Rewrite the following raw text into an engaging audiobook narration. Do not add meta commentary.

        Text to rewrite:
        {raw_text}
        """
        response = model.generate_content(prompt)
        return getattr(response, 'text', raw_text)
    except Exception as e:
        print(f"Error in LLM processing: {e}")
        return raw_text
