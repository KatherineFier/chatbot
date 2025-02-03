from openai import OpenAI

client = OpenAI()

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

model = "gpt-3.5-turbo"
