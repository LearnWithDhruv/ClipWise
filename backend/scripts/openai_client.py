from openai import OpenAI

client = OpenAI(
    api_key="xai-LG5aXA3qKcqfUKfWXU9g9fHkhJ0fpXar7nv7VDHZvTk0MF97GbTkHGTJKVIbLBYuj9hKfbfIC9VDD9Zc",  # Replace with your API key
    base_url="https://api.x.ai/v1"  
)

try:
    completion = client.chat.completions.create(
        model="grok-2-1212",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Tell me about the latest AI trends."}
        ]
    )

    print("Completion Response:", completion)

except Exception as e:
    print("Error:", str(e))
