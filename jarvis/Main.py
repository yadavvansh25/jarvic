from Backend.Chatbot import ChatBot  # Import the ChatBot function from Chatbot.py

# Main program entry point.
if __name__ == "__main__":
    while True:
        user_input = input("Enter Your Question (or type 'exit' to quit): ")  # Prompt the user for a question.
        if user_input.lower() == 'exit':  # Allow the user to exit the loop
            print("Exiting the chatbot. Goodbye!")
            break

        response = ChatBot(user_input)  # Call the ChatBot function with the user's input.
        if response is None:  # Check if the response is None and handle it gracefully.
            print("An error occurred while processing your request. Please try again.")
        else:
            print(response)  # Print the chatbot's response.
