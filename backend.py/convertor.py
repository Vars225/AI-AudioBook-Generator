import os
import uuid
from gtts import gTTS

def generate_audio_from_text(text: str, output_dir: str = "temp_audio") -> str:
    """
    LLM nundi vacchina enriched text ni audio (.mp3) file ga convert chesthundi.
    Audio file path ni return chesthundi.
    """
    # Text lekapothe emi cheyyodu
    if not text or not text.strip():
        raise ValueError("No text provided for audio generation.")

    # Audio files save cheyyadaniki oka temporary folder create chesthunnam
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Prathi output ki oka unique file name isthunnam (e.g., audiobook_abc123.mp3)
    # Deeni valla patha files overwrite avvavu
    unique_filename = f"audiobook_{uuid.uuid4().hex[:8]}.mp3"
    file_path = os.path.join(output_dir, unique_filename)
    
    try:
        # gTTS engine tho text ni audio ga marchadam
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(file_path)
        
        return file_path
    
    except Exception as e:
        print(f"Error during TTS conversion: {e}")
        return ""