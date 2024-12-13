from abc import ABC, abstractmethod

class ResponseStrategy(ABC): 
    @abstractmethod
    def generate_response(self, message, session_id):
        pass
class GreetingStrategy(ResponseStrategy):
    def generate_response(self, message, session_id):
        return "Hello! How can I assist you today?"

class FarewellStrategy(ResponseStrategy):
    def generate_response(self, message, session_id):
        return "Goodbye! Have a great day!"

# Uses the AI model to predict the response
class AIStrategy(ResponseStrategy):
    def __init__(self, ai_model):
        self.ai_model = ai_model

    def generate_response(self, message, session_id):
        return self.ai_model.predict(message, session_id)