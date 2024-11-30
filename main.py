import os
from translator import Translator

def main():
    endpoint = os.getenv("AZURE_TRANSLATOR_ENDPOINT")
    api_key = os.getenv("AZURE_TRANSLATOR_KEY")

    translator = Translator(endpoint, api_key)

    source_url = "https://example.com/path/to/your/document.pdf"  # URL do documento a ser traduzido
    target_language = "fr"  # Código do idioma de destino (ex: 'fr' para francês)
    display_name = "Technical Article Translation"

    translation_result = translator.translate_documents(source_url, target_language, display_name)

    if translation_result:
        print(f"Translation job ID: {translation_result.id}")
        print("Translation status:", translation_result.status)
    else:
        print("Translation failed.")

if __name__ == "__main__":
    main()
