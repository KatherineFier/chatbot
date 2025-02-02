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

#prompt the user to ask a question
# user_input = input("\nAsk something...\n\n")

model = "gpt-3.5-turbo"

event_flowers_description = """Now accepting orders for our Spring, Summer and Fall 2025 harvests.

Wedding and Event Flowers are sold by the bucket.

Each bucket contains approximately 150 stems, or 5 bouquets.

Customization options include bouquets, loose stems, and vase arrangements.


We recommend ordering just a few buckets, then schedule a visit to the farm about 1 week before your pick-up so we can discuss your flower needs. You can always increase or decrease your order after your visit."""

event_flowers_review_prompt = f"""
Please determine the sentiment of the current event flowers review as a single word, positive or negative. < and >, in no more than 100 words.
<{event_flowers_description}>
Make the summary exciting, this will be used in an email.
"""

messages = [
    {"role": "system", "content": "You are an expert on growing flowers and you love marketing and sales."},
    {"role": "user", "content": event_flowers_review_prompt},
]

event_flowers_summary = get_api_chat_response_message(model, messages)

event_flowers_reviews = {
"Absolutely Stunning Flowers! The flowers we ordered for our wedding were beyond perfect! The variety, freshness, and vibrant colors made our arrangements truly special. The farm visit a week before pickup was such a nice touch—it gave us confidence in our choices. Highly recommend! — Emily R.",
"Perfect for DIY Wedding Arrangements! We wanted a natural, garden-inspired look for our wedding, and these event flowers delivered! The DIY buckets were full of gorgeous, high-quality stems. Having the option to mix bouquets, loose stems, and vase arrangements made the process so easy. Will definitely order again! — Sarah & Jake T.",
"Great Experience from Start to Finish! From placing the order to picking up the flowers, the process was seamless. I loved being able to visit the farm beforehand to fine-tune my selection. The flowers were fresh, fragrant, and lasted beautifully throughout our event! — Mark D.",
"More Than Enough for My Event! I ordered a few buckets for a summer bridal shower, and they were so full that I had more than enough to decorate! The mix of seasonal flowers was perfect, and the flexibility to adjust my order after visiting the farm was a huge plus. Will definitely be back for future events! — Jessica L.",
"Seasonal Beauty at Its Best! The flowers were absolutely breathtaking! You can tell they were grown with care. I loved that we could choose from different customization options, and the staff was so helpful in making sure we got exactly what we needed. If you want fresh, locally grown flowers for your event, this is the place to go! — Olivia M."
}

event_flowers_reviews_with_sentiments = []


for review in event_flowers_reviews:
    review_prompt = f"""Give me the sentiment of {review} as one word, "positive" or "negative"."""

    review_messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": review_prompt}
    ]
    sentiment = get_api_chat_response_message(model, review_messages)

    event_flowers_reviews_with_sentiments.append({
        "review": review,
        "sentiment": sentiment
    })

# if set_user_input_category(user_input) == "question":
#     response_for_user = "Good question! " + response_for_user

# print("\n" + event_flowers_summary + "\n")
print(event_flowers_reviews_with_sentiments)