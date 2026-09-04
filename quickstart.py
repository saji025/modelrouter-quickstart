import os
from openai import OpenAI

# ModelRouter Quickstart Example
# 1. Register / Login at https://modelrouter.web.id/login
# 2. Get your API Key at https://modelrouter.web.id/token

client = OpenAI(
    api_key=os.environ.get("MODELROUTER_API_KEY", "YOUR_API_KEY_HERE"),
    base_url="https://modelrouter.web.id/v1"
)

def test_modelrouter():
    print("[*] Sending request to ModelRouter...")
    response = client.chat.completions.create(
        model="deepseek-v4-flash", # or 'hy3-free', 'gemini-3.8-flash', 'claude-sonnet-4.6'
        messages=[
            {"role": "user", "content": "Halo! Berikan 3 tips coding efisien."}
        ],
        temperature=0.7
    )
    print("\n--- Response ---")
    print(response.choices[0].message.content)

if __name__ == "__main__":
    test_modelrouter()
