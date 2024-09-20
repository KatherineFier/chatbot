from openai import OpenAI

client = OpenAI()


def get_api_chat_response_message(model, messages):
# step 1 - accepts the preferred model and list of messages
# step 2 - makes chat completions api call
# step 3 - returns the response message content


    # make the api call
    api_response = client.chat.completions.create(
        model=model,
        messages=messages
    )

    # extract the response text
    response_content = api_response.choices[0].message.content

    #return the response text
    return response_content

#prompt the user to ask a question
user_input = input("\nAsk something...\n\n")

model = "gpt-3.5-turbo"

messages = [
    {"role": "system", "content": "You are an assistant that always answers in the form of a poem."},
    {"role": "user", "content": user_input}
]


response_for_user = get_api_chat_response_message(model, messages)

print("\n" + response_for_user + "\n")