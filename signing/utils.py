from cryptography.fernet import Fernet
import docx
import PyPDF2
from io import BytesIO

KEY = Fernet.generate_key()  # В реальных условиях храните этот ключ в безопасном месте!

def sign_document(document_content):
    cipher = Fernet(KEY)
    return cipher.encrypt(document_content)

def verify_signature(document_content, signature):
    cipher = Fernet(KEY)
    try:
        decrypted = cipher.decrypt(signature)
        return decrypted == document_content
    except:
        return False
def sign_word_document(document_content):
    doc = docx.Document(BytesIO(document_content))
    # Здесь можно добавить дополнительные действия с документом, если необходимо
    return sign_document(document_content)

def verify_word_signature(document_content, signature):
    return verify_signature(document_content, signature)

def sign_pdf_document(document_content):
    # Если вы хотите как-то модифицировать PDF перед подписанием, делайте это здесь.
    # Используйте PyPDF2.PdfFileReader и другие инструменты
    return sign_document(document_content)

def verify_pdf_signature(document_content, signature):
    return verify_signature(document_content, signature)