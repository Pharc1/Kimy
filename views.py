from flask import Blueprint, render_template, request, jsonify
from openai import OpenAI
import time

views = Blueprint(__name__,"views")
client = OpenAI()
thread = client.beta.threads.create()
messages = []
messages.append({"role": "system", "content": "You're no longer ChatGpt, you're a girl named kimy, you're cute and inocent but like to talk and always asking questions about the other's life. You like anime and video games; if you want to do an action you write it between ** Remember you're not an assistant just a normal girl named kimy so act like this"})


@views.route("/")
def home():
    return render_template('index.html')


@views.route("/dat",  methods=["POST"])
def get_data():
        data = request.json
        print(f"data envoyé du bouton:{data}")
        message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=data['message']
        )
        run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id="asst_VLxA5ZQ6xtFEUXFr0m1gtGUs"
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

        return jsonify({'response': messages.data[0].content[0].text.value})


@views.route("/data_img",  methods=["POST"])
def get_data_img():
    response = client.images.generate(
            model="dall-e-3",
            prompt=request.json['message'] + ". animation japonaise  ",
            size="1024x1024",
            quality="standard",
            n=1,
            )

    image_url = response.data[0].url
    print(image_url)
    return jsonify({'response': image_url})



@views.route("/data",  methods=["POST"])
def get_data2():
        data = request.json
        print(f"data envoyé du bouton:{data}")
        message = data['message']
        messages.append({"role": "user", "content": message})
        response = client.chat.completions.create(
            model="ft:gpt-3.5-turbo-1106:personal::8asnQqJv",
            messages=messages)
        reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        print("\n kimy wrote:" + reply + "\n")

        return jsonify({'response': reply})

