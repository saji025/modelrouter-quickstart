from openai import OpenAI

# Inisialisasi client ModelRouter (OpenAI-compatible)
# Dapatkan API Key di https://modelrouter.id/keys
client = OpenAI(
    api_key="YOUR_MODELROUTER_API_KEY",
    base_url="https://modelrouter.id/v1"
)

# Contoh memanggil model DeepSeek V4.1 Flash (Bansos AI / Free Tier)
response = client.chat.completions.create(
    model="deepseek-v4.1-flash",
    messages=[
        {"role": "system", "content": "Kamu adalah asisten AI yang ramah dan to the point."},
        {"role": "user", "content": "Halo ModelRouter! Buatkan fungsi Python untuk membalik string."}
    ],
    temperature=0.7
)

print(response.choices[0].message.content)
