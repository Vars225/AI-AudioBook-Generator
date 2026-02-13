import os
import google.generativeai as genai
from dotenv import load_dotenv

# .env file nundi API key load cheyyadaniki
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Gemini API ni configure chesthunnam
genai.configure(api_key=GEMINI_API_KEY)

def rewrite_text_for_audio(raw_text: str) -> str:
    """
    Extracted raw text ni theesukoni, audiobook style lo narration ki 
    anukulanga rewrite chesthundi.
    """
    if not raw_text.strip():
        return "No text found to process."

    # Gemini model ni initialize chesthunnam
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    # Ee prompt chala important, idi LLM ki clear instructions isthundi
    prompt = f"""
    You are a professional audiobook script editor. 
    Take the following raw text extracted from a document and rewrite it for an engaging audiobook narration. 
    Please follow these rules:
    1. Remove any references to figures, tables, charts, or page numbers.
    2. Expand abbreviations where necessary so they sound natural when spoken.
    3. Make the flow smooth, conversational, and engaging for a listener.
    4. Do NOT add any extra commentary like "Here is the rewritten text", just output the script.

    Text to rewrite:
    {raw_text}
    """
    
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        # Emaina API error vasthe app crash avvakunda
        print(f"Error in LLM processing: {e}")
        return raw_text # Error vasthe fallback ga original text ichestham