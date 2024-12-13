from abc import ABC, abstractmethod
from chatbot_patterns.strategy import GreetingStrategy, FarewellStrategy, AIStrategy
from chatbot_patterns.singleton import AIModel

class StrategyFactoryBase(ABC):
    @abstractmethod
    def get_strategy(self, message):
        pass

class StrategyFactory(StrategyFactoryBase):
    current_strategy = None
# Decides which strategy (response logic) to use based on the user input
    @staticmethod
    def get_strategy(message):
        new_strategy = None
        if "hello" in message.lower() or "hi" in message.lower():
            new_strategy = GreetingStrategy()
        elif "bye" in message.lower() or "thanks for" in message.lower() or "goodbye" in message.lower():
            new_strategy = FarewellStrategy()
        else:
            ai_model = AIModel()
            new_strategy = AIStrategy(ai_model)

        if StrategyFactory.current_strategy is not None:
            print(f"Strategy changed: {StrategyFactory.current_strategy.__class__.__name__} -> {new_strategy.__class__.__name__}")
        else:
            print(f"Strategy initialized: {new_strategy.__class__.__name__}")

        StrategyFactory.current_strategy = new_strategy
        return new_strategy
