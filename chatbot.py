from chatbot_patterns.template import SimpleMessageProcessor
from chatbot_patterns.decorator import EmojiDecorator, CustomerSupportDecorator
from chatbot_patterns.facade import ChatbotFacade
from chatbot_patterns.factory import StrategyFactory
import uuid

class Chatbot:
    def __init__(self):
        self.processor = SimpleMessageProcessor()
        self.facade = ChatbotFacade()

    def handle_message(self, message, session_id=None):
        if session_id is None:
            session_id = str(uuid.uuid4())
        
        # Chooses a response strategy based on user input
        strategy = StrategyFactory.get_strategy(message)
        response = strategy.generate_response(message, session_id)
        
        # Gets AI response if strategy returns a default message
        if response == "I'm not sure how to respond to that.":
            response = self.facade.get_response(message, session_id)
    
        # Applies decorators for responses
        decorated_processor = CustomerSupportDecorator(EmojiDecorator(self.processor))
        return decorated_processor.process_message(response)