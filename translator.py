import os
import logging
from azure.ai.translation.document import DocumentTranslationClient
from azure.core.credentials import AzureKeyCredential

logging.basicConfig(level=logging.INFO)

class Translator:
    def __init__(self, endpoint: str, api_key: str):
        self.client = DocumentTranslationClient(
            endpoint=endpoint,
            credential=AzureKeyCredential(api_key)
        )

    def translate_documents(self, source_url: str, target_language: str, display_name: str):
        try:
            poller = self.client.begin_translate_document(
                source_url,
                target_language,
                display_name=display_name
            )
            result = poller.result()
            logging.info(f"Translation job '{result.id}' completed successfully.")
            return result

        except Exception as e:
            logging.error(f"Error during translation: {str(e)}")
            return None

    def get_translation_result(self, job_id: str):
        try:
            result = self.client.get_translation_job(job_id)
            logging.info(f"Fetched results for job '{job_id}'.")
            return result

        except Exception as e:
            logging.error(f"Error fetching translation results: {str(e)}")
            return None
