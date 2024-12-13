from abc import ABC, abstractmethod
class MessageDecorator(ABC):
    def __init__(self, message_processor):
        self._message_processor = message_processor

    @abstractmethod
    def process_message(self, message):
        pass
# Adds emojis to specific responses
class EmojiDecorator(MessageDecorator):
    def process_message(self, message):
        message = self._message_processor.process_message(message)
        if "Hello! How can I assist you today?" in message or "Goodbye! Have a great day!" in message:
            emoji = "😊"
        elif "I'm not sure how to respond to that." in message:
            emoji = "😢"
        else:
            return message

        return f"{message} {emoji}"

# Adds customer support-related responses based on specific keywords
class CustomerSupportDecorator(MessageDecorator):
    def process_message(self, message):
        message = self._message_processor.process_message(message)
        if "order status" in message.lower():
            message += "\nFor more details, please visit our order status page."
        elif "return policy" in message.lower():
            message += "\nYou can return our products within 30 days. For more details, please visit our return policy page."
        elif "delivery time" in message.lower():
            message += "\nOur standard delivery time is 3-5 working days. For more details, please visit our delivery information page."
        return message
