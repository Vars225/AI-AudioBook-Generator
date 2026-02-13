import os
import uuid
from gtts import gTTS

def generate_audio_from_text(text: str, output_dir: str = "temp_audio") -> str:
    """
    Convert text to an mp3 file and return the file path.
    """
    if not text or not text.strip():
        raise ValueError("No text provided for audio generation.")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    unique_filename = f"audiobook_{uuid.uuid4().hex[:8]}.mp3"
    file_path = os.path.join(output_dir, unique_filename)
    
    try:
        tts = gTTS(text=text, lang='en', slow=False)
        tts.save(file_path)
        return file_path
    except Exception as e:
        print(f"Error during TTS conversion: {e}")
        return ""
