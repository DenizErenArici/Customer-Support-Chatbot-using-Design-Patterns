from abc import ABC, abstractmethod
class AIModelBase(ABC):
    @abstractmethod
    def predict(self, message, session_id):
        pass

class AIModel(AIModelBase):
    def __init__(self):
        pass
    
    def predict(self, message, session_id):
        from chatbot_patterns.facade import ChatbotFacade
        facade = ChatbotFacade()
        return facade.get_response(message, session_id)
