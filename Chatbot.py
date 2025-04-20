import openai

# Set your OpenAI API key
openai.api_key ="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"

def chatbot_response(user_input):
    try:
        # Query the OpenAI model for a response
        response = openai.Completion.create(
            model="gpt-3.5-turbo",  # Or "gpt-3.5-turbo" / "gpt-4" if you have access
            prompt=user_input,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.9
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"Error: {str(e)}"

print("Chatbot is ready! Type 'exit' to quit the conversation.")
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")



    # it needs to pay
