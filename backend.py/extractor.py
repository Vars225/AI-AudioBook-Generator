import io
import pdfplumber
import docx

def extract_text_from_pdf(file_bytes: bytes) -> str:
    """PDF nundi text extract chesthundi."""
    text = ""
    # Bytes ni memory lo file laaga open chesthunnam
    with pdfplumber.open(io.BytesIO(file_bytes)) as pdf:
        for page in pdf.pages:
            extracted = page.extract_text()
            if extracted:
                text += extracted + "\n"
    return text

def extract_text_from_docx(file_bytes: bytes) -> str:
    """Word document nundi text extract chesthundi."""
    doc = docx.Document(io.BytesIO(file_bytes))
    text = "\n".join([para.text for para in doc.paragraphs])
    return text

def extract_text_from_txt(file_bytes: bytes) -> str:
    """Text file nundi text chadavadaniki."""
    return file_bytes.decode('utf-8')

def process_file_extraction(file_bytes: bytes, filename: str) -> str:
    """
    File extension ni batti correct function ki route chesthundi.
    Idi manam main.py lo call chestham.
    """
    filename_lower = filename.lower()
    
    if filename_lower.endswith('.pdf'):
        return extract_text_from_pdf(file_bytes)
    elif filename_lower.endswith('.docx'):
        return extract_text_from_docx(file_bytes)
    elif filename_lower.endswith('.txt'):
        return extract_text_from_txt(file_bytes)
    else:
        raise ValueError("Unsupported file format. Only PDF, DOCX, and TXT are allowed.")