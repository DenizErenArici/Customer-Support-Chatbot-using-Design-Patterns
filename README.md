# Customer Support Chatbot Application

This project is a conversational chatbot designed to provide intelligent, dynamic responses to user queries. It integrates with Google Dialogflow for AI-driven natural language processing and implements several design patterns to ensure maintainability and scalability.

---

## Features

- **Interactive Chat Interface**: Users can chat with the bot and receive meaningful responses.
- **Emotion Enhancements**: Responses include emojis to enhance user engagement.
- **Customer Support**: Provides predefined answers to common questions (e.g., order status, return policy, delivery time).
- **Dialogflow Integration**: Uses AI to handle complex and context-aware queries.
- **Flexible Design**: Implemented with reusable design patterns for clean and modular code.

---

## Design Patterns

### 1. **Singleton**
- **Purpose**: Ensures there is a single instance of critical components such as the AI model.  
- **Implementation**: Used to manage the AI model (`AIModel`) and ensure consistent access throughout the application.  
- **Integration**: Facilitates a single point of communication with Dialogflow.  

### 2. **Factory**
- **Purpose**: Dynamically selects the appropriate strategy to handle a user query.  
- **Implementation**: The `StrategyFactory` decides whether to use a greeting, farewell, or AI-based strategy based on the input message.  
- **Integration**: Ensures flexibility in handling diverse user intents.  

### 3. **Template**
- **Purpose**: Provides a reusable structure for processing user messages.  
- **Implementation**: The `MessageProcessor` class defines `preprocess`, `generate_response`, and `postprocess` methods for consistent response handling.  
- **Integration**: Used as a base to standardize how messages are handled and responses are generated.  

### 4. **Decorator**
- **Purpose**: Adds additional features to responses without modifying the core logic.  
- **Implementation**: `EmojiDecorator` and `CustomerSupportDecorator` enhance messages with emojis and helpful tips.  
- **Integration**: Applied to the chatbot to improve user interaction with enriched responses.  

### 5. **Strategy**
- **Purpose**: Defines a family of algorithms, encapsulates them, and makes them interchangeable.  
- **Implementation**: The `ResponseStrategy` interface allows the bot to use different strategies (e.g., `GreetingStrategy`, `FarewellStrategy`, or `AIStrategy`) to generate responses.  
- **Integration**: Dynamically selects a response strategy based on the user input, enabling the chatbot to handle different intents effectively.  

### 6. **State**
- **Purpose**: Allows the chatbot to change its behavior dynamically based on the current state.  
- **Implementation**: The bot's behavior (e.g., greeting, responding, or farewell) depends on the current context or state determined by user input.  
- **Integration**: Simplifies state-dependent behavior by encapsulating it into state-specific classes.

---

## Technologies Used

- **Backend**: Python  
- **Web Framework**: Flask  
- **AI/NLP**: Google Dialogflow  
- **Frontend**: HTML/CSS  

---

## Installation

### Prerequisites
- Python 3.8 or above
- Google Dialogflow account and project

### Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/chatbot.git
   cd chatbot

2. **Install Dependencies**:
   ```bash
   pip install Flask
   pip google-cloud-dialogflow
   pip python-dotenv 

### Python Packages
- **Flask**: Web framework to create and manage the chatbot interface.
- **python-dotenv**: For managing environment variables securely.
- **google-cloud-dialogflow**: For integrating Google Dialogflow API for AI-driven responses.


3. **Set Up Environment Variables**:
   ```bash
   DIALOGFLOW_PROJECT_ID=<your-dialogflow-project-id>  

4. **Run the Application**:
   ```bash
   python app.py  
