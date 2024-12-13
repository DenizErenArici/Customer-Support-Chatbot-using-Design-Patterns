class MessageProcessor:
    def process_message(self, message):
        self.preprocess(message)
        response = self.generate_response(message)
        self.postprocess(response)
        return response

    def preprocess(self, message):
        pass

    def generate_response(self, message):
        raise NotImplementedError

    def postprocess(self, response):
        pass
class SimpleMessageProcessor(MessageProcessor):
    def generate_response(self, message):
        return message