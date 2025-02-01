from openai import OpenAI

client = OpenAI()

def set_user_input_category(user_input):
    question_keywords = ["who", "what", "when", "where", "why", "how", "?"]
    for keyword in question_keywords:
        if keyword in user_input.lower():
            return "question"
    return "statement"

def get_api_chat_response_message(model, messages):
# step 1 - accepts the preferred model and list of messages
# step 2 - makes chat completions api call
# step 3 - returns the response message content


    # make the api call
    api_response = client.chat.completions.create(
        model = model,
        messages = messages
    )

    # extract the response text
    response_content = api_response.choices[0].message.content

    #return the response text
    return response_content

#prompt the user to ask a question
user_input = input("\nAsk something...\n\n")

model = "gpt-3.5-turbo"

messages = [
    {"role": "system", "content": "You are an expert on growing flowers and you love marketing and sales."},
    {"role": "user", "content": user_input}
]

response_for_user = get_api_chat_response_message(model, messages)

if set_user_input_category(user_input) == "question":
    response_for_user = "Good question! " + response_for_user

print("\n" + response_for_user + "\n")