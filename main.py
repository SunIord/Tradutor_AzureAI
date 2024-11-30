import os
from translator import DocumentTranslator

def run_translation():
    # Recupera informações de ambiente para autenticação
    translator_endpoint = os.getenv("TRANSLATOR_API_ENDPOINT")
    translator_key = os.getenv("TRANSLATOR_API_KEY")

    # Instancia o tradutor com os parâmetros necessários
    translator_service = DocumentTranslator(translator_endpoint, translator_key)

    # Configurações da tradução
    document_url = "https://example.com/path/to/document.pdf"  # URL do arquivo para tradução
    target_language_code = "fr"  # Código ISO do idioma de destino (exemplo: 'fr' para francês)
    job_name = "Article Translation Task"

    # Inicia a tradução do documento
    translation_job = translator_service.submit_translation(
        document_url, target_language_code, job_name
    )

    # Verifica se a tradução foi iniciada com sucesso
    if translation_job:
        print(f"Job ID: {translation_job.id}")
        print(f"Status da tradução: {translation_job.status}")
    else:
        print("Não foi possível iniciar a tradução.")

if __name__ == "__main__":
    run_translation()
