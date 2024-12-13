from google.cloud import dialogflow_v2 as dialogflow
import os
from dotenv import load_dotenv
import json

load_dotenv()

class ChatbotFacade:
    def __init__(self):
        self.project_id = os.getenv("DIALOGFLOW_PROJECT_ID")
        self.private_key_id = os.getenv("PRIVATE_KEY_ID")
        self.private_key = os.getenv("PRIVATE_KEY").replace('\\n', '\n')
        self.client_email = os.getenv("CLIENT_EMAIL")
        self.client_id = os.getenv("CLIENT_ID")
        self.auth_uri = os.getenv("AUTH_URI")
        self.token_uri = os.getenv("TOKEN_URI")
        self.auth_provider_cert_url = os.getenv("AUTH_PROVIDER_CERT_URL")
        self.client_cert_url = os.getenv("CLIENT_CERT_URL")

        credentials = {
            "type": "service_account",
            "project_id": self.project_id,
            "private_key_id": self.private_key_id,
            "private_key": self.private_key,
            "client_email": self.client_email,
            "client_id": self.client_id,
            "auth_uri": self.auth_uri,
            "token_uri": self.token_uri,
            "auth_provider_x509_cert_url": self.auth_provider_cert_url,
            "client_x509_cert_url": self.client_cert_url
        }

        # Write credentials to a temporary JSON file
        with open("temp_credentials.json", "w") as temp_file:
            json.dump(credentials, temp_file)

        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "temp_credentials.json"

        self.session_client = dialogflow.SessionsClient()

    def get_response(self, message, session_id):
        session = self.session_client.session_path(self.project_id, session_id)
        text_input = dialogflow.TextInput(text=message, language_code="en")
        query_input = dialogflow.QueryInput(text=text_input)
        try:
            response = self.session_client.detect_intent(request={"session": session, "query_input": query_input})
            return response.query_result.fulfillment_text
        except Exception as e:
            print(f"Dialogflow API error: {e}")
            return "I'm not sure how to respond to that."