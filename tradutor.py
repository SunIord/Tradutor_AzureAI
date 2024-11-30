import os
import logging
from azure.ai.translation.document import DocumentTranslationClient
from azure.core.credentials import AzureKeyCredential

# Configuração do logger
logging.basicConfig(level=logging.DEBUG)

class DocumentTranslator:
    def __init__(self, service_endpoint: str, service_key: str):
        self.translation_client = DocumentTranslationClient(
            endpoint=service_endpoint,
            credential=AzureKeyCredential(service_key)
        )

    def submit_translation(self, document_url: str, language_code: str, job_name: str):
        try:
            # Inicia a tradução
            translation_poller = self.translation_client.begin_translate_document(
                document_url, language_code, display_name=job_name
            )
            translation_result = translation_poller.result()
            logging.info(f"Translation completed successfully with job ID: {translation_result.id}")
            return translation_result

        except Exception as error:
            logging.error(f"Translation process failed: {error}")
            return None

    def fetch_translation_status(self, translation_job_id: str):
        try:
            # Consulta o status da tradução
            job_status = self.translation_client.get_translation_job(translation_job_id)
            logging.info(f"Status fetched for job ID: {translation_job_id}")
            return job_status

        except Exception as error:
            logging.error(f"Failed to fetch status for job ID {translation_job_id}: {error}")
            return None
