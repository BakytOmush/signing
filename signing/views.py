# from django.shortcuts import render, redirect
from django.shortcuts import render, redirect, get_object_or_404
from .forms import DocumentForm
from .models import Document
from .utils import sign_document  # Убедитесь, что этот модуль и функция действительно существуют

def upload_and_sign(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document_content = document.document.read()

            # Определите тип файла и используйте соответствующий метод подписи
            if document.document.name.endswith('.docx'):
                document.signature = sign_word_document(document_content)  # Убедитесь, что у вас есть этот метод
            elif document.document.name.endswith('.pdf'):
                document.signature = sign_pdf_document(document_content)  # И этот метод тоже
            else:
                # Неверный тип файла
                form.add_error(None, "Only Word and PDF files are supported.")
                return render(request, 'upload.html', {'form': form})

            document.save()
            return redirect('verify_signature')  # Убедитесь, что у вас есть URL с именем 'verify_signature'
    else:
        form = DocumentForm()

    return render(request, 'upload.html', {'form': form})

def sign_document_page(request, document_id):
    # Тут вы можете реализовать логику подписи
    document = get_object_or_404(Document, id=document_id)
    return render(request, 'sign.html', {'document': document})