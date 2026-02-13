def chatbot():
    print("Chatbot: Hello! Ask me something. Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if "hi" in user or "hello" in user:
            print("Chatbot: Hello!")
        elif "how are you" in user:
            print("Chatbot: I'm doing well.")
        elif "your name" in user:
            print("Chatbot: I am a simple Python chatbot.")
        elif "capital of india" in user:
            print("Chatbot: The capital of India is New Delhi.")
        elif "bye" in user:
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: I am still learning. Please ask simple questions.")

chatbot()
