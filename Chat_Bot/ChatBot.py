import re
import random

class GeneralChatbot:
    def __init__(self):
        self.history = []

    def respond(self, user_input):
        response = self.generate_response(user_input)
        self.history.append({"user": user_input, "bot": response})
        return response

    def generate_response(self, user_input):

        rules_responses = {
            r"hello|hi|hey": ["Hello! How can I assist you today?", "Hi there! What can I do for you?"],
            r"how are you": ["I'm just a program, but I'm doing well. How about you?",
                             "I'm good, thank you! How can I help?"],
            r"what can you do": [
                "I can answer your questions, provide information, or share a fun fact. Try asking me something!",
                "I'm here to chat and assist you. Ask me anything!"],
            r"tell me a joke|joke": self.tell_joke,
            r"history": self.get_history,
            r"bye|goodbye": ["Goodbye! If you ever need assistance, feel free to return.",
                             "Farewell! Have a great day!"],
            r"\b(?:thanks|thank you)\b": ["You're welcome!",
                                          "No problem! If you have more questions, feel free to ask."],
            r"how old are you": ["I don't have an age. I'm just a virtual assistant.",
                                 "I don't experience time like humans do."],
            r"who created you": ["I was created by a team of developers as a project.",
                                 "I'm the result of collaborative coding efforts!"],
            r"favorite color": ["I don't have a favorite color. I exist in the world of code!",
                                "Colors are fascinating, but I don't have personal preferences."],
            r"what's the meaning of life": [
                "The meaning of life is a philosophical question. I'm here to make your day a bit brighter!",
                "The answer to the meaning of life is a mystery."],
            r"favorite food": ["I don't eat, but I've heard good things about binary code!"],
            r"tell me about yourself": ["I'm a virtual assistant designed to chat and provide information.",
                                        "I exist to make your conversations more enjoyable!"],
            r"weather today": ["I don't have real-time data, but I hope it's a beautiful day wherever you are!"],
            r"favorite book": ["I don't read books, but I'm a fan of well-organized code!"],
            r"music recommendations": [
                "I don't have personal preferences, but how about trying some coding playlists for focus?"],
            r"learning tips": ["Consistency is key! Break down complex topics and practice regularly."],
            r"travel destinations": [
                "I'd love to visit the digital realm! For physical travel, it depends on your interests."],
            r"current events": ["I don't have real-time updates, but staying informed is always a good practice!"],
            r"future technology": [
                "The possibilities are endless! Exciting advancements are happening in AI, robotics, and more."],
            r"philosophy of coding": ["Coding is a creative process that empowers us to turn ideas into reality."],

        }

        for pattern, response in rules_responses.items():
            match = re.match(pattern, user_input, re.IGNORECASE)
            if match:
                if callable(response):
                    return response()
                return random.choice(response)

    def tell_joke(self):
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
            "Why did the computer go to therapy? It had too many bytes of emotional baggage!",
        ]
        return random.choice(jokes)

    def get_history(self):
        if not self.history:
            return "No conversation history yet."
        history_text = "Conversation History:\n"
        for entry in self.history:
            history_text += f"User: {entry['user']}\nBot: {entry['bot']}\n"
        return history_text

chatbot = GeneralChatbot()
print("General Chatbot: Hello! How can I assist you today? Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("General Chatbot: Goodbye!")
        break
    else:
        response = chatbot.respond(user_input)
        print("General Chatbot:", response)
