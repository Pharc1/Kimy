import os
from openai import OpenAI

openai_api_key = os.environ.get('OPENAI_API_KEY')
client = OpenAI()
print("L'aventure commence ici")

thread = client.beta.threads.create()

while True:
    user_input = input("> ")
    message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=user_input
    )
    run = client.beta.threads.runs.create(
    thread_id=thread.id,
    assistant_id="asst_Awlfp9XjYuPeE7fViaOAEbQb"
    )
    
    run = client.beta.threads.runs.retrieve(
    thread_id=thread.id,
    run_id=run.id
    )
    while run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
        thread_id=thread.id,
        run_id=run.id
        )
    print(run.status)
    messages = client.beta.threads.messages.list(
    thread_id=thread.id
    )
    print("Kimy >" + messages.data[0].content[0].text.value)