import openai
import os
import json

def generate_script(topic):
    openai.api_key = os.environ.get("OPENAI_API_KEY")
    prompt = f"Write a gentle, cozy 30-second script to help someone relax. Topic: {topic}"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content']

if __name__ == "__main__":
    topic = "breathing with candlelight"
    script = generate_script(topic)
    with open(f"scripts/{topic.replace(' ', '_')}.txt", "w") as f:
        f.write(script)
    print("Script generated.")
